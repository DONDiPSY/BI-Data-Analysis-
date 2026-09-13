from pathlib import Path
Raw_dir= Path(__file__).resolve().parent.parent
staging_dir =  Raw_dir/"stagingOpenAQ_platform"
Dimension_dir =  Raw_dir/"Warehouse_OpenAQ"/"Dimension_OpenAQ"
Fact_dir =  Raw_dir/"Warehouse_OpenAQ"/"Fact_OpenAQ"



# Question: try to understand how to access a directory ASAP and SURE using Path !!!!