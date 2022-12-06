import sqlite3
import configuration

connection = configuration.connection
table = configuration.admin_table_name

def contains(id: str) -> bool:

    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {table} WHERE userid=?", [id])
    content = cursor.fetchone()
    connection.commit()

    return content is not None