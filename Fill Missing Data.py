import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products['quantity'].fillna(0, inplace=True)
    return products

'''
fillna Function Argument Definition:

The fillna function has several arguments that you can utilize, but we'll focus on the most commonly used ones:

- value: Scalar, dict, Series, or DataFrame. The value to use to fill holes (e.g. 0). This is what we use in our solution.

- method: {'backfill', 'bfill', 'pad', 'ffill', None}. Method to use for filling holes in reindexed Series. Default is None.

- axis: {0 or 'index', 1 or 'columns'}. Axis along which to fill missing values.

- inplace: Bool. If True, fills in place. Note: this will modify any other views on this object. Default is False.
'''