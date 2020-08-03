from flask import Flask, render_template
app = Flask(__name__)

signed_in = False
@app.route("/")
def index():
    return render_template('index.html',signed_in=signed_in)

@app.route("/contact")
def contact():
    return render_template('contact.html',signed_in=signed_in)

@app.route("/hiuser/<name>")
def hiuser(name):
    name = name.upper()
    return render_template('index.html',name=name)


@app.route("/another")
def show():
    return '<h1>Yo</h1>'

@app.route("/user/<username>")
def shows(username):
    return f"Hi {username[0:3]}"


if __name__ == '__main__':
    app.run(debug=True)