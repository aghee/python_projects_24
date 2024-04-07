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

    def __init__(self,orig_username,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.orig_username=orig_username
    
    # def validate_username(self,username):
    #     if username.data !=self.orig_username:
    #         user=db.session.scalar(sa.select(User).where(User.username==username.data))
    #         if user is not None:
    #             raise ValidationError('You can only update about me details relating to yourself,not for another user! ')
    #         elif user is None:
    #             raise ValidationError('User does not exist! Confirm that the username is that of currently logged in user')
        
        
        