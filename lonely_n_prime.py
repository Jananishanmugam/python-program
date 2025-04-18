arr = [1,2,3,4,3,2,1]

dt = {}

for i in arr:
    if i not in dt:
        dt[i]=1
    else:
        dt[i]+=1
        
print(dt)
for i in dt.keys():
    if dt[i] == 1:
        print(i)
        break




A = 49
def isPrime(A):
    if A < 2:
        return 0
    i = 2
    while i*i<=A:
        # print(i)
        if A%i == 0:
            return 0
        i+=1
    return 1
print(isPrime(A))
