from ovsfGenerator import ovsfGenerator
from Mobile import Mobile

#convert a number in a string of bits
def bitToString(a):
    return (bin(a)[2:])

#function which is decoding a signal in the global signal
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

#generate Codes
listCodes = ovsfGenerator(4)
#generate a testing list of mobile phones
listMobile = [Mobile("A",listCodes[0]),Mobile("B",listCodes[1]),Mobile("C",listCodes[2]),Mobile("D",listCodes[3])]
for mobile in listMobile :
    print(mobile)


signal = [0,0,0,0]
#generate the global signal with the mobiles ovsf codes (all mobiles send 1 for the moment
for i in range(0,4):
    for mobile in listMobile :
        bits=bitToString(mobile.ovsfCode)
        if(bits[i]=='0'):
            signal[i]-=1
        else:
            signal[i]+=1
#signal=signal[::-1]
print(signal)

#cheating function in order to test if the demodulation fuction works
#Actualy, with this signal the function may return True False False True, True is 1 and False is "You know..."
signal=[0,0,0,4]

#signal=[0,0,0,4]
for i in listMobile :
    print(demodulateSignal(signal,i))





