import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    students.dropna(subset=['name'], inplace=True)
    return students

'''
dropna Function Argument Definition:

1. axis: It can be {0 or 'index', 1 or 'columns'}. By default it's 0. If axis=0, it drops rows which contain missing values, and if axis=1, it drops columns which contain missing value.

2. how: Determines if row or column is removed from DataFrame, when we have at least one NA or all NA.
    - how='any' : If any NA values are present, drop that row or column (default).
    - how='all' : If all values are NA, drop that row or column.

3. thresh: Require that many non-NA values. This is an integer argument which requires a minimum number of non-NA values to keep the row/column.

4. subset: Labels along the other axis to consider, e.g. if you are dropping rows these would be a list of columns to include. This is particularly useful when you only want to consider NA values in certain columns.

5. inplace: It's a boolean which makes the changes in data frame itself if True. Always remember when using the inplace=True argument, you're modifying the original DataFrame. If you need to retain the original data for any reason, avoid using inplace=True and instead assign the result to a new DataFrame.
'''