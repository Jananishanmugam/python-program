s = "naciicata"
k =""
for i in range(1,len(s)-1):
    j = i
    l = i
    while (j>0) & (l<(len(s)-1)):
        if s[j-1] == s[l+1]:
            temp = s[j-1:l+2]
            j-=1
            l+=1
            if len(k)<len(temp):
                k = temp
        else:
            break

for i in range(len(s)-1):
    j = i
    l = i+1
    while (j>=0) & (l<len(s)):
        if s[j]==s[l]:
            temp = s[j:l+1]
            j-=1
            l+=1
            if len(k)<len(temp):
                k = temp
        else:
            break
    
print(k)
            
