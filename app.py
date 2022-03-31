from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SECRET_KEY'] = "shhh it's a secret"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Register(db.Model):
    name = db.Column(db.String(30), nullable=False, primary_key=True)

class RegisterForm(FlaskForm):
    name = StringField('Name')
    submit = SubmitField('Submit')

db.create_all()

@app.route('/', methods=["GET","POST"])
def home():
    form = RegisterForm()
    if form.validate_on_submit():
        person = Register(name=form.name.data)
        db.session.add(person)
        db.session.commit()
    registrees = Register.query.all()
    return render_template("home.html", registrees=registrees, form=form)

'''The Tutorial's unit test script currently doesn't Create functionality for the application. 
Write a unit test that tests this functionality by adding a new registree to the database. Doing so should provide you with 100% coverage.

You will need to make a `POST` request to the Flask application as described in the Making HTTP Requests section of this module.'''

if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')