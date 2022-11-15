"""Example docstring."""

__version__ = "0.1.0"

import typing

import flask

app = flask.Flask(__name__)


@app.route("/hello/")
@app.route("/hello/<string:name>")
def hello_world(name: typing.Optional[str] = None) -> str:
    """Do the welcome to new users."""
    if name is None:
        name = "Bro"
    return flask.render_template("hello.html", name=name)
