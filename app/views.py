from app import app #imports the app variable from our app package 

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"