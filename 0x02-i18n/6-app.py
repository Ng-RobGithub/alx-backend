from flask import Flask, request, render_template, g
from flask_babel import Babel, _
import os

app = Flask(__name__)
babel = Babel(app)

# Sample user settings
USER_SETTINGS = {
    "user1": {"locale": "fr_FR"},
    "user2": {"locale": "es_ES"},
    # Add more users and their preferred locales as needed
}


@babel.localeselector
def get_locale():
    # 1. Locale from URL parameters
    locale = request.args.get('lang')
    if locale:
        return locale

    # 2. Locale from user settings
    user = getattr(g, 'user', None)
    if user:
        user_settings = USER_SETTINGS.get(user)
        if user_settings:
            return user_settings.get('locale')

    # 3. Locale from request header
    header_locale = request.headers.get('Accept-Language')
    if header_locale:
        return header_locale

    # 4. Default locale
    return 'en_US'  # Set your default locale here


@app.before_request
def before_request():
    ''' Simulate user authentication, you need to implement your
    own user authentication logic '''
    g.user = authenticate_user(request)


def authenticate_user(request):
    # Implement your user authentication logic here
    ''' For demonstration purposes, let's assume we extract user
    from request headers '''
    return request.headers.get('User')


@app.route('/')
def index():
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run(debug=True)
