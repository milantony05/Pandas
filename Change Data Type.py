import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students = students.astype({'grade': int})
    return students

'''
astype Function: The astype function is used to cast a pandas object to a specified dtype (data type). astype can be used to cast a pandas object to any dtype. The astype function does not modify the original DataFrame in place. Instead, it returns a new DataFrame with the specified data type changes. If you want to reflect changes in the original DataFrame, you need to reassign the result back to it or use the copy parameter accordingly. The function’s syntax is:

- DataFrame.astype(dtype, copy=True, errors='raise')
Where:
    - dtype: It's a data type, or dict of column name -> data type.
    - copy: By default, astype always returns a newly allocated object. If copy is set to False, a new object will only be created if the old object cannot be casted to the required type.
    - errors: Controls the raising of exceptions on invalid data for the provided dtype. By default, raise is set which means exceptions will be raised.
'''