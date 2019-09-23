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

Mitsy memory setup:
 - 0-10: 
