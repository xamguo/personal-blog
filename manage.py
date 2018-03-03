#!/usr/bin/env python

from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from backend.app import create_app, db
from backend.models.user import User

app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
  return dict(app=app, db=db, User=User)

@manager.command
def hello():
    """Command test."""
    print "hello"

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

manager.add_command('db', MigrateCommand)
manager.add_command("shell", Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()
