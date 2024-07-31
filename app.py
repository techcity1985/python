from flask import Flask, render_template, request

app = Flask(__name__)

# Define functions for each operation
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def modulus(x, y):
    return x % y

def exponentiate(x, y):
    return x ** y

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operation = request.form['operation']
    
    if operation == 'add':
        result = add(num1, num2)
    elif operation == 'subtract':
        result = subtract(num1, num2)
    elif operation == 'multiply':
        result = multiply(num1, num2)
    elif operation == 'divide':
        result = divide(num1, num2)
    elif operation == 'modulus':
        result = modulus(num1, num2)
    elif operation == 'exponentiate':
        result = exponentiate(num1, num2)
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
