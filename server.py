from flask import Flask, render_template
import webbrowser
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("trainer.html")
webbrowser.open("http://localhost:5000/")

app.run(debug=False)