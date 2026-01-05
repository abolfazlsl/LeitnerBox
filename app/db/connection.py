import psycopg2
from psycopg2.extras import RealDictCursor

from app.config import Config

class Database:

    def __init__(self):
        self.params = Config.get_db_config()
        self.conn = None

    def __enter__(self):
        self.conn = psycopg2.connect(**self.params)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn :
            if exc_type:
                self.conn.rollback()
            else:
                self.conn.commit()
            self.conn.close()

    def get_cursor(self):
        return self.conn.cursor(cursor_factory=RealDictCursor)

    def execute_query(self, query, params=None):
        with self.get_cursor() as cursor:
            cursor.execute(query, params)
            return cursor.rowcount

    def fetch_all(self, query, params=None):
        #SELECT
        with self.get_cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchall()