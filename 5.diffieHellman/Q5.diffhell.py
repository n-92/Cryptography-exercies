"""
Diffie Hellman key exchange algorithm
Used for key syncing for symmetric Cryptography
"""

class DH:
    def __init__(self,p,g,secret):
        self.p = p
        self.g = g
        self.secret = secret

    def partialKey(self):
        return pow(self.g,self.secret,self.p)

    def fullKey(self,partial_key):
        return pow(partial_key,self.secret,self.p)

#alice = DH(23,5,6)
#bob = DH(23,5,15)

alice = DH(599699,3,239699)
bob = DH(599699,3,511699)

#alice sends to bob the partial key. Bob uses the partial key to generate full key
print(bob.fullKey(alice.partialKey()))
#bob sends to alice the partial key. Alice uses the partial key to generate full key
print(alice.fullKey(bob.partialKey()))

        

        
    
