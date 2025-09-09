import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age':[25, 30, 35, 28],
    'Salary':[75000, 85000, 90000, 80000],
    'Company':['Google', 'Apple', 'Microsoft', 'Amazon']
}


dataframe = pd.DataFrame(data)
print(dataframe)

print(dataframe.shape)

#now we willl go for indexind and selection. 

#Row based indexing
print(dataframe.head(2))    #it will give first 2 rows

#Column based indexing
print(dataframe['Name'])   #it will give all the values of Name column

#Row based indexing 
print(dataframe.loc[2])    #it will give all the values of 2nd row
print(dataframe.loc[2,'Age'])

print(dataframe.iloc[2,2])  #it will give the value of 2nd row and 2nd column

#boolean indexing

print(dataframe[dataframe['Age']>30])   #it will give all the rows where Age is greater than 30

print(dataframe[dataframe['Age']>30]['Salary'])



#selection in Pandas is done by using loc and iloc.

print(dataframe.loc[2])    #it will give all the values of 2nd row
print(dataframe.loc[2,'Age'])
print(dataframe.iloc[2,2])  #it will give the value of 2nd row and 2nd column   




#GROUPING AND AGGREGATION

dataframe.groupby('Company')['Salary'].mean()

dataframe.groupby('Company')['Salary'].agg(['mean','sum'])



data2 = {
    "Department": ["IT", "IT", "HR", "HR", "Finance"],
    "Gender": ["M", "M", "F", "F", "M"],
    "Salary": [50000, 60000, 45000, 55000, 70000]
}
df2 = pd.DataFrame(data2)

#SORTING

df2.sort_values(by='Salary',ascending=False)   #sorts the values in descending order
df2.sort_index()    #rearranges the index values in ascending order




#MATPLOTLIB

import matplotlib.pyplot as plt

x=  [1,2,3,4,5  ]
y=  [10,20,30,40,50]
plt.plot(
    x,
    y,
    linewidth=2,          # thickness of the line
    color='blue',         # line color
    marker='o',           # put a circle marker at each data point
    markersize=4          # size of the markers
)   #plots the points and joins them with a line
plt.title("Sample Plot",fontsize=16,fontweight='bold')
plt.xlabel("X-axis",fontsize=12)
plt.ylabel("Y-axis",fontsize=12)
plt.grid(True,alpha=0.3)  #add a grid to the plot for better readability
plt.xticks(rotation=45)  #rotate the x-axis labels so they don't overlap
plt.tight_layout()   #adjust the layout so everything fits nicely
plt.savefig('sample_plot.png',dpi=300,bbox_inches='tight')
plt.show()      #displays the plot


