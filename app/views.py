from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app,db,lm,bcrypt
from .models import Aluno
from .forms import LoginForm

@app.route('/')
@app.route('/index')
@login_required
def index():
	return render_template("index.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = LoginForm()
	if form.validate_on_submit():
		aluno = Aluno.query.filter_by(ra = form.ra.data).filter_by(senha = form.password.data).first()
		if aluno:
			login_user(aluno)
			return redirect(url_for('index'))
		flash('Wrong email or password')

	return render_template('login.html', form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@lm.user_loader
def load_user(user_id):
	return Aluno.query.get(user_id)