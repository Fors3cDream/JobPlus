from flask import Blueprint, render_template, redirect, url_for, flash
from jobplus.models import User, db, Job
from jobplus.forms import LoginForm, RegisterForm
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
@login_required
def logout():
	logout_user()
	flash("Log out success!", category="success")
	return redirect(url_for('.index'))

@front.route('userregister')
def userregister():
	form = RegisterForm()
	if form.validate_on_submit():
		form.create_user()
		flash('注册成功，请登录！', 'success')
		return redirect(url_for('.login'))
	return render_template('userregister.html', form=form)


@front.route('companyregister', methods=['GET', 'POST'])
def companyregister():
    form = RegisterForm()
    form.name.label = u'企业名称'
    if form.validate_on_submit():
        company_user = form.create_user()
        company_user.role = User.ROLE_COMPANY
        db.session.add(company_user)
        db.session.commit()
        flash('注册成功，请登录！', 'success')
        return redirect(url_for('.login'))
    return render_template('companyregister.html', form=form)