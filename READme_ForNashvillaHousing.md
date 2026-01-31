"""
1. Create consistency and reliabity but still a partial clean up :
  - Read the CSV File
  - Convert data type
  - Drops rows with missing columns  because missing columns are more than 50 %
  - Filled up missing values because it in the range of 5%- 20% with a total of 18 rows
  -  Create Feature Engineering for "property_age_sale" to know the actual span of property before it was bought

2. Normalize SalePrice strings, convert to Int64, and inspect rows failing numeric coercion :
   - Notice some field Saleprice have currency sign without cleaning can make data unreliable
   - change data types columns like Bedroom,  FullBath , Halfbath from float to int
   - Remove ParcelID and Legal reference from  conversion because they're  identification for housing and not meant to be converted
     
