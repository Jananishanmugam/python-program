A = [2, 1, 2, 3, 3, 5, 6, 3, 8]

##approch 1:(works)
D = {}

for i in range(len(A)):
    if A[i] not in D.keys():
        D[A[i]] = 1
    else:
        D[A[i]]+=1

m = max(D.values())
for i in D.keys():
    if D[i] == m:
        print(i)

##approch 2: (doubt)
# indx = 0
# count = 1

# for i in range(len(A)):
#     if A[indx] == A[i]:
#         count+=1
#     else:
#         count-=1
#     if count == 0:
#         indx = i
#         count = 1
        
# print(count,A[indx])


arr = [5,3,1,2,4]
l = len(arr)

for i in range(l):
    for j in range(i,l):
        if arr[i]>arr[j]:
            c = arr[j]
            arr[j] = arr[i]
            arr[i] = c
        elif arr[j]>=arr[i]:
            pass
        
print(arr[l//2])




arr = [1,3,5,7,9]

mn = arr[0]
mx = arr[0]

count = 0

for i in range(1,5):
    if arr[i] < mn:
        mn = arr[i]
    elif arr[i] > mx:
        mx = arr[i]

for i in range(len(arr)):
    count = count+arr[i]

print(count-mx)
print(count-mn)
    
