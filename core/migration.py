import peewee
import importlib.util
from setting import *
from core.database.database import db
from core.model.core_migration import CoreMigration


spec = importlib.util.spec_from_file_location("model", MODEL_PATH)
model_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(model_module)


def execute(name, path):
    print("Running migration script : ", name)
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    try:
        module.migrator.migrate()
    except Exception as e:
        print("An error occurred : ", e)


def create_tables_if_not_exist():
    tables = MODEL
    tables_to_create = []

    for t in tables:
        table_class = getattr(model_module, t)
        if type(table_class) == peewee.ModelBase and not table_class.table_exists():
            tables_to_create.append(table_class)

    db.create_tables(tables_to_create)


def drop_all_tables():
    tables = MODEL
    tables_to_drop = []

    for t in tables:
        table = getattr(model_module, t)
        if type(table) == peewee.ModelBase and table.table_exists():
            tables_to_drop.append(table)

    db.drop_tables(tables_to_drop)


def reset_all():
    drop_all_tables()
    create_tables_if_not_exist()
