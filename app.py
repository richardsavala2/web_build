from flask import Flask, render_template

# '__main__'
app = Flask(__name__)


# www.mysite.com/api/
@app.route('/')
def hello_method():
    return render_template('login.html')


if __name__ == '__main__':
    app.run()
