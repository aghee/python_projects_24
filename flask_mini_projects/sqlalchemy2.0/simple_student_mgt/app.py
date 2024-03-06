import os

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

#db connection established
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#db object creation
db = SQLAlchemy(app)


class Student(db.Model):
  id=db.Column(db.Integer,primary_key=True)
  fname=db.Column(db.String(20),nullable=False)
  lname=db.Column(db.String(30),nullable=False)
  email=db.Column(db.String(99),unique=True,nullable=False)
  age=db.Column(db.Integer)
  created_at=db.Column(db.DateTime(timezone=True),server_default=func.now())
  bio=db.Column(db.Text)

  def __repr__(self):
    return f'<Student {self.fname}>'

@app.route('/view_data')  
def view():
  students=Student.query.all()
  return render_template('view.html',students=students)

if __name__=='__main__':
  app.run(debug=True,host='0.0.0.0',port=5000)