# -*- coding: utf-8 -*-

from flask import redirect, url_for, render_template, session
from . import main
from .. import db
from .forms import NameForm
from ..models import User


@main.route('/', methods=['GET', 'POST'])
def index():
	form = NameForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.name.data).first()
		if user is None:
			user = User(username=form.name.data)
			db.session.add(user)
			session['known'] = False
		else:
			session['known'] = True
		session['name'] = form.name.data
		form.name.data = ''
		return redirect(url_for('.index'))
	return render_template('index.html', form=form, name=session.get('name'), known=session.get('known', False))
