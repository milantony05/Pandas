import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    report = report.melt(
        id_vars=["product"],
        value_vars=["quarter_1", "quarter_2", "quarter_3", "quarter_4"],
        var_name="quarter",
        value_name="sales",
    )
    return report

'''
melt Function Argument Definition:

1. id_vars: This specifies the columns that should remain unchanged. For this problem, only the product column remains unchanged because we want every row in the output to be associated with a product.

2. value_vars: This specifies the columns that we want to "melt" or reshape into rows. In our case, these are the sales data columns for each quarter: quarter_1, quarter_2, quarter_3, and quarter_4.

3. var_name: This is the name of the new column that will store the header names from the value_vars. In our problem, these are the quarter names.

4. value_name: This is the name of the new column that will store the values from the value_vars. In our problem, this will be the sales figures for each product for each quarter.
'''