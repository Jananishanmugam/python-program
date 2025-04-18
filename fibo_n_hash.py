#fibonacci
def fibo(A):
    if A == 0:
        return 0
    if A == 1:
        return 1
    return fibo(A-1)+fibo(A-2)

print(fibo(9))


#hashing
A = [1, 2, 3, -1, -2, 5]

pf = []
sum = 0
for i in range(len(A)):
    sum+=A[i]
    if sum not in pf:
        pass
    else:
        print(1)
    pf.append(sum)
print(A)
