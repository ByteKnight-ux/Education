import pandas as pd

# CREATING A BASIC PANDAS DATAFRAME
data = {
    'Sno':[1,2,3],
    'Name':['Raman', 'Kamala', 'Sujitha'],
    'Marks':[10,20,30]}
df = pd.DataFrame(data, index=data['Sno'])
print(df)

# NOTE
# SERIES: refers to each column in a dataframe

# CREATING A SINGLE SERIES
L = [10,20,30]
sr = pd.Series(L, index=range(1,len(L)+1))
# print(sr)

# GET A MAXIMUM, MINIMUM AND AVERAGE VALUE OF A SERIES RESPECTIVELY
# print(sr.min(), sr.max(), sr.median())

# GET BASIC STATISTICS OF THE GIVEN DATAFRAME
# print(df.describe())

# NOTE
# DATAFRAME : table
# SERIES    : column
# methods are applied to the DATAFRAME AND SERIES