import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt

df = pd.read_csv("./data.csv")  # create new pandas dataframe

cameroon_data = df.loc[1212: 1214]

cameroon_data = cameroon_data.drop(
    columns=["Area Code", "Item Code", "Area", "Item", "Element Code", "Element", "Unit"])

# print(cameroon_data)

rem_cols = []
year_cols_ = cameroon_data.columns


for i in range(len(year_cols_)):
    if re.compile(r"\wF").search(year_cols_[i]) != None:
        rem_cols.append(year_cols_[i])
    else:
        pass

# print(rem_cols)
# print(re.compile(r"\wF").search("Hello"))

cameroon_data = cameroon_data.drop(columns=rem_cols)

useless_col_str = ["Area", "Item", "Element Code", "Element", "Unit"]

cm_yield = cameroon_data.loc[1212]
cm_yield = cm_yield.drop(columns=useless_col_str)
cm_yield = cm_yield.to_dict()

yield_y = []
yield_x = []

for k in cm_yield.keys():
    yield_y.append(k)
    yield_x.append(cm_yield[k])

plt.plot(yield_y, yield_x)
plt.show()
