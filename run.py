# Import Flask app object from project folder (For python this means from the __init__.py file)
from project import app

# Run flask app with debug on and listening on port 8000
app.run(
    debug=True,
    port=8000
)