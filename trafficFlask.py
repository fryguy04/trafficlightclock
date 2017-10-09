#!flask/bin/python
from flask import Flask, jsonify, abort, request, make_response, url_for
import time
import traffic

t = traffic()

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/time', methods=['GET'])
def get_time():
    return time.ctime()

@app.route('/traffic', methods=['GET'])
def get_color():
    return t.status()

@app.route('/traffic/<color>', methods=['GET'])
def set_color(color):
    result = t.set_light(color) # Todo have traffic class return Color or Error
    return color



if __name__ == '__main__':
    app = Flask(__name__, static_url_path="")
    app.run(debug=True)