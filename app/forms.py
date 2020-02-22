from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectMultipleField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    location = SelectMultipleField(u'Server Location', choices=[
                                   ('east', 'New Jersey'), ('west', 'Los Angles'), ('mid', 'Texas')])
    submit = SubmitField('Sign In')
