# -*- coding: utf-8 -*-

from functools import wraps
from flask_login import current_user
from flask import abort
from models import Permissions


def permission_required(permission):
	def decorator(f):
		@wraps(f)
		def decorated_function(*args, **kwargs):
			if not current_user.can(permission):
				abort(403)
			return f(*args, **kwargs)
		return decorated_function
	return decorator


def admin_required(f):
	return permission_required(Permissions.ADMINISTER)(f)
