import math
import random

def sophGerm(Q):
    '''Q is a 32 bit number between 2^31 to 2^32-1'''
    P = 2*Q+1
    g = 0
    if(isprime(Q) and isprime(P)):
        for i in range(2,P):
            if(pow(i,Q,P) == 1):
                g = i
                return g
            
    else:
        return -1

def isprime(prime):
    '''checks if the number is prime using sieve function '''
    for i in range(2,math.ceil(math.sqrt(prime))):
        if(prime % i == 0):
            return False
    return True

def checker(Q):
    generator = sophGerm(Q)
    if(generator != -1):
        a = random.randrange(1,2*Q)
        b = random.randrange(1,2*Q)
        x = pow(generator,a,2*Q+1)
        y = pow(generator,b,2*Q+1)
        check1 = pow(x,b,2*Q+1)
        check2 = pow(y,a,2*Q+1)
        if(check1 == check2):
            return "The value " + str(Q) + " worked as a Sophie Germain prime and works in DHKE protocol"
    #else:
     #   return "The argument or 2*arg+1 isn't a prime"
def main():
    for i in range(pow(2,31), pow(2,32)):
        if(checker(i) == None):
            continue;
        print(checker(i))

