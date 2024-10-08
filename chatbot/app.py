from flask import Flask, render_template

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()
