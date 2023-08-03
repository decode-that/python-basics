# Pandas Library Demo
# Drop duplicate entries from DataFrame 
# Part 1
import pandas as pd

myDataFrame = pd.read_csv('data/important_data.csv')
print(myDataFrame.head(10))
myDataFrame.drop_duplicates(inplace=True)
print(myDataFrame.head(10))