import hashlib
import random
import math

def createsign(M):
    return hashlib.sha256(M.encode('utf-8')).hexdigest()

def isprime(prime):
    '''checks if the number is prime using sieve function '''
    
    for i in range(2,math.ceil(math.sqrt(prime))):
        if(prime % i == 0):
            return False
    return True

def euclidean(a, b):
    '''b (mod a) with a being greater than b'''
    if(b == 1 ):
        return 1
    if (b == 0):
        return a
    return euclidean(b,a%b)
diction = {}
def euclidean1(a, b):
    '''b (mod a) with a being greater than b'''
    if(a == 1 or b == 1):
        return 1
    if(a>b):
        num = (a-a%b)/b
        diction[a%b] = [1,a,int(num),b]
        return euclidean1(b,a%b)
    else:
        num = (b-b%a)/a
        diction[b%a] = [1,a,int(num),b]
        return euclidean1(a,b%a)
def extended(a,b):
    euclidean1(a,b)
    while (diction[1][1] != a):
        temp = diction[1][0]
        diction[1][0] = diction[1][2]*diction[diction[1][3]][0]
        diction[1][1] = diction[diction[1][3]][1]
        diction[1][2] = diction[1][2]*diction[diction[1][3]][2]+temp
        diction[1][3] = diction[diction[1][3]][3]
        #print(diction[1])
    if(diction[1][0]*diction[1][1]-diction[1][2]*diction[1][3] == -1):
        #print(diction[1][2])
        return diction[1][2]
    else:
        #print(diction[1][1]-diction[1][2])
        return diction[1][1]-diction[1][2]

def RSAgen():
    lower = pow(2,31)
    upper = pow(2,32)
    p = pow(2,31)
    while(not(isprime(p))):
        p = random.randrange(lower,upper)
    q = pow(2,31)
    while(not(isprime(q))):
        q = random.randrange(lower,upper)
    N = p*q
    ToiletN = (p-1)*(q-1)
    e = random.randrange(1,ToiletN)
    while(not(euclidean(e, ToiletN)==1)):
        e = random.randrange(1,ToiletN)
    d = extended(ToiletN,e)
    return [N,e,d]
def digsign(M, N, d):
    digest = createsign(M)
    digest_60 = digest[:15]
    DS = pow(int(digest_60,16),d,N)
    return [M, DS]
def digverify(M1,DS1,N,e):
    digest = createsign(M1)
    digest_60 = digest[:15]
    verify = pow(DS1,e,N)
    if(int(digest_60,16) == verify):
        return True
    else:
        return False
def main(message):
    #this function checks to make sure that the RSA key pair is correct
    #the better way to do it would be to have the digverify function run on
    #user input to see if its the same as the original input they gave
    keygen = RSAgen()
    toreceiver = digsign(message,keygen[0],keygen[2])
    if(digverify(toreceiver[0],toreceiver[1],keygen[0],keygen[1])):
        return "The messaged was signed by the sender"
    else:
        return "The messaged wasn't signed by the sender"
