from flask import Flask

#'__main__'
app = Flask(__name__)

#www.mysite.com/api/
@app.route('/')
def hello_method():
    return 'Hello, world!'

if __name__ == '__main__':
    app.run()
