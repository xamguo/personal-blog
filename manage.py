#!/usr/bin/env python

from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from backend.app import create_app, db
from backend.models.user import User

manager = Manager(create_app())

def make_shell_context():
  return dict(db=db, User=User)

@manager.command
def hello():
    print "hello"

manager.add_command("shell", Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()
