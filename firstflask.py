from flask import Flask,render_template,request


app = Flask(__name__)
age=1000
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template("about.html",x=age)


if __name__ == "__main__":
    app.run()