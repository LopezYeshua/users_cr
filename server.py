from flask import Flask, render_template, redirect, request
from user import User
app = Flask(__name__)

@app.route('/')
def index():
    users = User.get_all()
    print(users)
    return render_template('index.html', users = users)

@app.route('/create_user', methods=['POST'])
def add():
    data = {
        "fname": request.form["fname"],
        "lname": request.form['lname'],
        "email": request.form['email']
    }

    User.save(data)

    return redirect('/results')

@app.route('/results')
def results():
    users = User.get_all()
    return render_template('results.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)