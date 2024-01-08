from flask import Flask , render_template ,request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/first")
def first():
    return render_template('first.html')

@app.route("/second")
def second():
    return render_template('second.html')

@app.route("/third")
def third():
    return render_template('third.html')

@app.route("/fourth")
def fourth():
    return render_template('fourth.html')

@app.route("/success")
def fith():
    return render_template('success.html')


if __name__=="__main__":
    app.run(debug=True)