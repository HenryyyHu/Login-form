from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Initialize an empty user database (for demonstration purposes).
database = {}

@app.route('/')
def hello_world():
    return render_template("login.html")

@app.route('/form_login', methods=['POST', 'GET'])
def login():
    name1 = request.form['username']
    pwd = request.form['password']
    if name1 not in database:
        return render_template('login.html', info='Invalid User')
    else:
        if database[name1] != pwd:
            return render_template('login.html', info='Invalid Password')
        else:
            return render_template('home.html', name=name1)

# New route and view function for the signup page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the username already exists
        if username in database:
            return render_template('signup.html', info='Username already exists')

        # Store the new user in the database (for demonstration purposes)
        database[username] = password

        # Redirect to the login page after successful registration
        return redirect(url_for('hello_world'))

    return render_template('signup.html')

if __name__ == '__main__':
    app.run()
