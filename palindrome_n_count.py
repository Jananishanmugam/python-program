#count factor
A = 36
count = 0
i = 1
while i*i <= A:
    if A%i == 0 :
        count+=1
        if i != A//i:
            count+=1
    i+=1

#count sort
arr = [
    63, 25, 73, 1, 98, 73, 56, 84, 86, 57, 16, 83, 8, 25, 81, 56, 9, 53, 98, 67, 
    99, 12, 83, 89, 80, 91, 39, 86, 76, 85, 74, 39, 25, 90, 59, 10, 94, 32, 44, 
    3, 89, 30, 27, 79, 46, 96, 27, 32, 18, 21, 92, 69, 81, 40, 40, 34, 68, 78, 
    24, 87, 42, 69, 23, 41, 78, 22, 6, 90, 99, 89, 50, 30, 20, 1, 43, 3, 70, 95, 
    33, 46, 44, 9, 69, 48, 33, 60, 65, 16, 82, 67, 61, 32, 21, 79, 75, 75, 13, 
    87, 70, 33
]
n = 100

result = [0] * 100

for i in arr:
    result[i]+=1

print(result)


#palindrome
def solve(A):
    if A  <= 1:
        return 1
    return A*solve(A-1)
# print(solve(4))

def palindrome(A,i,j):
    if i>=j:
        return 1
    if A[i] == A[j]:
        return palindrome(A,i+1,j-1)
    return 0

# print(palindrome("nman",0,3))
class solution:
    def solve(self,A):
        if A == 0:
            return 
        self.solve(A-1)
        print(A,end=" ")

# s = solution()
# s.solve(10)

def sumofDigits(A):
    if A==0:
        return 0
    return A%10 + sumofDigits(A//10)
    
# print(sumofDigits(1234))

def pow(A,B,C):
    if A == 0:
        return 0
    if B == 0:
        return 1
    res = pow(A,B//2,C)
    if B%2 == 0 :
        return (res*res)%C
    else:
        return (((res*res)%C)*A)%C
        
# print(pow(2,3,3))
import math
def function(n):
    if n%2 == 0:
        return 0
    return function(n-1)+function(math.floor(n/2))

print(function(5))
