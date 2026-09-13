from pathlib import Path
Base_Dir = Path(__file__).resolve().parent.parent
Staging_Dir = Base_Dir/"staging_paysim"
Dim_Dir = Base_Dir/"Warehouse_paysim"/"Dimesion"
Fact_Dir =Base_Dir/"Warehouse_paysim"/"Fact"


print(f"Base_Dir: {Base_Dir}")
