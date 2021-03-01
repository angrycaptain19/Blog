from flask import Flask, render_template, url_for,request,redirect
from flask_pymongo import pymongo
from datetime import datetime
from bson.objectid import ObjectId

app = Flask(__name__)


client = pymongo.MongoClient("mongodb+srv://new:newpassword123@cluster0.pw6li.mongodb.net/blog?retryWrites=true&w=majority")
db = client.get_database('blog')

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/result')
def res():
    x = []
    cursor = db.posts
    for document in cursor.find():
        x.append(document)
    print(x)
    return render_template('new.html',thing = x)


@app.route('/', methods=['POST'])
def my_form_post():
     data = request.form
     return render_template('new.html', data=data)


if __name__ == "__main__":
    app.run(debug=True)
