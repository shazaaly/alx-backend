from flask import Flask, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

@babel.localeselector
def get_locale():
    # Attempt to get the language from the URL parameters
    return request.args.get('lang', default='en')
