import pandas as pd
import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=RAMS_LAPTOP\SQLEXPRESS;'
                      'Database=test_database;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()
cursor.execute('''
                IF OBJECT_ID('[dbo].[products1]', 'U') IS NOT NULL
                DROP TABLE [dbo].[products1];
		        CREATE TABLE [dbo].[products1](
	            [product_id] [int] NOT NULL,
	            [product_name] [nvarchar](50) NULL,
	            [price] [int] NULL);
	         ''')
conn.commit()