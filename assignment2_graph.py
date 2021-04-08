import pandas as pd
import matplotlib.pyplot as plt

excel_file = 'Assignment2.xlsx'
df = pd.read_excel(excel_file)
print(df)

df.ProductID = 'Text'

data = df.describe()

assignment = df.groupby(['Salesperson']).sum().sort_values('Price',ascending=False)
print(assignment)

grand_total = df.Price.sum()
print(grand_total)

employees = {'Salesperson': ['Haleh Borzu','Dan Kennedy','Diane Cooley ','Nancy Smith','Gary Hightower','Bob Beasley',
                                'Kay Hutchson','Nancy Sure','Kay Heughs'],
                'Price': [240.68, 214.89, 198.19, 174.81, 166.68, 149.33, 121.56, 116.38,73.88]

               }

df = pd.DataFrame(employees, columns= ['Salesperson','Price'])
pivot = df.pivot_table(index=['Salesperson'], values=['Price']).plot(kind='bar',rot=0,figsize=(5,5))
plt.xlabel('Salesperson')
plt.ylabel('sum of price')
plt.title('Total sale by each saleperson')
plt.legend(loc='upper right')
plt.show()