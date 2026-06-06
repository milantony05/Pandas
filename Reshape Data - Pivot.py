import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    ans = weather.pivot(index='month', columns='city', values='temperature')
    return ans

'''
Here's what each argument in the pivot function does:

- index: It determines the rows in the new DataFrame. For this example, we use the month column from the original DataFrame as the index, which means our pivoted table will have one row for each unique value in the month column.

- columns: It determines the columns in the new DataFrame. Here, we're using the city column, which means our pivoted table will have one column for each unique value in the city column.

- values: This argument specifies the values to be used when the table is reshaped. For this example, we use the temperature column from the original DataFrame.
'''