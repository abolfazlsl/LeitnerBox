import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    DB_NAME = os.getenv("PG_DB", "leitner_db")
    DB_USER = os.getenv("PG_USER", "postgres")
    DB_PASSWORD = os.getenv("PG_PASS")
    DB_HOST = os.getenv("PG_HOST", "localhost")
    DB_PORT = os.getenv("PG_PORT", "5432")

    DOWNGRADE_THRESHOLD_DAYS = 2

    @classmethod
    def get_db_config(cls):
        return {
            "dbname": cls.DB_NAME,
            "user": cls.DB_USER,
            "password": cls.DB_PASSWORD,
            "host": cls.DB_HOST,
            "port": cls.DB_PORT
        }