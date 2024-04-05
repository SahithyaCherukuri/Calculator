from flask import Flask, jsonify, request
import requests

app = Flask(__name__)


@app.route('/minus', methods=['POST'])
def plus():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    filename = '/my-volume/result.txt'
    if num1 == "M":
        try:
            with open(filename, 'r') as f:
                num1 = int(f.read().strip())
        except FileNotFoundError:
            print("in expect")
            num1 = 0
    if num2 == "M":
        try:
            with open(filename, 'r') as f:
                num2 = int(f.read().strip())
        except FileNotFoundError:
            print("in expect")
            num2 = 0
    result = int(num1) - int(num2)
    with open(filename, 'w') as f:
            f.write(str(result))
    return jsonify({'result': result})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)