# -*- coding: utf-8 -*-

from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required


class NameForm(Form):
	name = StringField(label='What is your name?', validators=[Required()])
	submit = SubmitField(label='Submit')
