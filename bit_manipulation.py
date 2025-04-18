# A =  "1001011" 
# B = "11001001"
# #Ans = 100010100   
# # #1+1 = 0 carry 1
# # #1+1+carry(1) = 1 carry (1)
# # #0+1 = 1 
# # #0+0 = 0
# sum = bin(int(A,2) + int(B,2))
# print(sum[2:])


# # convert to decimal
# print(int("10101101",2))
# print(bin(76))

# a = 1010011 
# b = 1001001


#binary to decimal
# A = 22
# B = 3

# a = list(str(A))
# ans = 0
# l= len(a)
# for i in range(l):
#     ans+=int(a[i])*(B**(l-1-i))
# print(ans)

#decimal to binary
# A = 6
# B = 4

# r = 0
# i = 0
# while A > 0 :
#     r =r+(10**i)*(A%B)
#     print(r,A%B)
#     i+=1
#     A = A//B
    
# print(r)
    
    
#check bit

# A = 309
# B = 9

# b = bin(A)
# l = list(b[2:])
# l = l[::-1]
# if B>l-1:
#     print(0)
# if l[B] == '1':
#     print(1)
# else:
#     print(0)
   
# A = [1, 4, 3]
# B = 2 
# ans = 0
# mod = B
# n = len(A)
# curr = 1
# for i in range(n - 1, -1, -1):
#     dig = A[i]
#     term = (dig * curr) % mod
#     ans = (ans + term) % mod
#     curr = (curr * 10) % mod
#     print(curr)


print(sum([1,2,3]))
