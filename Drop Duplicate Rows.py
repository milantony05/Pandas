import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    customers.drop_duplicates(subset='email', keep='first', inplace=True)
    return customers

'''
drop_duplicates Function Argument Definition:

- subset: This is the column label or sequence of labels to consider for identifying duplicate rows. If not provided, it considers all columns in the DataFrame.

- keep: This argument determines which duplicate row to retain.
    - 'first': (default) Drop duplicates except for the first occurrence.
    - 'last': Drop duplicates except for the last occurrence.
    - False: Drop all duplicates.

- inplace: If set to True, the changes are made directly to the object without returning a new object. If set to False (default), a new object with duplicates dropped will be returned.
'''