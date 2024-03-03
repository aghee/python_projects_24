from flask import Flask

app=Flask(__name__)

@app.route('/')
def greeting():
    return '<p>Hello Agnes!</p>'

if __name__=='__main__':
    app.run(debug=True)