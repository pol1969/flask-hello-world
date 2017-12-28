#-----Flask Hello World -------#

#import the Flask class from the flask package
from flask import Flask

#create the application object
app = Flask(__name__)

# use the decorator pattern to
# link the view function to a url
@app.route("/")
@app.route("/hello")

# define the view using a function, wich  returns a string
def hello_world():
	return "Hello, World!"

if __name__ == "__main__":
	app.run()
