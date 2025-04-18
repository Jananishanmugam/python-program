# Valid Paranthesis

def paranthesis(s):
    stack = []
    open_paranth = ['{','[','(']
    for i in range(len(s)):
        if s[i] in open_paranth:
            stack.append(s[i])
        else:
            r = stack.pop()
            if s[i] == '}' and r != '{':
                return False
            if s[i] == ']' and r != '[':
                return False
            if s[i] == ')' and r != '(':
                return False
    return True

# s='{[(({))]}'
# print(paranthesis(s))


#get the count of the string 

def char_count(s):
    count,i = 0,0
    l = len(s)
    new_char = ''
    for j in range(len(s)):
        if s[i] == s[j]:
            count+=1
        else:
            if count != 0 :
                new_char += s[i]+str(count)
            else:
                new_char += s[i]
            i=j
            count = 0
    if count != 0 :
        new_char += s[i]+str(count+1)
    else:
        new_char += s[i]
    return new_char

# s = 'aaabbbcddee'
# print(char_count(s))

def flatten(arr):
    l = []
    for i in arr:
        if type(i) is list:
            l.extend(flatten(i))
        else:
            l.append(i)
    return l

# arr = [1,2,[7,9,[15,[12,9]],18,10]]
# output = [1,2,7,9,15,12,9,18,10]
# print(flatten(arr))

def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo(n-1)+fibo(n-2)

# input = 6
# fibo 0 1 1 2 3 5
# print(fibo(input))

def sum_natural(n):
    if n == 1:
        return 1
    return n+sum_natural(n-1)

# input = 6
# # 1+2+3+4+5+6 = 21
# print(sum_natural(input))

def armstrongnumber(ip):
    sm,o = 0,0
    r,i = ip,ip
    while r!=0:
        o+=1
        r = r//10
        
    while i != 0:
        m = i%10
        sm += (m**o)
        i = i//10

    if ip == sm:
        return "arm"
    else:
        return "not arm"


# How does “is” differ from “==”
#The is operator in Python checks whether two variables point to the same object, while == checks if the values of two variables are the same.
# a = [1,2]
# b = a
# print(a is b)

# a = [1,2]
# b = [1,2]
# print(a is b)

# a = [1,2]
# b = [1,2]
# print(a == b)

def nge(arr):
    stack = []
    new_arr = []

    for i in range(len(arr)-1,-1,-1):
        if not stack:
            new_arr.append(-1)
            stack.append(arr[i])
        elif arr[i] < stack[-1]:
            new_arr.append(stack[-1])
            stack.append(arr[i])
        elif arr[i] >= stack[-1]:
            while arr[i] >=stack[-1]:
                stack.pop()
            if not stack:
                new_arr.append(-1)
            else:
                new_arr.append(stack[-1])
                stack.append(arr[i])
    return new_arr[::-1]

# arr = [0,2,4,3,6,5,4,1,10]
# print(nge(arr))

# d = {"Sun":5,"Mon":3,"Tue":5,"Wed":3}
# n_d = {}
# for k,v in d.items():
#     if str(v) not in n_d.keys():
#         n_d[str(v)] = [k]
#     else:
#         n_d[str(v)].append(k)
# print(n_d)


