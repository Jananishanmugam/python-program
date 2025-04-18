# A = [3, 30, 34, 5, 9]
# def compare(X,Y):
#     if X+Y > Y+X:
#         return 1
#     elif X==Y:
#         return 0
#     else:
#         return -1

# import functools
# A = sorted(A, key = functools.cmp_to_key(compare))
# print(A)

A = "1111000111011"
l = []
r = []
count,count_l,count_r = 0,0,0
for i in range(len(A)):
    if A[i]=='1':
        count_l+=1
        count+=1
        l.append(count_l)
    else:
        count_l = 0
        l.append(0)
    if A[len(A)-i-1]=='1':
        count_r+=1
        r.append(count_r)
    else:
        count_r=0
        r.append(0)
r = r[::-1]
print(l)
print(r)
cnt = 0
for i in range(len(A)):
    if A[i] == '0':
        temp = l[i-1]+r[i+1]
        cnt = max(temp,cnt)
        
if cnt == 0:
    cnt = count
    print(cnt)
if cnt < count:
    cnt = cnt+1
    
print(cnt)
