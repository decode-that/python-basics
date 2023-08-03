# Pandas Library Demo
# Drop duplicate entries from DataFrame 
# Part 2
import pandas as pd

myDataFrame = pd.read_csv('data/important_data2.csv')
print(myDataFrame.head(10))
myDataFrame.drop_duplicates(subset=['order_id'],keep='first',inplace=True)
print(myDataFrame.head(10))