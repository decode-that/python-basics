# Pandas Library Demo
# Remove Columns from DataFrame

import pandas as pd

myDataFrame = pd.read_csv('important_data.csv')
myDataFrame.drop(columns=['order_id','customer_id'], inplace=True)