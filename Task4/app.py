from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')


def plus_service(num1, num2):
    url = 'http://localhost:5001/plus'
    data = {'num1': num1, 'num2': num2}
    response = requests.post(url, json=data)
    result = response.json()['result']
    return result


def minus_service(num1, num2):
    url = 'http://localhost:5002/minus'
    data = {'num1': num1, 'num2': num2}
    response = requests.post(url, json=data)
    result = response.json()['result']
    return result

def multiply_service(num1, num2):
    url = 'http://localhost:5003/multiply'
    data = {'num1': num1, 'num2': num2}
    response = requests.post(url, json=data)
    result = response.json()['result']
    return result

def divide_service(num1, num2):
    url = 'http://localhost:5004/divide'
    data = {'num1': num1, 'num2': num2}
    response = requests.post(url, json=data)
    result = response.json()['result']
    return result

@app.route('/calculate', methods=['POST'])
def calculate():
    expr = request.form['expression'].strip()
    print(expr)
    # Split expression into operands and operators
    operands = []
    operators = []
    for x in expr.split():
        if x.isdigit() or x == "M":
            operands.append(x)
        else:
            operators.append(x)
    
    print(operands, operators)
    # Perform operations using microservices
    for operator in operators:
        print(operands, operators)
        if operator == '+':
            result = plus_service(operands.pop(0),operands.pop(0))
        elif operator == '-':
            result = minus_service(operands.pop(0),operands.pop(0))
        elif operator == '*':
            result = multiply_service(operands.pop(0),operands.pop(0))
        elif operator == '/':
            result = divide_service(operands.pop(0),operands.pop(0))

        operands.insert(0, result)
        

    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
