# Merge Sorted Array

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

m=3
n=3
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6] 

# nums1 = [1]
# m = 1
# nums2=[]
# n = 0

# nums1 = [4,0,0,0,0]
# m = 1
# nums2 = [1,2,3,4]
# n = 4

l = m+n
j = m

for i in nums2:
    nums1[j] = i
    j += 1

i = 0
j = m

while j < l and i < l and n!=0:
    print(f"inside - {i,j,nums1}")
    if nums1[i] <= nums1[j]:
        i+=1
    elif nums1[i] > nums1[j]:
        temp = nums1[i]
        nums1[i]= nums1[j]
        nums1[j] = temp
        i+=1
        j+=1

print(f"result - {nums1}")

