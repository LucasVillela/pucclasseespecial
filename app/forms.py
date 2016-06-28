from flask.ext.wtf import Form
from wtforms import TextField, PasswordField,validators
#from wtforms.validators import DataRequired


class LoginForm(Form):

    ra = TextField('Email', [validators.Required()])
    password = PasswordField('Password',[validators.Required()])
