# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, ValidationError
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from ..models import User


class LoginForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember_me = BooleanField('Keep me logged in')
	submit = SubmitField('Log In')


class RegistrationForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
	username = StringField('Username', validators=[DataRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 'Username must have only letters, numbers, dots or underscores.')])
	password = PasswordField('Password', validators=[DataRequired(), EqualTo('password2', message='Passwords must match.')])
	password2 = PasswordField('Confirm Password', validators=[DataRequired()])
	submit = SubmitField('Register')

	def validate_email(self, field):
		if User.query.filter_by(email=field.data).first():
			raise ValidationError('Email already registered.')

	def validate_username(self, field):
		if User.query.filter_by(username=field.data).first():
			raise ValidationError('Username already in user.')


class ChangePasswordForm(FlaskForm):
	old_pwd = PasswordField('Old Password', validators=[DataRequired()])
	new_pwd = PasswordField('New Password', validators=[DataRequired(), EqualTo('new_pwd2', message='Passwords must match.')])
	new_pwd2 = PasswordField('Confirm New Password', validators=[DataRequired()])
	submit = SubmitField('Confirm')
