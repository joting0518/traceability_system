from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 建立資料庫連接
db_url = "your password!"
engine = create_engine(db_url)

Session = sessionmaker(bind=engine)
session = Session()

"""
pymysql 是一個用於 Python 連接 MySQL 資料庫的驅動。當您使用 SQLAlchemy 並嘗試通過 pymysql 連接到 MySQL 時，如果未安裝此模組，就會出現這樣的錯誤。
"""