import random
import binascii

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))
def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'
class Mobile :

    def __init__(self, id, ovsf):
        self.ovsfCode = ovsf
        self.identifier = id
        self.ascii='hello'
        self.binary= text_to_bits(self.ascii)
        self.received=''
        self.message = random.randint(0,1)
        if (self.message == 0):
            self.message =-1
    def setOvsfCode(self, ovsf):
        self.ovsfCode = ovsf
    def setId(self, id):
        self.identifier = id
    def __str__(self):
        if(self.received==''):
            return self.identifier + " my code is " + (bin(self.ovsfCode)) + " "+ "my antena sent "+ str(self.ascii)+" I received nothing for the moment"
        try:
           return self.identifier + " my code is " + (bin(self.ovsfCode)) + " "+ "my antena sent "+ str(self.ascii)+" I received "+text_from_bits(self.received) 
        except Exception:
           return self.identifier + " my code is " + (bin(self.ovsfCode)) + " "+ "my antena sent "+ str(self.ascii)+" I received an error due to lot of noises" +"\n"+self.received

