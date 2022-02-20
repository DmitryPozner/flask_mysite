# -*- coding: utf-8 -*-
from flask import Flask, render_template

application = Flask(__name__)


@application.route("/")
def root():
    return render_template("index.html")


if __name__ == "__main__":
    application.debug = True
    application.run(host='0.0.0.0', port = 80)
    
