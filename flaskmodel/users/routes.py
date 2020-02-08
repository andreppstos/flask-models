from . import users
from .forms import RegistrationForm, LoginForm
from flask import render_template, redirect, url_for, flash


@users.route('/register', methods=['GET','POST'])
@users.route('/cadastro', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        return redirect(url_for('main.index'))
    else:
        return render_template('users/cadastro.html', form= form)


@users.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('main.index'))
    else:
        return render_template('users/login.html', form=form)