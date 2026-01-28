from flask import Flask, render_template
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__, template_folder="../templates")

@app.route("/")
def hello():
    return render_template("trainer.html")

#app.run(debug=False)