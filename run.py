from flask import *
from flask.ext.pymongo import PyMongo 
import json

app=Flask(__name__)
mongo = PyMongo(app)

from pymongo import Connection  
connection = Connection() 
db = connection.test_database
collection = db.test_collection
@app.route('/')
def welcome():
	return render_template('welcome.html')
@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/save/<filename>',methods=['POST'])
def save(filename=None):
	value={["filename":request.form['name'],"imagedata":request.form['data']}
	posts=db.posts
	posts.insert(value)
	return render_template('home.html')
@app.route('/gallery')
def gallery():
	posts=db.posts.findall()
	return render_template('post.html',posts=posts)
@app.route('/gallery/<filename>',methods=['GET'])
def load(filename=None):
	posts=[db.posts.find_one({"filename":filename})]
	print posts
	return render_template('load.html',value1=value1)
@app.route('/close')
def close():
	return render_template('welcome.html')

	
	
app.run(debug=True)
