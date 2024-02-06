# from flask import Flask, request

# from flask_babel import Babel, get_locale
# app = Flask(__name__)

# babel = Babel(app)

# @babel.localeselector
# def get_locale():
#     # Automatically use best match from the Accept-Language header
#     return request.accept_languages.best_match(['en', 'es', 'fr', 'de'])


from flask import Flask, request,render_template

from flask_babel import format_datetime
from datetime import datetime
app = Flask(__name__)


@app.route('/')
def home():
    now = datetime.utcnow()
    localized_time = format_datetime(now, 'yyyy-MM-dd HH:mm:ssZZZZ', locale='auto')
    return render_template('home.html', localized_time=localized_time)
