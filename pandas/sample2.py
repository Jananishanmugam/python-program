#Fix Names in a Table
import pandas as pd

# Create a dictionary with the data
data = {
    'user_id': [1, 2, 3, 4],
    'name': ['Winston', 'Jonathan', 'Annabelle', 'Marwan'],
    'mail': ['winston@leetcode.com','jonathanisgreat', 'bella-@leetcode.com', 'quarz#2020@leetcode.com']
}

# Create a DataFrame from the dictionary
users = pd.DataFrame(data)
# users['mail'] = users['mail'].filter(like='@leetcode.com', axis=0)
# df.name.str.contains('y')
users = users[(users.mail.str.contains('@leetcode.com') & users.mail[:-13].str.isalnum())]
# users["mail"] = users["mail"].apply(lambda x: x[:-13] if x[:-13].isalnum() else 0)
print(users)
