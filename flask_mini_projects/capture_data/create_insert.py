#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask app
app=Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy database
db = SQLAlchemy(app)

# Create the EmployeeDetails model
class EmployeeDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(20), nullable=False)
    midname = db.Column(db.String(20))
    lname = db.Column(db.String(20), nullable=False)
    nat_id_no = db.Column(db.Integer, unique=True, nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    username = db.Column(db.String(40), unique=True, nullable=False)

    def __init__(self, fname, lname, nat_id_no, email, username):
        self.fname = fname
        self.lname = lname
        self.nat_id_no = nat_id_no
        self.email = email

        user_exists=EmployeeDetails.query.filter_by(username=username)
        if user_exists:
            print('Username already exists!')
        else:
            self.username = username

    def __repr__(self):
        return f'{self.email}'

# Define a route to display the data
@app.route('/display')
def display():
    with app.app_context():
        fake_users = EmployeeDetails.query.all()
    return render_template('index.html', fake_users=fake_users)

if __name__ == '__main__':
    with app.app_context():
        # Create the database tables
        db.create_all()

        # Add data to the database
        obj1 = EmployeeDetails('Trisha', 'Kims', 90907856, 'trishakims@yahoo.com', 'trishan')
        obj2 = EmployeeDetails('Kimo', 'Lwe', 87121314, 'kimolwe@gmail.com', 'kimo')

        # Add the objects to the session and commit      
        db.session.add(obj1)
        db.session.add(obj2)
        db.session.commit()

    # Run the Flask app
    app.run(debug=True)

