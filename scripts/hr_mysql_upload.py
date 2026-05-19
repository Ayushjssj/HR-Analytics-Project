import pandas as pd
from sqlalchemy import create_engine

# Load cleaned dataset
df = pd.read_csv("../output/cleaned_hr_data.csv")

# MySQL credentials
username = "root"
password = "Ayush%402003"
host = "localhost"
database = "hr_analytics_project"

# Create engine
engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}/{database}"
)

# Upload data
df.to_sql(
    name="hr_data",
    con=engine,
    if_exists="replace",
    index=False
)

print("HR data uploaded successfully to MySQL!")