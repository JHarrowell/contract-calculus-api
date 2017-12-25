from flask import Flask, request
from comparer import comparer

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/')
def hello_world():
    return 'Hello, world xD'


@app.route('/compare', methods=['POST'])
def compare():
    return comparer(request.json)


if __name__ == '__main__':
    app.run(debug=True)
