# Import Flask app object from project folder (For python this means from the __init__.py file)
from project import app

# Import functions from flask package
from flask import render_template

# Create new route at '/'
@app.route('/')
def home():
    # return the rendered version of file.html
    return render_template('file.html')