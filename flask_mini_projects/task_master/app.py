from flask import Flask,render_template,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from database import db
from datetime import datetime
from models import ToDo

app=Flask(__name__)

#CONNECTING TO DB TO BE SORTED!!!
db_name='test_db'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+ db_name

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db.init_app(app)


# db=SQLAlchemy(app)
def createdb():
    with app.app_context():
        db.create_all()
    # print(current_app.name)

@app.route('/', methods=['POST','GET'])
def index():
    if request.method=='POST':
        task_content=request.form['content']
        new_task=ToDo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task.'
    else:
        tasks=ToDo.query.order_by(ToDo.date_created).all()
        return render_template('index.html',tasks=tasks)

if __name__=='__main__':
    app.run(debug=True)
    createdb()