import pandas as pd
from sqlalchemy import create_engine

conn_string='postgresql://postgres:admin@localhost/project1'
db=create_engine(conn_string)
conn=db.connect()

df=pd.read_csv(r'F:\PYTHON_EXCEL_SQL_PBI_Projects\SQL_Projects\Project1\Datasets\artist.csv')
print(df.info)

files=['artist', 'canvas_size', 'image_link', 'museum', 'museum_hours', 'product_size', 'subject', 'work']

for file in files:
    df=pd.read_csv(f'F:/PYTHON_EXCEL_SQL_PBI_Projects/SQL_Projects/Project1/Datasets/{file}.csv')
    df.to_sql(file , con=conn ,if_exists='replace',index=False)
    print(file)
   



