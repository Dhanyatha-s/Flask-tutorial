from flask import Flask, request




app = Flask(__name__)

## Routes
@app.route('/', methods=['GET'])
def hello():
    return "<h1>Hello world</h1>" , 200

@app.route('/greet/<name>')
def greet(name):
    return f'<h1>Hello {name}</h1>'



@app.route('/handle_url_params')
def handle_params():
    # Get 'greeting' and 'name' from URL query parameters
    greeting = request.args.get('greeting')
    name = request.args.get('name')
    
    if greeting and name:
        return f'{greeting}, {name}'
    else:
        return "Missing parameters", 400  # Return a 400 Bad Request if parameters are missing

if __name__ == '__main__':
    app.run(port=5555, debug=True)

## URL Parameter Handeling


        
