#!/usr/bin/python3
import binascii
import numpy as np
#ord (for convert a char to int)

def xor(message, key): return ''.join(x if y=='0' else '0' if x=='1' else '1'  for x,y in zip(message,key))

#code0 = input("code0 :")
#data0 = input("data0 : ")
#data0 = int(input("data 0 : "),2)
#code0 = int(input("data 1"),2)
code0='0101'
data0='1101011'
#while data0 > 0 :
#    bit=data0 & 1
#    bit^code0
xored=''
for char in data0 :
    for char2 in code0:
        xored+=xor(char2,char)
print(xored)

#print("code 1 bin : "+bin(code0))
#signal=""
#for i in str(code0):
#    signal+=int(str(int(i)^data0),2)

#print("signal : "+signal)

