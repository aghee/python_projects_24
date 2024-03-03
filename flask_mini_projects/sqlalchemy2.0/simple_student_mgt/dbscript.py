from app import Student, app, db

with app.app_context():
  db.create_all()

student_A= Student(
  fname='Jon',
  lname='Kay',
  email='jonkay@yahoo.com',
  age=34,
  bio='Physics major'
)