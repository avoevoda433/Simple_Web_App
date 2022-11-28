from flask import Flask, render_template, redirect, url_for
from converter.converter import converter
from params_validation import params, ValidationError

app = Flask(__name__)


@app.route('/')
def index():
    """
    Renders template for the main html page
    """
    return render_template('result.html')


@app.route('/warning/<warning_msg>')
@app.errorhandler(ValidationError)
def warning(error):
    """
        Renders template for the main html page with warning message
        """
    return render_template('result.html', warning_msg=error), 200


@app.route('/c2f/<value>')
def c2f(value):
    """
    Renders template for the c2f convert endpoint
    :param value: conversion result
    """
    return render_template('result.html', value=value), 200


@app.route('/f2c/<value>')
def f2c(value):
    """
    Renders template for the f2c convert endpoint
    :param value: conversion result.
    """
    return render_template('result.html', value=value), 200


@app.route('/convert/', methods=['GET'])
@params
def convert_mode(direction, input_value):
    """
    Gets parameters and redirects to endpoint
    :return: Page for a convert endpoint
    """
    return redirect(url_for(direction, value=converter.get(direction)(float(input_value))))


@app.errorhandler(400)
def incorrect_input(error):
    """
    Renders template for 400 code error page
    """
    return render_template('error.html', error=error, code=400), 400


@app.errorhandler(404)
def not_found(error):
    """
    Renders template for 404 code error page
    """
    return render_template('error.html', error=error, code=404), 404


@app.errorhandler(500)
def server_error(error):
    """
    Renders template for 500 code error page
    """
    return render_template('error.html', error=error, code=500), 500


if __name__ == '__main__':
    app.run(debug=False)
