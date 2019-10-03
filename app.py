"""
Tiny hello world service example
"""

import os
from flask import Flask, request

APP = Flask(__name__)  # Standard Flask app


@APP.route("/", defaults={"path": "root"})
@APP.route("/<path>")
def hello(path):
    """
    Hello world on root path
    """
    print(request.method, request.path, request.headers, request.data)
    return "OK"


if __name__ == "__main__":
    APP.run(host='0.0.0.0', port=os.environ.get('listenport', 8080))
