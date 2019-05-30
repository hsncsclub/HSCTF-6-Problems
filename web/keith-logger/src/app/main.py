
from pymongo import MongoClient
from flask import Flask, request
import urllib.parse
import datetime

app = Flask(__name__)

database_address = "keith-logger-mongodb.web.chal.hsctf.com:27017"

client = MongoClient("mongodb://meow:kittiesarecute@{}".format(database_address), connect=False)
db = client.database
collection = db.collection

@app.route("/")
def home():
    return "Hello, World! nothing to see here"

@app.route("/api/admin")
def admin():
    return "didn't have time to implement this page yet. use {} for now".format(database_address)

@app.route("/api/record")
def record():
    text = request.args["text"]
    url = request.args["url"]
    
    post = {
        "text": str(urllib.parse.unquote(text)),
        "url": str(urllib.parse.unquote(url)),
        "time": str(datetime.datetime.now().time())
    }

    collection.insert_one(post)

    return str(post)

if __name__ == "__main__":
    app.run(debug=True)
