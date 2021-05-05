from flask import Flask, render_template

app = Flask(__name__)

@app.route('/ben')
def ben():
    return render_template('ben.html')

@app.route('/harry')
def harry():
    return render_template('harry.html')

@app.route('/show_b_names')
def show_b_names():
    names = ["ben", "harry", "bob", "jay", "matt", "bill"]
    return render_template('names.html', names = names)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')