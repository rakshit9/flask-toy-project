from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import (StringField,
                     IntegerField,
                     PasswordField,
                     SubmitField,
                     BooleanField,
                     SelectField,
                     TextAreaField)
from wtforms.validators import (DataRequired,
                                Length, Email,
                                EqualTo,
                                ValidationError)
from fiverr.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField(
        'Confirm Password',
        validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a\
                 different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a\
                 different one.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture',
                        validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a\
                     different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a\
                     different one.')


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    post_image = FileField('Update New post',
                           validators=[FileAllowed(['jpg', 'png'])])
    content = TextAreaField('Content', validators=[DataRequired()])
    # category = StringField('Catogory', validators=[DataRequired()])
    category = SelectField(choices=[
        ('Select', 'Select'),
        ("General", "General"),
        ("Graphics & Design", "Graphics & Design"),
        ("Digital Marketing", "Digital Marketing"),
        ("Writing & Translation", "Writing & Translation"),
        ("Video & Animation", "Videom & Animation"),
        ("Music & Audio", "Music & Audio"),
        ("Programming & Tech", "Programming & Tech"),
        ("Business", "Business")])
    price = IntegerField('Price', validators=[DataRequired()])
    submit = SubmitField('Post')
