arr = ["ate","eat","inch","tac","cat","tea","chin"]
#output = 3 (ate,eat,tea) (chin,inch) (cat, tac)

dic = {}

for i in arr:
    value = "".join(sorted(i))
    if value in dic:
        dic[value] +=1
    else:
        dic[value] = 1

print(dic)
print(len(dic.keys()))


#extend & append difference
fruits = ['apple', 'banana', 'cherry']

cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
fruits.append(cars)

print(fruits)
