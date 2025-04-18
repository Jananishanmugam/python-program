#Reverse entire array
# A = [1,2,3,4,5]
# l = len(A)
# for i in range(l//2):
#     A[i],A[l-i-1] = A[l-i-1],A[i]
# print(A)


#Reverse in range
# A = [0,1,2,3,4,5,6,7]
# B = 2
# C = 6
# i = B
# j = C
# n = (B+C)//2
# while i<=n and j > n:
#     A[i],A[j] = A[j],A[i]
#     i+=1
#     j-=1
# print(A)

#array rotation to right
# A = [1,2,3,4]
# #A = [5,6,1,2,3,4]
# l = len(A)
# B = 2
# for i in range((l - B)//2):
#     A[i],A[l-i-B-1] = A[l-i-B-1], A[i]

# for i in range(B//2):
#     A[l-B+i],A[l-i-1] = A[l-i-1],A[l-B+i]

# for i in range(l//2):
#     A[i],A[l-i-1] = A[l-i-1],A[i]
 
# print(A)

# l = 3
# B = 6
# print(B//l)

    
    

    
