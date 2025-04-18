s = "abcabcbb"

max_sub = 0

r=0
l=0

dic = {}

for r in range(len(s)):
    if s[r] not in dic:
        dic[s[r]] = r
    else:
        if l <= dic[s[r]]:
            l=dic[s[r]]+1
        dic[s[r]] = r
    max_sub = max(max_sub, r - l + 1)
print(max_sub)
