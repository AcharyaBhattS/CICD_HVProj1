from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return ("Introduction to CI/CD Project")


if __name__ == "__main__":
    app.run(debug=True, port=80)