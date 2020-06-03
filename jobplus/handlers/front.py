from flask import Blueprint, render_template, redirect, url_for, flash
from jobplus.models import User, db, Job
from jobplus.forms import LoginForm
from flask_login import login_user, logout_user, login_required

front = Blueprint('front', __name__, url_prefix="/") # url_prefix="/" if add url_prefix please use route('login') to register

@front.route('/')
def index():
	return render_template('index.html')

@front.route('login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		login_user(user, form.remember_me.data)
		next = 'user.profile'
		if user.is_admin:
			next = 'admin.index'
		elif user.is_company:
			next = 'company.profile'
		return redirect(url_for(next))
	return render_template('login.html', form=form)

@front.route('logout')
def logout():
	pass

@front.route('userregister')
def userregister():
	pass

@front.route('companyregister')
def companyregister():
	pass