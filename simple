arr=[6,3,5,1,12]
a =[]
b=[]
for i in range(len(arr)):
    for j in range(len(arr)):
        if len(arr[j:j+i+1])==i+1:
            a.append(min(arr[j:j+i+1]))
    b.append(max(a))
    a.clear()
print(b)
