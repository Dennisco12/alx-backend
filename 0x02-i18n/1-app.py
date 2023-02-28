#!/usr/bin/env python3
"""This set up a flask app"""

from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config():
    """This configures the languages in app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


@app.route('/', strict_slashes=False)
def index():
    """Entry point"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
