from flask_app import app
from flask_app.controllers import templates
#this if statement needs to run underneath all our routes so that it debugs everything, not just the imports
if __name__ == "__main__":
    app.run(debug=True)
