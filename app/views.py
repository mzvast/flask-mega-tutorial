from flask import render_template
from app import app #imports the app variable from our app package 

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    posts = [  # fake array of posts
        { 
            'author': {'nickname': 'John'}, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': {'nickname': 'Susan'}, 
            'body': 'The Avengers movie was so cool!' 
        },
        {
            'author':{'nickname':'Zhao,the sky fucker'},
            'body':'I am not Fu!'
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)