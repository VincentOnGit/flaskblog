# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required


class NameForm(FlaskForm):
	name = StringField(label='What is your name?', validators=[Required()])
	submit = SubmitField(label='Submit')
