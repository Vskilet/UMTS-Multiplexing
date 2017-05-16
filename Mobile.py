class Mobile :

    def __init__(self, id, ovsf):
        self.ovsfCode = ovsf
        self.identifier = id
        
    def setOvsfCode(self, ovsf):
        self.ovsfCode = ovsf
    def setId(self, id):
        self.identifier = id
    def __str__(self):
        return u"\U0001F4F1" + self.identifier + " my code is " + str(bin(self.ovsfCode) + "")




