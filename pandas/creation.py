1. single list :
 
import pandas as pd
 
# list of strings
lst = ['Geeks', 'For', 'Geeks', 'is', 
            'portal', 'for', 'Geeks']
 
# Calling DataFrame constructor on list
df = pd.DataFrame(lst)
print(df)

------------------------------------------------------------------------
2. Dict

# list of name, degree, score
nme = ["aparna", "pankaj", "sudhir", "Geeku"]
deg = ["MBA", "BCA", "M.Tech", "MBA"]
scr = [90, 40, 80, 98]
  
# dictionary of lists 
dict = {'name': nme, 'degree': deg, 'score': scr} 
    
df = pd.DataFrame(dict)
    
print(df)
--------------------------------------------------------------------------

3.Two different lists

lst = ['Geeks', 'For', 'Geeks', 'is', 'portal', 'for', 'Geeks']
 
# list of int
lst2 = [11, 22, 33, 44, 55, 66, 77]
 
# Calling DataFrame constructor after zipping
# both lists, with columns specified
df = pd.DataFrame(list(zip(lst, lst2)),
               columns =['Name', 'val'])
print(df)

----------------------------------------------------------------------------
4.2D list and changing datatype

lst = [['tom', 'reacher', 25], ['krish', 'pete', 30],
       ['nick', 'wilson', 26], ['juli', 'williams', 22]]
   
df = pd.DataFrame(lst, columns =['FName', 'LName', 'Age'], dtype = float)
print(df)

----------------------------------------------------------------------------

5.Index and column names

# list of strings
lst = ['Geeks', 'For', 'Geeks', 'is', 'portal', 'for', 'Geeks']
 
# Calling DataFrame constructor on list
# with indices and columns specified
df = pd.DataFrame(lst, index =['a', 'b', 'c', 'd', 'e', 'f', 'g'],
                                              columns =['Names'])
print(df)
----------------------------------------------------------------------------

