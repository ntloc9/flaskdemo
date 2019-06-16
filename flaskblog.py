from flask import Flask, render_template, url_for, flash, redirect
from form import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'd07ffc88bd84d2d1d3e5db13e92a1ed7'

posts=[
	{
	'author': 'Loc Nguyen',
	'title': 'Blog 1',
	'content': 'Content 1',
	'date_posted': 'April 21, 2019'
	},
	{
	'author': 'Loc Nguyen 1',
	'title': 'Blog 2',
	'content': 'Content 2',
	'date_posted': 'April 22, 2019'
	},
	{
	'author': 'Loc Nguyen 2',
	'title': 'Blog 3',
	'content': 'Content 3',
	'date_posted': 'April 23, 2019'
	},
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('Home.html', posts = posts)

@app.route("/about")
def about():
    return render_template('About.html', title = 'About')

@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit:
		flash(f'Account created for {form.username.data}!', 'success')
	return render_template('register.html', title = 'Register', form = form)

@app.route("/login")
def login():
	form = LoginForm()
	return render_template('login.html', title = 'Login', form = form)




if __name__== '__main__':
	app.run(debug=True)