from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    greet = "<H1>Hello, Creators</H1>"
    link = '<p><a = href = "user/Albert">Click Me!😁</a></p>'
    return greet + link


@app.route('/user/<name>')
def user(name):
    personal = f'<h1>Hello,{name}!</h1>'
    instrcution = '<p>You can change the name by changing in address bar in browser</p>'
    return personal + instrcution


if __name__ == '__main__':
    app.run(debug=True)
