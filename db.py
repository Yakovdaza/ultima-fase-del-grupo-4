from sqlite3 import Error
from flask import g
import sqlite3

def get_db():
    try: 
        if "db" not in g:
            g.db=sqlite3.connect('Base de Datos Dunn Brothers Coffee.s3db')
            g.db.row_factory = sqlite3.Row
        return g.db
    except Error:
        print(Error)
        
def close_db():
    db =g.pop('db',None)
    if db is not None:
        db.close() 
