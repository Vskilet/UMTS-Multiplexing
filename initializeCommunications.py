from ovsfGenerator import ovsfGenerator
from Mobile import Mobile
from random import randint
import binascii

MOBILE_NUMBER=130

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

def listMobileGenerator(mobile_number):
    #generate Codes...
    listCodes = ovsfGenerator(mobile_number)
    #generate a testing list of mobile phones
    listMobile = [Mobile(str(i),listCodes[i]) for i in range(0,mobile_number) ]
    # print(listMobile)
    # for mobile in listMobile :
        # print(mobile)
    return listMobile


def generateGlobalSignal(listMobile):
    #function who generate signal
    signal = [0 for x in range(0,len(bitToString(listMobile[0].ovsfCode)))]
    #generate the global signal with the mobiles ovsf codes

    #print(len(bitToString(listMobile[0].ovsfCode)))
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
    # print(signal)
    return signal

def sendAscii(listMobile,interferenceRate,interferenceAmplitude):
    for j in range(0,len(listMobile[0].binary)):
        for i in listMobile:
            i.message=int(i.binary[j])
            if(i.message==0):
                i.message=-1
        signal=generateGlobalSignal(listMobile)
        signal=addRandomNoises(signal,interferenceAmplitude,interferenceRate)
        for k in listMobile :
            if(demodulateSignal(signal,k)==-1):
                k.received+='0'
            else:
                k.received+='1'

#add random noises in the signal, the amplitude is a number , and the rate is a percentage(0-100)
def addRandomNoises(signal, amplitude, rate):
    sig=[]
    for i in signal :
        if(randint(0,100)<rate):
            i=i+randint(-amplitude,amplitude)
        sig.append(i)
    return sig

def calculErrorRate(signal, listMobile):
    nbErrors = 0
    for i in listMobile :
        if i.message != demodulateSignal(signal,i):
            nbErrors += 1
    return nbErrors

def calculErrorRateStr(signal, listMobile):
    nbErrors = 0
    for i in listMobile :
        if i.ascii != i.unbin():
            nbErrors += 1
    return nbErrors
