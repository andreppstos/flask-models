
from flask import render_template
from . import main

@main.route('/')
@main.route('/home')
def index():
    return render_template('main/index.html')