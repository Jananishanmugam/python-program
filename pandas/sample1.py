#Fix Names in a Table
import pandas as pd

# Create a dictionary with the data
data = {
    'user_id': [1, 2],
    'name': ['bOB', 'aLice']
}

# Create a DataFrame from the dictionary
users = pd.DataFrame(data)

# users["name"] = users["name"].apply(lambda x: x.lower() if isinstance(x,str) else x)
users["name"] = users["name"].apply(lambda x: x[0].upper()+x[1:].lower() if isinstance(x,str) else x)
users.sort_values(by=["name"], inplace = True)
print(users)
