import pandas as pd
major=pd.read_csv("major.csv")
school_info=pd.read_csv("school_info.csv")
add=major+school_info
print(add)