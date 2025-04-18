# import pandas as pd
# df = pd.read_csv("https://raw.githubusercontent.com/jakevdp/PythonDataScienceHandbook/master/notebooks/data/births.csv")
# print(df.count())
# df1 = df.loc[(df.year == 1969),:]
# df2 = df[df['year']==1969]

# df['date'] = df['year'].astype('str')+'/' +df['month'].astype('str')
# print(df) 
def solution(A):
    # Implement your solution here
    a = sorted(A)
    a = set(a)
    print(a)
    #basic checks if positive number not present in list
    if (1 not in a) & (0 not in a):
        return 1
    m = 1
    for i in a:
        if i < 0:
            pass
        elif (i > 0) & (i == m):
            m+=1
        else:
            return m
    return m 
A = [1, 3, 2]
print(solution(A))
