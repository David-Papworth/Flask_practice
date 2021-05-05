from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DateField, DecimalField, SelectField
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

class BasicForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    age = IntegerField('Age')
    date_of_birth = DateField('Date of Birth')
    favourite_dec_number = DecimalField('Favourite Decimal Number', places=3)
    favourite_colour = SelectField('Favourite Colour', choices=[])
    submit = SubmitField('Add Name')

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def register():
    error = ""
    form = BasicForm()

    form.favourite_colour.choices = ['Blue', 'Green', 'Red']

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        age = form.age.data
        date_of_birth = form.date_of_birth.data
        favourite_dec_number = form.favourite_dec_number.data
        favourite_colour = form.favourite_colour.data

        if len(first_name) == 0 or len(last_name) == 0:
            error = "Please supply both first and last name"
        elif age < 0:
            error = 'Please add a valid age'
        else:
            return f'Thank you {first_name} {last_name}'

    return render_template('home.html', form=form, message=error)

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0')