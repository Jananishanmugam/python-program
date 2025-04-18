# A = [16, 17, 4, 3, 8, 10, 5, 2]
# l = len(A)
# n = []
# n.append(A[l-1])
# mx = A[l-1]
# for i in range(l-2,0,-1):
#     if A[i] > mx:
#         mx = A[i]
#         n.append(A[i])
# print(n)

# A = [2, 6, 1, 6, 9, 1, 9, 1, 2, 3, 9, 1]
# A = [343,291,963,165,152]
A = [4,4,4,4,4]
# A = [2, 6, 1, 6, 9]
l = len(A)
mn , mx = A[0] , A[0] 
for i in range(l):
    if A[i] < mn:
        mn = A[i]
    elif A[i] > mx:
        mx = A[i]
print(mn,mx)
a,b = -1, -1
count = 1000000
for i in range(l):
    if A[i] == mn:
        a = i
    if A[i] == mx:
        b = i
    if (a!=-1) & (b!=-1):
        print(a,b)
        count = min(count,abs(a-b))
        print(count)

print(count+1)
