import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([df1, df2], axis=0)

'''
pd.concat(): A convenient function within pandas used to concatenate DataFrames either vertically (by rows) or horizontally (by columns).

- The objs parameter is a sequence or mapping of Series or DataFrame objects to be concatenated.
- The axis parameter determines the direction of concatenation:
    - axis=0 is set as the default value, which means it will concatenate DataFrames vertically (by rows).
    - axis=1 will concatenate DataFrames horizontally (by columns).
'''