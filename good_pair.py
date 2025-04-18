
A= [510827,351151,96897,925335,299818,192489,456948,44720,510589,598577]
B = 808099
def good_pair(A,B):
    for i in range(1,len(A)):
        d = B - A[i]
        if d in A: 
            if d != A[i]:
                return 1
            j = A.index(d)
            if i!=j:
                return 1
        else:
            i+=1
    return 0

print(good_pair(A,B))
