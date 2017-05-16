from ovsfGenerator import ovsfGenerator
from Mobile import Mobile

listCodes = ovsfGenerator(4)
listMobile = [Mobile("A",listCodes[0]),Mobile("B",listCodes[1]),Mobile("C",listCodes[2]),Mobile("D",listCodes[3])]

for mobile in listMobile :
    print(mobile)
