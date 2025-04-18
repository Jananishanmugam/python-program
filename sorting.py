# #ELEMENTS removal
# A = [2, 1, 3, 4]
# s_A = sorted(A,reverse=True)

# count = sum(s_A)

# ans = count
# for i in range(0,len(s_A)-1):
#     ans+=count-s_A[i]
#     count = count - s_A[i]
# print(ans)


# NOBLE INTeger, find if an integer p exists in the array such that the number of integers greater than p in the array equals p.

# A = [-4,-2,0,-1,-6]
# S = sorted(A)
# print(S)
# l= len(A)
# print(l)
# for i in range(l-1):
#     if (S[i] == l-i-1) & (S[i]<S[i+1]):
#         print(S[i],1)
# if l == 1 & A[0] == 1:
#     print(1)

# Factors Sort

A = [6, 8, 9]
def fact(A):
    if A == 1:
        return 1
    count = 2
    i = 2
    while i*i <= A:
        if (A % i == 0) & (A//i == i) :
            count+=1
        elif A % i == 0:
            count+=2
        i+=1
    return count

def compare(val1, val2):
    count1 = fact(val1)
    count2 = fact(val2) 
    if count1 == count2:
        return val1 - val2
    return count1 - count2

import functools
A = sorted(A, key = functools.cmp_to_key(compare))
