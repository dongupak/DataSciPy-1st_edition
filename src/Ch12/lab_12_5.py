#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# LAB 12-5 다양한 방법으로 merge 적용해 보기, 333쪽
#
import pandas as pd 

df_1 = pd.DataFrame( {'A' : ['a10', 'a11', 'a12'], 
          'B' : ['b10', 'b11', 'b12'],
          'C' : ['c10', 'c11', 'c12']} , index = ['가', '나',  '다'] )

df_2 = pd.DataFrame( {'B' : ['b23', 'b24', 'b25'],
          'C' : ['c23', 'c24', 'c25'],
          'D' : ['d23', 'd24', 'd25']} , index = ['다', '라',  '마'] )

print('left outer \n' , df_1.merge(df_2, how='left', on='B' ) )
print('right outer \n' ,df_1.merge(df_2, how='right', on='B' ) )
print('full outer \n' ,df_1.merge(df_2, how='outer', on='B' ) )
print('inner \n' ,df_1.merge(df_2, how='inner', on='B' ) )