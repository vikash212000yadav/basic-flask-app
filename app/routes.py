from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Vicky'}
    posts = [
            {
                'author': {'username': 'Abhi'},
                'body': 'Beautiful day in Bangalore!'
                },
            {
                'author': {'username': 'Kiran'},
                'body': 'The Avengers movie was so cool!'
                },
            ]
    return render_template('index.html', title='Home', user=user, posts=posts)
#    return "Welcome to the Scientist Technologies!"
