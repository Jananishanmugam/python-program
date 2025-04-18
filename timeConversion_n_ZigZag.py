s = '12:05:45PM'
period = s[-2:]
hour = int(s[:2])

if period == 'PM':
    if hour!= 12:
        hour +=12
elif period == 'AM':
    if hour==12:
        hour = 0

print(f"{hour:02}{s[2:-2]}")
--------------------------------------
a = [2,3,5,1,4,6,7,8,9]
n = len(a)
a.sort()
mid = int((n + 1)/2) -1
a[mid], a[n-1] = a[n-1], a[mid]

st = mid + 1
ed = n - 2

while(st <= ed):
    print(a)
    a[st], a[ed] = a[ed], a[st]
    st = st + 1
    ed = ed - 1

for i in range (n):
    if i == n-1:
        print(a[i])
    else:
        print(a[i], end = ' ')
