import pandas as pd 

df_1 = pd.DataFrame({'item' : ['ring0', 'ring0', 'ring1', 'ring1'], 
                     'type' : ['Gold', 'Silver', 'Gold', 'Bronze'], 
                     'price': [20000, 10000, 50000, 30000]})

df_2 = df_1.pivot(index='item', columns='type', values='price') 
print(df_2)