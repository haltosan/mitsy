## Mitsy documentation

| Syntax | Arguments | Description |
| ----------- | ----------- | ----------- |
| print;TYPE;DATA | type:data type, data:data | print the thing |
| if;CONDITION;T:F | condition:true/false, t:run if true, f:false | conditional |
| goto;LBL | lbl:label |  goto a location |
| lbl;N | n:label name | a goto location |
| .M;OFF;M1;OFF2;GOTO | m:location 1, off:offset, m1:location 2, off1:offset 2, goto: goto location (actual location) | insert a line to the table |

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
 - psuedo registers

---
registers:

eax, ebx, ecx, edx, esi, edi, ebp, esp, eip

21,  22,  23,  24,  25,  26,  27,  28,  29,
 - 21 = return value
 - 22 = temp var
 - 23 = loop counter
 - 24 = temp var
 - 25 = goto pointer
 - 26 = pointer
 - 27 = general purpose
 - 28 = stack pointer
 - 29 = instruction pointer

---
Mitsy memory setup:
 - 0-10: temp computation/comparison space
 - 11-20: temp vars
 - 21-29: registers
 - 30-50: permanent vars
 - 51-52: print space
 - 53-63: typed vars (string)
 - 64-65: typed print space (string)
 - 66-76: typed vars (float)
 - 77-78: typed print space (float)
