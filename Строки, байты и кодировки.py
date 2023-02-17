#print(ord('h'))   Вывод: 104
#print(chr(104))   Вывод: h


#for ch in 'Hello':
#   print(ord(ch)) Вывод: 104 101 108 108 111

#for code in range(128):
#    print(code, hex(code), chr(code))


bb = b'\xd1\x84'
print(bin(0xd1))
print(bin(0x84))

code = 0b10001000100
print(code, hex(code))
print(chr(code))