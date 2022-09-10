from crypt import methods
from flask import Flask, render_template, request,redirect,url_for
from getAll import Result as r



app = Flask(__name__)

#Making url for the function
@app.route('/', methods =['POST', 'GET'])

#declaring the function
def home():
	return render_template("home_page.html")

@app.route('/search',methods=['POST','GET'])

def search():
    

if __name__ == '__main__':
	app.run(debug = True)