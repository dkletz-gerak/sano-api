from core.database.database import db
from playhouse.migrate import *


class MigrateAction:
    def __init__(self, method, *params):
        self.method = method
        self.params = params

    def execute(self):
        return self.method(*self.params)


class Migrator(MySQLMigrator):
    def __init__(self):
        self.actions = []
        super().__init__(db)

    def add_migration_actions(self, *actions):
        self.actions += actions

    def migrate(self):
        migrate(*[a.execute() for a in self.actions])
