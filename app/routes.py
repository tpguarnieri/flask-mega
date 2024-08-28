from flask import render_template, flash, redirect, url_for
from app import app 
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'tpguarnieri'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'I loved that movie'
        },
        {
            'author': {'username': 'Smith'},
            'body': 'I preferred the Avengers'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f"User {form.username.data}, remember_me={form.remember_me.data}")
        return redirect(url_for('index'))
    return render_template('login.html', form=form)