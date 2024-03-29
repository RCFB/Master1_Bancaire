from . import app
from .database import db

def init_db():
    cursor = db.cursor()
    with app.open_resource('schema.sql') as file:
        for query in file.read().decode('utf-8').split(';'):
                cursor.execute(query)
    db.commit()


@app.cli.command('init-db')
def init_db_command():
    init_db()
