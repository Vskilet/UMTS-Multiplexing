from ovsfGenerator import ovsfGenerator
from Mobile import Mobile

listCodes = ovsfGenerator(4)
listMobile = [Mobile("A",listCodes[0]),Mobile("B",listCodes[1]),Mobile("C",listCodes[2]),Mobile("D",listCodes[3])]

for mobile in listMobile :
    print(mobile)

signal = [0,0,0,0]
for i in range(0,4):
    for mobile in listMobile :
        if(((mobile.ovsfCode>>i)%2)==0):
            signal[i]-=1
        else:
            signal[i]+=1
#signal=signal[::-1]

message=[0,0,0,0]
j=0
data = dict()

print(signal)
for mobile in listMobile :
    data[mobile.identifier]=[0,0,0,0]
print( bin(listMobile[0].ovsfCode))
for i in signal:
    for mobile in listMobile :
        if(((mobile.ovsfCode>>i)%2)==0):
            data[mobile.identifier][j]=1
        else:
            data[mobile.identifier][j]=-1
    j+=1
for i in data:
    print(i+" "+str(data[i]))





