from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<center><h1>Hello, World Flask deployment on azure!</h1></center>'

if __name__ == '__main__':
    app.run()
