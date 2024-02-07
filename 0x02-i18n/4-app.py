#!/usr/bin/env python3
""" A script for basic flask integration"""

from flask import Flask, render_template, request
from flask_babel import Babel, gettext


app = Flask(__name__)
babel = Babel(app)
app.jinja_env.autoescape = True


class Config:
    """
    Configuration class for the application.
        Attributes:
        Languages (list): List of supported languages.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCALE = 'en'


app.config.from_object(Config)


#@babel.localeselector
def get_locale():
    """
    Get the best matching language from the request's accepted languages.

    :return: The best matching language.
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)


@app.route("/")
def hello():
    """This function returns the rendered
    template for the index.html page.
    Returns:
        The rendered template for the
        index.html page.
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(debug=True)
