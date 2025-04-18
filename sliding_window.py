# A = [4, 3, 2, 6, 1]
# B = 3
# C = 11

# N= []
# l = len(A)
# sum = 0
# j=0 
# for i in range(l):
#     sum+=A[i]
#     if i>=B-1:
#         N.append(sum)
#         sum -=A[j]
#         j+=1
# if C in N:
#     print(1)
# else:
#     print(0)

# Minimum Swaps

# A = [52,7,93,47,68,26,51,44,5,41,88,19,78,38,17,13,24,74,92,5,84,27,48,49,37,59,3,56,79,26,55,60,16,83,63,40,55,9,96,29,7,22,27,74,78,38,11,65,29,52,36,21,94,46,52,47,87,33,87,70]
# B = 19

# A = [8,3,10,20,22,13,1,2,55,5,15,50]
# B = 5

# count = 0
# for i in range(len(A)):
#     if A[i] <= B:
#         count+=1

# swap = 0

# for i in range(count):
#     if A[i] > B:
#         swap+=1
# ans = swap
# l = 0
# r = count
# while r<len(A):
#     if A[l] > B:
#         swap-=1
#     if A[r] > B:
#         swap+=1
#     if swap < ans:
#         ans = swap
#     l+=1
#     r+=1
# print(ans)


#2D 
A = 5
B = [[0 for i in range(A)] for i in range(A)]
count = 1
for i in range((A+1)//2):
    for j in range(i,A-i):
        B[i][j] = count
        count+=1
    for j in range(i+1,A-i):
        B[j][A-1-i] = count
        count+=1
    for j in range(A-2-i,-1+i,-1):
        B[A-1-i][j] = count
        count+=1
    for j in range(A-2-i,i,-1):
        B[j][i] = count
        count+=1
print(B)
