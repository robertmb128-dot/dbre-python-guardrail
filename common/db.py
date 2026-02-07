# common/db.py
import pyodbc

def get_connection(conn_string: str):
    return pyodbc.connect(conn_string)

def fetch_all(conn_string: str, query: str):
    with get_connection(conn_string) as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        columns = [col[0] for col in cursor.description]
        rows = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return rows
