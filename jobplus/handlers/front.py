from flask import Blueprint, render_template

front = Blueprint('front', __name__, url_prefix='/')

@front.route('/')
def index():
	return render_template('index.html')

@front.route('/login')
def login():
	pass

@front.route('/logout')
def logout():
	pass

@front.route('/userregister')
def userregister():
	pass

@front.route('/companyregister')
def companyregister():
	pass