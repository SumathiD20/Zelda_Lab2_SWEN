from flask import Flask

app = Flask(__name__)

@app.route("/")
def Hello():
    return "Hello, This is combat.py file!"

if __name__ == 'main':
    app.run()