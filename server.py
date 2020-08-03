from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return '<h1>Why so easy</h1>'


@app.route("/another")
def show():
    return '<h1>Yo</h1>'

@app.route("/user/<username>")
def shows(username):
    return f"Hi {username[0:3]}"


if __name__ == '__main__':
    app.run()