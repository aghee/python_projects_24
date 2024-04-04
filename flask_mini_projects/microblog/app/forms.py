from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,TextAreaField
from wtforms.validators import DataRequired,Email,EqualTo,ValidationError,Length
from app import db
import sqlalchemy as sa
from app.models import User

class LoginForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired()])
    pwad=PasswordField('Password',validators=[DataRequired()])
    remember_me=BooleanField('Remember me')
    submit=SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired()])
    email=StringField('Email',validators=[DataRequired(),Email()])
    passwd=PasswordField('Password',validators=[DataRequired()])
    pass1=PasswordField('Repeat Password',validators=[DataRequired(),EqualTo('passwd')])
    submit=SubmitField('Register')

    def validate_username(self,username):
        user=db.session.scalar(sa.select(User).where(User.username==username.data))
        if user is not None:
            raise ValidationError('Username exists!Enter a different one.')
    
    def validate_email(self,email):
        user=db.session.scalar(sa.select(User).where(User.email==email.data))
        if user is not None:
            raise ValidationError('Email exists!Enter a different one')
        
class EditProfileForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired()])
    about_me=TextAreaField('About me',validators=[Length(min=10,max=150)])
    submit=SubmitField('Submit')
