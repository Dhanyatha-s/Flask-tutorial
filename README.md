# Flask Basic Tutorial  
### Table of Contents  
1. Introduction  
2. Installation  
3. Creating a Basic Flask Application  
4. Running the Application  
5. Routing in Flask  

### Introduction  
Flask is a lightweight and flexible Python web framework used to build web applications. It’s minimal and comes with built-in development tools, making it ideal for small to medium-sized applications.  

### Installation  
#### Step 1: Install Python  
Ensure Python is installed. You can check this by running:  
```
python --version

```
### Creating a Basic Flask Application
#### 1.Create a project folder and navigate to it:
```
mkdir flask_app
cd flask_app
```
#### 2.Create the main Flask file: Create a Python file named app.py
```
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)

```
. Flask(__name__): Initializes the app.  
. @app.route('/'): Defines the home route (default endpoint).  
. app.run(debug=True): Runs the app in development mode.  
### Running the Application  
Open a terminal/command prompt and navigate to your project folder (flask_app).  

Run the Flask app with:
```
python app.py
or
flask run
```


