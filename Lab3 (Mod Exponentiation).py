import time
def modexponent(a, b, N):
    start = time.time_ns()
    x = 1
    for i in range(b):
        x = (x*a)%N
        print(i)
        if(i == 10000):
            end = time.time_ns()
            print((end-start))
    end = time.time_ns()
    print((end-start))
    return x
def efficientmodexponent(a, b, N):
    start = time.time_ns()
    total = 1
    while 1:
        if (b % 2 == 1):
            #print(b)
            total = (total * a) % N
        b = b // 2
        if (b == 0):
            break
        a = a * a % N
    end = time.time_ns()
    print((end-start))
    return total

    '''x = 0;
    if(b == 1):
        return a%N
    if(b%2 == 0):
        x = ((efficientmodexponent(a, b/2, N))**2)%N
    else:
        x = (((a%N)*efficientmodexponent(a,(b-1)/2, N))**2)%N
    return x '''   
'''
def efficientmodexponent(a, b, N):
    start = time.time_ns()
    if(N == 1):
        end = time.time_ns()
        print(end-start)
        return 0;
    temp = (N - 1) * (N - 1)
    a = a%N
    while(b > 0):
        if(b%2 == 1):
            temp = (temp * a)%N
        b = b - 1
        a = (a * a)%N
    end = time.time_ns()
    print(end-start)
    return temp
'''
#function modular_pow(base, exponent, modulus) is
 #   if modulus = 1 then
  #      return 0
   # Assert :: (modulus - 1) * (modulus - 1) does not overflow base
    #result := 1
    #base := base mod modulus
    #while exponent > 0 do
#        if (exponent mod 2 == 1) then
 #           result := (result * base) mod modulus
  #      exponent := exponent >> 1
   #     base := (base * base) mod modulus
    #return result

