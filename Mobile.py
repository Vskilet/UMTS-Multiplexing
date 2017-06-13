import random
class Mobile :

    def __init__(self, id, ovsf):
        self.ovsfCode = ovsf
        self.identifier = id
        self.message = random.randint(0,1)
        if (self.message == 0):
            self.message =-1

         

    def setOvsfCode(self, ovsf):
        self.ovsfCode = ovsf
    def setId(self, id):
        self.identifier = id
    def __str__(self):
        return u"\U0001F4F1" + self.identifier + " my code is " + (bin(self.ovsfCode)) + " "+ "my message i "+ str(self.message)




