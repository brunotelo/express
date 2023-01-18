from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:root@db:3306/db-express"
# SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:root@db:3306/db-express"
SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format('root', 'root', 'db', 3306, 'db-express')
# "mysql+pymysql://sylvain:passwd@localhost/db?host=localhost?port=3306"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL#, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

Base = declarative_base()