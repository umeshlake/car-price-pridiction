from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Default API"


@app.route('prediction', methods =['GET','POST'])
def prediction():
    return "result"


if __name__ == "__main__:
    app.run(debug=True)