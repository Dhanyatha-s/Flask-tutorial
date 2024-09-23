from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "<H1>Hello World!🥳</H1>"
    
           
           