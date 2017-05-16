#!/usr/bin/python3
import math
#Generate the ovsf tree
def ovsfGenerator(numberOfMobile):
#calculate the depth of the OVSF code tree
    numberOfColumn =  math.ceil(math.log(numberOfMobile,2))
    column = [1]
    #Generation of the list of codes
    for i in range (0,numberOfColumn):
        newColumn=[]
        xornumber=pow(2,pow(2,i))-1 #create a mask in order to do a bit inversion of the code
        for j in column :
            codesize = j.bit_length()
            code=(j<<codesize) + j #generate the first code by duplicating the previous code
            newColumn.append(code)
            code=(j<<codesize) + (j^xornumber) #generate the second code by duplicating the previous code and inverting all bits of it
            newColumn.append(code)
        column=newColumn
    return column

