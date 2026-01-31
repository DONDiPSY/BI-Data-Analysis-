#import libraries
import numpy as np
import pandas as pd
from sqlalchemy import create_engine
# to read the csv file
df = pd.read_csv("NashvilleHousing.csv")
backup_df = df.copy()
# information about the file
print(df.isnull().sum())
print(df.loc[df["SalePrice"].notna(), "SalePrice"].sample(6))



# convert column datatype
def Convert(df, SalePrice="SalePrice", data_date="SaleDate" ):
    # 1. Handle the sales and Date column (Numeric/String cleanup)
    if SalePrice in df.columns:
        # Remove (,) first
        df[SalePrice] = df[SalePrice].astype(str).replace(r"[^\d]", "", regex=True)
        # Convert datatype int64
        df[SalePrice] = pd.to_numeric(df[SalePrice], errors="coerce").astype("Int64")

    if data_date in df.columns:
        # convert to datetime
        df[data_date] = pd.to_datetime(df[data_date], format="%d-%b-%y", errors="coerce", dayfirst=True)


    return  df

Convert(df)
print(df[["SalePrice", "SaleDate"]].head())


def show_bad_values(df, col):
    # Identify rows that are not numeric in SalePrice
    mask = pd.to_numeric(df[col], errors="coerce").isna()
    return df.loc[mask, col].value_counts(dropna=False)

print(show_bad_values(backup_df, "SalePrice"))

def process_data(df, Bed="Bedrooms", fullbath="FullBath", half="HalfBath", Totalvalue="TotalValue",BuildingValue="BuildingValue"):
  for col in [Bed, fullbath, half,  Totalvalue,BuildingValue]:
      df[col] = df[col].astype("Int64")
  return  df

process_data(df)





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


#df.info()

# Ensure YearBuilt is numeric and convert to integer
df["YearBuilt"] = pd.to_numeric(df["YearBuilt"], errors="coerce").astype("Int64")

 # Age of property before it was sold
df["property_age_at_sale"] = df["SaleDate"].dt.year - df["YearBuilt"]
print(df["property_age_at_sale"].head())

df.info()


print(df.isnull().sum())
