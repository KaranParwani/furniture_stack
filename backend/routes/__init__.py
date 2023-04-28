import os
import sqlite3


def get_db_conn():
    '''Method to connect with the sqlite database with the given name.

       :returns: Returns connection object or exception it it fails. 
    '''
    try:
        database_path = os.path.join(os.getcwd(), 'database\Furniture.db') 
        conn = sqlite3.connect(database_path, check_same_thread=False)
        return conn
    except Exception as e:
        print(e)
