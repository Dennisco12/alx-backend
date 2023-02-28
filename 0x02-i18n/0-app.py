#!/usr/bin/env python3
"""This set up a flask app"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Entry point"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
