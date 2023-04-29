import os
import sqlite3


def get_db_conn():
    '''Method to connect with the sqlite database with the given name.

       :returns: Returns connection object or exception it it fails. 
    '''
    try:
        database_path = os.path.join(os.getcwd(), 'database/Furniture.db') 
        c = sqlite3.connect(database_path)
        connection = c.cursor()
        table_name = 'furniture'
        connection.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
        result = connection.fetchone()
        
        if result is None:
            connection.execute('''CREATE TABLE IF NOT EXISTS furniture
                                (id INTEGER PRIMARY KEY,
                                name TEXT,
                                description TEXT,
                                price REAL,
                                comment text);''')
            return c
        else:
            return c
    
    except Exception as e:
        print(e)
