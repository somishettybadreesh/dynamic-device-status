# db/db.py
import psycopg2
import psycopg2.extras
from config import DB_URL

def get_conn():
    return psycopg2.connect(DB_URL, cursor_factory=psycopg2.extras.RealDictCursor)

def query(sql, params=None):
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, params or ())
            try:
                return cur.fetchall()
            except psycopg2.ProgrammingError:
                return None
