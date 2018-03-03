from . import main

@main.route('/')
def index():
    return 'Hello world!'

@main.route('/test')
def test():
    return 'Hello world!'
