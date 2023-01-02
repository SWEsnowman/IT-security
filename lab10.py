import hashlib
import random
import secrets

public_keys = [[],[]]
def createsign(M):
    return hashlib.sha256(M.encode('utf-8')).hexdigest()
def numToBinary(num) :
    if num == 0 : 
        return ""
    else :
        if num % 2 == 1 :
            return numToBinary(num//2) + "1"
        else :
            return numToBinary(num//2) + "0"
def sender(M):
    digest = numToBinary(int(createsign(M),16))
    while(not(len(digest) == 256)):
        digest = "0" + digest
    secret_keys = [[],[]]
    for i in range(2):
        for j in range(256):
            secret_keys[i].append(secrets.token_hex(32))
            public_keys[i].append(createsign(secret_keys[i][j]))
    DS = []
    for i in range(256):
        DS.append(secret_keys[int(digest[i])][i])
    return [M, DS]
def receiver(M1, DS1):
    digest1 = numToBinary(int(createsign(M1),16))
    while(not(len(digest1) == 256)):
        digest1 = "0" + digest1
    for i in range(256):
        if(createsign(DS1[i]) == public_keys[int(digest1[i])][i]):
            continue
        else:
            return False
    return True
def main(M):
    temp = sender(M)
    if(receiver(temp[0],temp[1])):
        print("The digital signature is verified")
    else:
        print("The digital signature is not verified")


def keygen(n):
    hasher = []
    hasher.append(secrets.token_hex(32))
    for i in range(1,n):
        hasher.append(createsign(hasher[i-1]))
    hasher.append(createsign(hasher[n-1]))
    hasher.reverse()
    return hasher
def SKEY(n):
    keys = keygen(n)
    currkey = keys[0]
    nextkey = client(keys[1:])
    if(currkey == nextkey):
        print("Authenticated")
    else:
        print("Not authenicated")
def client(Klist):
        return createsign(Klist[0])
            
        


    
