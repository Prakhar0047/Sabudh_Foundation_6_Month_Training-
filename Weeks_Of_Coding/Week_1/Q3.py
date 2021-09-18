# Ques 3. Create a new DataFrame which has the data “ 'numbers': [1, 2, 3], 'colors': ['red', 'white', 'blue'] ”. Now create a new DataFrame which has the data “ 'numbers': [5, 6, 7], 'colors': ['gray', 'gold', 'silver'] ”. Append the new DataFrame into the old one.

import pandas as pd

df1 = pd.DataFrame(data=[[1,'red'],[2,'white'],[3,'blue']], columns=['numbers','colors'])
df2 = pd.DataFrame(data=[[4,'gray'],[5,'gold'],[6,'silver']], columns=['numbers','colors'])

final = df1.append(df2, ignore_index=True)

print(final)