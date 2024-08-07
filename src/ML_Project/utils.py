# For generic functionality

import os
import sys
import pandas as pd
from src.ML_Project.exception import CustomException
from src.ML_Project.logger import logging

from dotenv import load_dotenv
import pymysql

load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv("db")

def read_sql_data():
    logging.info("Reading MySQL database started.")
    try:
        mydb = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        logging.info("Connection established...", mydb)

        # Now reading the dataset
        df = pd.read_sql_query("select * from used_cars_pricing", mydb)
        print(df.head())

        return df

    except Exception as e:
        raise CustomException(sys, e)
