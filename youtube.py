#Retrive the elements which match the frquency

def match_freq():
    nums = [0,0,2,2,2,3,3,3,3,5,5]
    n = 2
    # output = [0,5]

    dict = {}
    output = []

    for i in range(len(nums)):
        if nums[i] not in dict:
            dict[nums[i]] = 1
        else:
            dict[nums[i]]+=1
            
    for k,v in dict.items():
        if v == n:
            output.append(k)
    print(output)  
    
nums = [0,0,1,1,1,2,2,3,3,4,5,5]  
# output = [0,1,2,3,4,5]

i = 0
j = 1

while j<len(nums):
    if nums[i]!=nums[j]:
        nums[i+1] = nums[j]
        i=i+1
    else:
        j+=1
nums = nums[:i+1]
print(nums)
