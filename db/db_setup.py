import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

db_username = os.environ["DB_USERNAME"]
db_password = os.environ["DB_PASSWORD"]
db_ip_address = os.environ["IP_ADRRESS"]
database = os.environ["DATABASE"]

SQLALCHEMY_DATABASE_URL = (
    f"postgresql+psycopg2://{db_username}:{db_password}@{db_ip_address}/{database}"
)


engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={}, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True)

Base = declarative_base()

# DB Utilities
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
