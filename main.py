# main.py
from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
import os

# Setup environment variables before app initialization
SECRET_KEY_ENV = os.environ.get('MYSECRETKEY', 'default-secret-key')
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY_ENV

class MyLoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()], render_kw={"size": "30"})  # Email field with size attribute
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=4, max=30, message=None)], render_kw={"size": "30"})  # Password field with size attribute
    submit = SubmitField(label="Log In")

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = MyLoginForm()
    if form.validate_on_submit():
        # Place your authentication logic here
        return redirect(url_for('success'))
    else:
        # Form is not valid, print or log the errors
        print(form.errors)
    return render_template('login.html', form=form)

@app.route('/success')
def success():
    return "Login successful!"

if __name__ == '__main__':
    app.run(debug=True)
