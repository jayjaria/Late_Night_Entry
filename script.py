# Excel code
import pandas as pd
from sqlalchemy import create_engine
import os
from urllib.parse import quote_plus
import uuid
import datetime

db_uri = (
    f"{os.getenv('DB_DIALECT')}://"
    f"{os.getenv('DB_USERNAME')}:{quote_plus(os.getenv('DB_PASSWORD'))}@"
    f"{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)

df = pd.read_excel("Student_database.xlsx")

engine = create_engine(db_uri)

df["id"] = [uuid.uuid4() for _ in range(len(df.index))]
df["created_on"] = [datetime.datetime.now() for _ in range(len(df.index))]
df["updated_on"] = [datetime.datetime.now() for _ in range(len(df.index))]
df.to_sql("students", con=engine, if_exists="append", index=False)
