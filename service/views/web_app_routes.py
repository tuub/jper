from flask import render_template
from octopus.lib.webapp import custom_static


def index():
    """
    Default index page

    :return: Flask response for rendered index page
    """
    return render_template("index.html")


def static(filename):
    """
    Serve static content

    :param filename: static file path to be retrieved
    :return: static file content
    """
    return custom_static(filename)

