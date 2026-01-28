from flask import Flask, render_template
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("trainer.html")

app.run(debug=False)