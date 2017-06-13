import math
numberOfMobile=512
class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val

class Tree:
    def __init__(self):
        self.root = None
        self.root=Node(1)
        thislevel = [self.root]
        for i in range(0,math.ceil(math.log(numberOfMobile,2))):
            nextlevel=[]
            xornumber=pow(2,pow(2,i))-1
            for n in thislevel:
                codesize=n.v.bit_length()
                n.l=Node((n.v<<codesize)+n.v)
                n.r=Node((n.v<<codesize)+(n.v^xornumber))
                nextlevel.append(n.l)
                nextlevel.append(n.r)
            thislevel=nextlevel

    def getRoot(self):
        return self.root

    def deleteTree(self):
        # garbage collector will do this for us. 
        self.root = None

    def traverse(self):
        thislevel = [self.root]
        while thislevel:
            nextlevel = [] 
            for n in thislevel:
                print( str(bin(n.v)), end=" ")
                if n.l: nextlevel.append(n.l)
                if n.r: nextlevel.append(n.r)
            print("      ")
            thislevel = nextlevel

tree1=Tree()
tree1.traverse()
