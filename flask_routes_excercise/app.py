from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return 'This is the home page'

@app.route('/square/<int:number>')
def about(number):
    return f'The square of {number} is {number**2}'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')