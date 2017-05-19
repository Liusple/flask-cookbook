from flask import Flask
from my_app.hello.views import hello

app = Flask(__name__)
app.register_blueprint(hello)
#import my_app.hello.views
#app.debug = True
#app.config['DEBUG'] = True
#DEBUG = True
#app.config.from_pyfile('config.cfg')
#app.config.from_object('myapp.default_settings')
#app.config.from_envvar('PATH_TO_CONFIG_FILE')
