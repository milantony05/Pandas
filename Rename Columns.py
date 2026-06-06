import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    students = students.rename(
        columns={
            "id": "student_id",
            "first": "first_name",
            "last": "last_name",
            "age": "age_in_years",
        }
    )
    return students

'''
rename Function Argument Definition:

- mapper, index, columns: The dictionaries you can pass to rename index or columns. In our example, we use columns.

- axis: Can be either "index" or "columns". Determines whether you're renaming the index or the columns. By default, if you provide the columns argument, you're renaming columns.

- copy: If set to True, a new DataFrame is created. If False, the original DataFrame is modified.

- inplace: If set to True, the renaming will modify the DataFrame in place and nothing will be returned. If False, a new DataFrame with renamed columns will be returned without modifying the original DataFrame.

- level: For DataFrames with multi-level index, level from which the labels should be renamed.

- errors: If 'raise', an error is raised if you try to rename an item that doesn't exist. If set to 'ignore', any failure to rename items will be ignored.
'''