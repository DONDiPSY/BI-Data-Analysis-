#import libraries
import numpy as np
import pandas as pd

# to read the csv file
df = pd.read_csv("NashvilleHousing.csv")
backup_df = df.copy()
# information about the file
#df.info()
# convert column datatype
def Convert(df, data_ID="ParcelID", data_date="SaleDate" ):
    # 1. Handle the ID column (Numeric/String cleanup)
    if data_ID in df.columns:
        #Remove Space First
        df[data_ID] = df[data_ID].astype(str).str.replace(r"\s+", "" , regex=True)
        # Convert to numeric
        df[data_ID] = pd.to_numeric(df[data_ID], errors='coerce')

    if data_date in df.columns:
        # convert to datetime
        df[data_date] = pd.to_datetime(df[data_date], format="%d-%b-%y", errors="coerce", dayfirst=True)


    return  df


Convert(df)
print(df[["ParcelID", "SaleDate"]].head())



# check sum of null values
#print(df.isnull().sum())

# drop NAN values  in rows  if > 50%
rows  = [
'OwnerName',  'OwnerAddress', 'Acreage',
'TaxDistrict', 'LandValue',
'BuildingValue', 'TotalValue',
'YearBuilt' ,   'Bedrooms' ,
'FullBath' ,    'HalfBath'
            ]
df =  df.dropna(subset= rows, axis=0, inplace=False)


# Fill up columns 5 - 20%
df["PropertyAddress"] = \
df["PropertyAddress"].fillna("109  BAILEY VIEW CT, GOODLETTSVILLE", inplace= False)

print(df.isnull().sum())


df.info()

# Ensure YearBuilt is numeric and convert to integer
df["YearBuilt"] = pd.to_numeric(df["YearBuilt"], errors="coerce").astype("Int64")

 # Age of property before it was sold
df["property_age_at_sale"] = df["SaleDate"].dt.year - df["YearBuilt"]
print(df["property_age_at_sale"].head())

df.info()