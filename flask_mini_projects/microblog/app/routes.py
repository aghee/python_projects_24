from flask import render_template,flash,redirect,request,url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user={'username':'Agy'}
    posts=[
        {'author': {'username': 'Kay'},
        'body': 'Oh Happy Day!'},
        {
        'author': {'username': 'Wangwi'},
        'body': 'Don\'t get away with murder movie by Viola Davis was so cool!'
        }
    ]
    return render_template('index.html',user=user,posts=posts)

@app.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {},remember_me ={}'.format(form.username.data,form.remember_me.data))
        return redirect(url_for('index'))

    return render_template('login.html', title='Sign In', form=form)

