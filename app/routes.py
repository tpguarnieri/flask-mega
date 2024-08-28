from flask import render_template
from app import app 

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