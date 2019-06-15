import os
import peewee
import importlib.util
from src import model
from src.database import db


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
    tables = model.__all__
    tables_to_create = []
    for t in tables:
        table_class = getattr(model, t)
        if type(table_class) == peewee.ModelBase and not table_class.table_exists():
            tables_to_create.append(table_class)

    db.create_tables(tables_to_create)
    print("Created tables: ", tables_to_create)


def drop_all_tables():
    tables = model.__all__
    tables_to_drop = []
    for t in tables:
        table = getattr(model, t)
        if type(table) == peewee.ModelBase and table.table_exists():
            tables_to_drop.append(table)

    db.drop_tables(tables_to_drop)


def initialize_last_state():
    files = os.listdir(".")
    if ".last_state" not in files:
        with open(".last_state", "w") as f:
            f.write("1")


def get_last_state():
    with open(".last_state") as f:
        last_state = int(f.read())

    return last_state


def migrate(last_state):
    files = os.listdir("migration")
    exists = True

    while exists:
        filename = f"migrate_{last_state}.py"
        if filename in files:
            execute(filename, f"migration/{filename}")
            last_state += 1
        else:
            exists = False

    return last_state


def save_last_state(last_state):
    with open(".last_state", "w") as f:
        f.write(str(last_state))


def main():
    create_tables_if_not_exist()
    initialize_last_state()
    state = get_last_state()
    state = migrate(state)
    save_last_state(state)


if __name__ == "__main__":
    main()
