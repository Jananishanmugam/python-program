# A = [[1,2,3,4],
# [5,6,7,8],
# [9,2,3,4]]
# l = len(A)
# s = []
# for i in range(len(A[0])):
#     sum = 0
#     for j in range(l):
#         sum +=A[j][i]
#     s.append(sum)
# print(s)


#Diagonal zeros
# A = [[1,2,3],[4,5,6],[7,8,9]]
# l = len(A)
# B = []
# for i in range(l):
#     j = 0
#     k = i
#     n = []
#     while j<=i:
#         n.append(A[j][k])
#         j+=1
#         k-=1
#     a = len(n)
#     while a<=l-1:
#         n.append(0)
#         a+=1
#     B.append(n)

# for i in range(1,l):
#     k = i
#     j = l-1
#     n = []
#     while j>=i:
#         n.append(A[k][j])
#         j-=1
#         k+=1
#     a = len(n)
#     while a<=l-1:
#         n.append(0)
#         a+=1
#     B.append(n)
# print(B)


#Transpose
# A = [[1, 2],[1, 2],[1, 2]]
# l = len(A)
# k = len(A[0])
# N = [[0 for i in range(l)] for i in range(k)]
# print(l,k)
# for i in range(l):
#     j = 0
#     while j<=k-1:
#         N[j][i] = A[i][j]
#         j+=1
    
# print(N)


#Rotate 90 degree
# A = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
#  ]

# l = len(A)
# ###transpose
# for i in range(l):
#     for j in range(0,i):
#         A[j][i],A[i][j] = A[i][j],A[j][i]
# print(A)

# ###reverse
# for i in range(l):
#     A[i] = A[i][::-1]
    
# print(A)
