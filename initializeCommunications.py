from ovsfGenerator import ovsfGenerator
from Mobile import Mobile

MOBILE_NUMBER=30

#convert a number in a string of bits
def bitToString(a):
    return (bin(a)[2:])
#compute the conjugue of a binary number
def conjugue(a):
    conj=""
    for i in a:
        if(i=='0'):
           conj+='1' 
        else:
            conj+='0'

    return conj

#function which is decoding a signal in the global signal
def demodulateSignal(sig, cellPhone):
    multipliedSignal=[]
    test=0
    for i in sig :
        if(bitToString(cellPhone.ovsfCode)[test]=='1'):
            multipliedSignal.append(i)
        else:
            multipliedSignal.append(-i)
        test+=1
    value=0
    for i in multipliedSignal:
        value+=i
    if (value > 0):
        return 1
    elif(value==0):
        return 0
    else:
        return -1

#generate Codes...
listCodes = ovsfGenerator(MOBILE_NUMBER)
#generate a testing list of mobile phones
listMobile = [Mobile(str(i),listCodes[i]) for i in range(0,MOBILE_NUMBER) ]
print(listMobile)
for mobile in listMobile :
    print(mobile)
#function who generate signal
def generateGlobalSignal():
    signal = [0 for x in range(0,len(bitToString(listMobile[0].ovsfCode)))]
    #generate the global signal with the mobiles ovsf codes 
    print(len(bitToString(listMobile[0].ovsfCode)))
    for i in range(0,len(bitToString(listMobile[0].ovsfCode))):
        for mobile in listMobile :
            if(mobile.message !=0):
                if(mobile.message == 1):
                    bits=bitToString(mobile.ovsfCode)
                if(mobile.message == -1):
                    bits=conjugue(bitToString(mobile.ovsfCode))
                if(bits[i]=='0'):
                    signal[i]-=1
                else:
                    signal[i]+=1
    #signal=signal[::-1]
    print(signal)
    return signal

signal=generateGlobalSignal()
for i in listMobile :
    print(demodulateSignal(signal,i))

 



