# A = [1,16,26,17,27,26,4]
# l = len(A)
# trip = 0
# for i in range(l):
#     lf = 0
#     for j in range(i+1,l):
#         if A[i] < A[j]:
#             lf += 1
#     rg = 0
#     for j in range(0,i):
#         if A[i] > A[j]:
#             rg+=1
#     print(lf,rg)
#     if (rg!=0) & (lf!=0):
#         trip += rg*lf
# print(trip)


#Josephus Problem 
# my sol:
# A = 5
# a = [i for i in range(1,A+1)]
# i = 1
# k = 0
# loop = 0
# while len(a)>1:
#     if i%2 == 0 :
#         k+=1
#         a.remove(a[k])
#     if k==len(a):
#         k = 0
#     elif k==len(a)-1:
#         k = -1
#     i+=1
#     print(a,k)

# def msbPos(n):
#     pos = 0
#     while (n != 0):
#         pos += 1
#         n = n // 2
#     return pos
# A = 12
# position = msbPos(A)
# print(position)
# j = pow(2, (position - 1))
# A = A - j
# A = A * 2
# A = A + 1
# print(A)

A = [5,4,3,5,4]
n=len(A)
# if n==1:
#     return 1
# if n==2:
#     return 0
sumEven = 0
sumOdd = 0
for i in range(n) :
    if (i % 2 == 0) :
        sumEven += A[i];

    else :
        sumOdd += A[i];
currOdd = 0
currEven = A[0]
res = 0
newEvenSum = 0
newOddSum = 0
for i in range(1,n-1):
    if i%2 :
        print(i)
        currOdd += A[i]
        print(currOdd)
        newEvenSum = currEven + sumOdd- currOdd
        print(newEvenSum)
        newOddSum = currOdd + sumEven - currEven - A[i]
        print(newOddSum)
    else :
        currEven += A[i]
        newOddSum = currOdd + sumEven  - currEven
        newEvenSum = currEven + sumOdd - currOdd -A[i]
    if (newEvenSum == newOddSum) :
        res+=1
if (sumOdd == sumEven - A[0]) :
    res+=1
if (n % 2 == 1) :
    if (sumOdd == sumEven - A[n - 1]) :
        res+=1
else :
    if (sumEven == sumOdd - A[n - 1]) :
        res+=1
print(res)
