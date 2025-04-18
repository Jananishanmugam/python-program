arr = [-4, 3, -9, 0, 4, 1]
n = 6
p,l,z = 0,0,0
for i in arr:
    if i < 0 :
        l = l+1
    elif i > 0:
        p = p+1
    elif i == 0:
        z = z+1

print(round(p/n,6))
print(round(l/n,6))
print(round(z/n,6))



# A = [1,2,3,4,5]
# B = [[0, 3], [1, 2]]

# pf = A
# for i in range(1,len(A)):
#     pf[i] = pf[i-1] + A[i]

# print(pf)
# n = []
# for i in B:
#     a,b = i[0],i[1]
#     if a != 0:
#         n.append(pf[b] - pf[a-1])
#     else:
#         n.append(pf[b])
# print(n)


#equilibrium index
# A = [-7, 1, 5, 2, -4, 3, 0]
# l = len(A)
# ls = [0 for i in range(l)]
# rs = [0 for i in range(l)] 
# for i in range(1,l):
#     ls[i] = ls[i-1]+A[i-1]

# for j in range(l-1,0,-1):
#     rs[j-1] = rs[j]+A[j]

# k = 0
# while k<l:
#     if ls[k] == rs[k]:
#         print(k)
#         break
#     else:
#         k+=1
# print(ls)
# print(rs)

###Count of even numbers between the range
A = [1, 2, 3, 4, 5]
B = [   [0, 2],
        [2, 4],
        [1, 4]   ]
ev = []

for i in A:
    if i%2 == 0:
        ev.append(1)
    else:
       ev.append(0)

pf = [0 for i in range(len(A))]
pf[0] = ev[0]
for i in range(1,len(A)):
    pf[i] = pf[i-1] + ev[i]

n = []
for i in B:
    a,b = i[0],i[1]
    if a != 0:
        n.append(pf[b] - pf[a-1])
    else:
        n.append(pf[b])
print(n)
