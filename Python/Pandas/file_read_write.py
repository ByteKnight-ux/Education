import pandas as pd

data = {
    'Name':['Raman', 'Kamala', 'Sujitha'],
    'Marks':[10,20,30]
    }
df = pd.DataFrame(data, index=[1,2,3])

# TO WRITE THE DATAFRAME TO EXCEL FILE
df.to_excel('Data.xlsx', 'Student')
# TO WRITE THE DATAFRAME TO CSV FILE
df.to_csv('Data.csv')

# READING FROM A EXCEL FILE
d = pd.read_excel('Data.xlsx')
# print(d)

# FETHCING FIRST 2 ELEMENTS
head, tail = d.head(2), d.tail(2)
# print(head)
# print(tail)

# PRINTS THE DATATYPES OF ALL THE COLUMNS
# print(d.dtypes)

print(d.info())