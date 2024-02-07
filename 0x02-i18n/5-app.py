#!/usr/bin/env python3
"""
Flask app
"""
from flask import (
    Flask,
    render_template,
    request,
    g
)
from flask_babel import Babel


class Config(object):
    """
    Configuration for Babel
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)
app.jinja_env.autoescape = True



users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id):
    """_summary_

    Returns:
        _type_: _description_
    """
    login_as = request.args.get('login_as')
    
    if user_id in users.keys():
        user = users[user_id]
        username = user.name
        return user
  
    if not login_as:
        return None
    
    return None

#@app.before_request
def before_request():
    """
    This function is executed before each request is processed.
    It retrieves the user and assigns it to the global variable g.user.
    """
    user = get_user()
    g.user = user
    
    
    
    
    
def get_locale():
    """
    Select and return best language match based on supported languages
    """
    loc = request.args.get('locale')
    if loc in app.config['LANGUAGES']:
        return loc
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app)  # No 'localeselector' attribute here

@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Handles / route
    """
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
