#!/usr/bin/env python3
from flask import Flask, render_template, request, g
from flask_babelex import Babel, gettext as _

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'translations'

babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    user_id = request.args.get('login_as')
    if user_id:
        user_id = int(user_id)
        return users.get(user_id)
    return None


@app.before_request
def before_request():
    g.user = get_user()


@babel.localeselector
def get_locale():
    user = g.get('user')
    if user and user['locale'] in ['en', 'fr']:
        return user['locale']
    locale = request.args.get('locale')
    if locale in ['en', 'fr']:
        return locale
    return request.accept_languages.best_match(['en', 'fr'])


@app.route('/')
def index():
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(debug=True)
