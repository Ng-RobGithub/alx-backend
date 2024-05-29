#!/usr/bin/env python3
from flask import Flask, render_template, request
from flask_babelex import Babel, gettext as _

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'translations'

babel = Babel(app)


@babel.localeselector
def get_locale():
    # Check if the 'locale' parameter is present in the request
    locale = request.args.get('locale')
    if locale in ['en', 'fr']:
        return locale
    return request.accept_languages.best_match(['en', 'fr'])


@app.route('/')
def index():
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)
