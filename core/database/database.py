import peewee as pw
import os


# If want to use pooling configuration: http://docs.peewee-orm.com/en/latest/peewee/playhouse.html#pool
db = pw.SqliteDatabase(
    os.getenv("DB_NAME"),
    pragmas={
        'journal_mode': 'wal',
    }
)
