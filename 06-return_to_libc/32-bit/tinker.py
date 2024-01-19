#!/usr/bin/env python3

# libc_base = 0xf7c00000
# system = libc_base + 0x0004c800
# binsh = libc_base + 0x1b5faa


libc_base = 0xf7c00000
system = libc_base + 0x0004c800
binsh = libc_base + 0x1b5faa

print(hex(libc_base))
print(hex(system))
print(hex(binsh))