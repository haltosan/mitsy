## Mitsy documentation

| Syntax | Arguments | Description |
| ----------- | ----------- | ----------- |
| print;T;D | t:type, d:data | print  |
| pvar;T;V | t:type, v:variable name | print the variable |
| goto;:L | l:label |  goto a label (include :) |
| lbl;N | n:label name | a goto location |
| >LIT, D, OFF1, S, OFF2, GOTO | lit: literal, d:dest, off1:offset 1, s:source, off2:offset 2, goto: goto location (relative location) | insert a line to the table |
| var;N;T;V | n:name, t:type, v:value | create a variable and give it a value |
| mult;L;A | l:location, a:amount | multiply the location value by amount | 
| sub;L;A | l:location, a:amount | decrease the location value by amount |
| add;L;A | l:location, a:amount | increase the location value by amount |
| inc;L | l:location | increment the value at location |
| dec;L | l:location | decrement the value at location |
| if;A;B | a:location a, b:location b | a==b; stepover next line on true |
| nop; | - | no operation |
| push;L | l:location | push a value from memory onto the stack |
| pop; | - | pop the value from the top of the stack to eax |
| call;:LBL | lbl:label | call the function at :LBL |
| return; | - | return from a function call |


---

Data types:

| type   | maps to | 
| ----------- | ----------- | 
| int | 1 | 
| string | 2 |
| float | 3 |


When using variables, you need to prefix with a /
example:
`
print;/x
`
Variable names can't include the following characters:
 - ;
 - /
 - [
 - ]
 - :

## Memory setup

Traditional memory is as follows:
 - 0-3ff: RAM, Real Mode IVT
 - 400-4ff: RAM, BIOS data area
 - 500-7bff: RAM, free
 - 7c00-7dff: RAM, OS BootSector
 - 7e00-7ffff: RAM, free
 - 80000-9ffff: Extended BIOS data area
 - a0000-fffff: Various types, ROM area & video memory

(use https://wiki.osdev.org/Memory_Map_(x86) as a ref for memory)

---
Memory needs:
 - comparison space
 - temp vars
 - permanent vars
 - print space (typed for typed language vms)
 - registers
 - imediates

---
Registers:

| . | . | . | . | . | . | . | . | . |
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| eax | ebx | ecx | edx | esi | edi | ebp | esp | eip |
| 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 |
 - 21 = return value
 - 22 = general purpose
 - 23 = loop counter
 - 24 = temp var/general purpose
 - 25 = goto pointer
 - 26 = pointer
 - 27 = literal loader
 - 28 = stack pointer (*set to offset*)
 - 29 = instruction pointer


 Registers can be used at any time. Just type the all caps name (`add;EAX;1` for example)

---
Mitsy memory setup:
 - 0: holds 1 (halt)
 - 1-10: temp computation space
 - 11-20: temp vars
 - 21-29: registers
 - 30-50: permanent vars
 - 51: print space
 - 52-61: string vars
 - 62: string print space
 - 63-72: float vars
 - 73: float print space
 - 74-328: one byte math table (*filled*)
 - 329-583: one byte comparison space
 - 584-624: stack
.
 ---
 ## Virtual Machine
 The lines of the bytecode are after this pattern (almost bit bit jump):
 literal, memory location 1, offset 1, memory location 2, offset 2, goto ;
 The literal is loaded into the ebp (27).
 The memory location is a literal integer.
 The offset is a literal integer.
 The goto is a relative jump decreased by 1 (0 goes to next)
 If this where to be rewritten in a higher level language, it would look something like this:
 ```
 .
 while(memory[0]==1){
 memory[EBP] = literal;
 memory[location1 + offset1] = memory[location2 + offset2];
 EIP += (GOTO + 1)*6;
 if(memory[PRINT_ACTIVATION!=0]){
   if(memory[PRINT_ACTIVATION]==1){
     print(memory[PRINT_INT]);
   } else if(memory[PRINT_ACTIVATION]==2){
     print(memory[PRINT_STRING]);
   } else{
     print(memory[PRINT_FLOAT]);
   }
   memory[PRINT_ACTIVATION]=0;
 }
 }
 ```
