# #1. You are given an array A of length N and Q queries given by the 2D array B of size Q*2. Each query consists of two integers B[i][0] and B[i][1].

# A = [16,3,3,6,7,8,17,13,7]
# B = [[2,6],[4,7],[6,7]]
# pf = []
# count = 0
# for i in range(len(A)):
#     if i%2 == 0:
#         count += A[i]
#         pf.append(count)
#     else:
#         pf.append(count)
# ans = []
# print(pf)
# for i in range(len(B)):
#     a,b = B[i][0],B[i][1]
#     if a!= 0:
#         ans.append(pf[b]-pf[a-1])
#     else:
#         ans.append(pf[b])
# print(ans)

A = [2, 1, 6, 4]
ans = 0
for i in range(len(A)):
    even = 0
    odd = 0
    for j in range(0,i):
        if j%2 == 0:
            even+=A[j]
        else:
            odd+=A[j]
    for j in range(i+1,len(A)):
        if (j-1)%2 == 0:
            even+=A[j]
        else:
            odd+=A[j]
    if even == odd:
        ans+=1
            
print(ans)
