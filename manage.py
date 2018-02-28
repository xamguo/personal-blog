#!/usr/bin/env python

from flask_script import Manager
from backend.app import create_app

manager = Manager(create_app())

@manager.command
def hello():
    print "hello"

if __name__ == '__main__':
    manager.run()
