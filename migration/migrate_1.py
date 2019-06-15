import peewee as pw

from core.migrator import Migrator, MigrateAction

migrator = Migrator()
migrator.add_migration_actions(
    MigrateAction(migrator.add_column, "locations", "price", pw.IntegerField(default=0)),
    MigrateAction(migrator.add_column, "events", "price", pw.IntegerField(default=0)),
    MigrateAction(migrator.add_column, "routines", "price", pw.IntegerField(default=0))
)
