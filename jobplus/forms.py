from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError, IntegerField, TextAreaField
from wtforms.validators import Length, Email, EqualTo, Required
from jobplus.models import db, User

class LoginForm(FlaskForm):
	email = StringField('email', validators=[Required(), Email()])
	password = PasswordField('password', validators=[Required(), Length(6, 24)])
	remember_me = BooleanField('Remember me')
	submit = SubmitField('submit')

	def validate_email(self, field):
		if field.data and not User.query.filter_by(email=field.data).first():
			raise ValidationError('User not exists!')

	def validate_password(self, field):
		user = User.query.filter_by(email=self.email.data).first()
		if user and not user.check_password(field.data):
			raise ValidationError('Password Wrong!')