import pandas as pd
import numpy as np
# to read the csv file
df = pd.read_csv("NashvilleHousing.csv")


# set seed for reproducibity
np.random.seed(0)
# looking at the first five rows
print(df.head(50))

# get the number of missing data point per column
missing_value_count = df.isnull().sum()

# look at the of missing point
print(missing_value_count)


# how many total missing values do we have
total_cells  = np.product(df.shape)
total_missing = missing_value_count.sum()

#  to get the percentage of the dataset that are missing
percent_missing = (total_missing/total_cells) * 100
print(percent_missing)

# 31.98190600179113

columns  = [
'OwnerName',  'OwnerAddress', 'Acreage',
'TaxDistrict', 'LandValue',
'BuildingValue', 'TotalValue',
'YearBuilt' ,   'Bedrooms' ,
'FullBath' ,    'HalfBath'
            ]
#drop columns  along the rows  and returns a new dataframe
df =  df.dropna(subset= columns, axis=0, inplace=False)


# Fill up columns 5 - 20%
df["PropertyAddress"] = \
df["PropertyAddress"].fillna("109  BAILEY VIEW CT, GOODLETTSVILLE", inplace= False)


