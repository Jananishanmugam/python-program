A = 1
i = 1
while i*i<=A:
    if A//i == i:
        print(i)
    i+=1
print(-1)

------------------------
# A = 5 #length of array C
# B = 12 #sum 
# C = [2, 1, 3, 4, 7] #array

# ans = 0
# for i in range(A):
#     sum = 0
#     for j in range(i,A):
#         sum += C[j]
#         if sum <= B:
#             ans = max(sum,ans)
#         else:
#             break
# print(ans)


#sum of all subarrays

# [1,2,3,4]

# [1]         [2]         [3]     [4]
# [1,2]       [2,3]       [3,4]
# [1,2,3]     [2,3,4]
# [1,2,3,4]

#formula :
# for i in range(n):
#     sum += A[i] * (i+1) * (n-i)  ###[Column * rows]


##Return all subarrays

A = [1,2,3]
l = len(A)
S = []
for i in range(l):
    for j in range(i,l):
        S.append(A[i:j+1])
print(S) 


#increasing triplet
#i < j < k and nums[i] < nums[j] < nums[k]
#[2,1,5,0,7,4,6] #output: True
def increasingTriplet(self, nums):
        first = float('inf')
        second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False
