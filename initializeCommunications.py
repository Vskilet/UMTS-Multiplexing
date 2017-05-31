from ovsfGenerator import ovsfGenerator
from Mobile import Mobile

def bitToString(a):
    return (bin(a)[2:])

def demodulateSignal(sig, cellPhone):
    k=0
    multipliedSignal=[]
    for i in sig :
        if(bitToString(cellPhone.ovsfCode)[sig.index(i)]=='1'):
            multipliedSignal.append(i)
        else:
            multipliedSignal.append(-i)
    value=0
    for i in multipliedSignal:
        value+=i
    if (value > 0):
        return True
    else:
        return False


listCodes = ovsfGenerator(4)
listMobile = [Mobile("A",listCodes[0]),Mobile("B",listCodes[1]),Mobile("C",listCodes[2]),Mobile("D",listCodes[3])]
for mobile in listMobile :
    print(mobile)

signal = [0,0,0,0]
for i in range(0,4):
    for mobile in listMobile :
        bits=bitToString(mobile.ovsfCode)
        if(bits[i]=='0'):
            signal[i]-=1
        else:
            signal[i]+=1
#signal=signal[::-1]
print(signal)
message=[0,0,0,0]
j=0
data = dict()


for mobile in listMobile :
    data[mobile.identifier]=[0,0,0,0]

for i in signal:
    for mobile in listMobile :
        bits=bitToString(mobile.ovsfCode)
        if(bits[j]=='0'):
            data[mobile.identifier][j]=1
        else:
            data[mobile.identifier][j]=-1
    j+=1
for i in data:
    print(i+" "+str(data[i]))

signal=[0,0,0,4]
for i in listMobile :
    print(demodulateSignal(signal,i))





