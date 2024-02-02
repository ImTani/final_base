from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
import sqlalchemy as sa
from app import db
from app.models import User

class ExampleForm(FlaskForm):
    heading = "Example Form"
    username = StringField('Username', render_kw={'placeholder': 'Enter your username'})
    email = StringField('Email', render_kw={'placeholder': 'Enter your email', 'form_text': 'Enter a valid email address.'})
    bio = TextAreaField('Bio', render_kw={'placeholder': 'Enter your bio'})

class LoginForm(FlaskForm):
    heading = "Sign in"
    username = StringField('Username', validators=[DataRequired()], render_kw={'placeholder': 'Enter your username.'})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={'placeholder': 'Enter your password.'})
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign in')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4,
                                                            max = 16)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6,
                                                            max = 18)])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Submit')

    def validate_username(self, username):
        user = db.session.scalar(sa.select(User).where(
            User.username == username.data))
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = db.session.scalar(sa.select(User).where(
            User.email == email.data))
        if user is not None:
            raise ValidationError('Please use a different email address.')

class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0,
                                                            max = 140)])
    submit = SubmitField('Submit')

class ContactForm(FlaskForm):
    first = StringField('First Name', validators=[DataRequired()])
    last = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    query =  TextAreaField('What can we help you with?', validators=[Length(min=40,
                                                                            max=500)])
    submit = SubmitField('Submit')