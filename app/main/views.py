# -*- coding: utf-8 -*-

from flask import redirect, url_for, render_template
from . import main
from ..decorators import admin_required, permission_required
from ..models import Permissions
from flask_login import login_required


@main.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')


@main.route('/admin/')
@login_required
@admin_required
def for_admins_only():
	return "For administrators!"


@main.route('/moderator/')
@login_required
@permission_required(Permissions.MODERATE_COMMENTS)
def for_moderators_only():
	return "For comment moderators!"
