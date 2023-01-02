
diction = {}
def euclidean(a, b):
    '''b (mod a) with a being greater than b'''
    if(a == 1 or b == 1):
        return 1
    if(a>b):
        num = (a-a%b)/b
        diction[a%b] = [1,a,int(num),b]
        return euclidean(b,a%b)
    else:
        num = (b-b%a)/a
        diction[b%a] = [1,a,int(num),b]
        return euclidean(a,b%a)
def extended(a,b):
    euclidean(a,b)
    while (diction[1][1] != a):
        temp = diction[1][0]
        diction[1][0] = diction[1][2]*diction[diction[1][3]][0]
        diction[1][1] = diction[diction[1][3]][1]
        diction[1][2] = diction[1][2]*diction[diction[1][3]][2]+temp
        diction[1][3] = diction[diction[1][3]][3]
        print(diction[1])
    if(diction[1][0]*diction[1][1]-diction[1][2]*diction[1][3] == -1):
        print(diction[1][2])
        return diction[1][2]
    else:
        print(diction[1][1]-diction[1][2])
        return diction[1][1]-diction[1][2]
extended(45,7)
