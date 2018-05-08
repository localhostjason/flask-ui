#!/usr/bin/env python
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from flask_assets import ManageAssets

from app.models import *
from app.assets import assets_env
from app import app, db

manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)
manager.add_command('assets', ManageAssets(assets_env=assets_env))


@manager.command
def deploy():
    from flask_migrate import upgrade, migrate
    # 把数据库迁移到最新修订版本
    migrate()
    upgrade()

    # 创建内置用户
    User.insert_admin()


if __name__ == '__main__':
    manager.run()
