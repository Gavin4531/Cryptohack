from pwn import *

for i in range(0,256):

 if ("crypto".encode() in xor(bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"),i)):
  
  print(xor(bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"),i)) 