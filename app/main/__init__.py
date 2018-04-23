# -*- coding: utf-8 -*-


from flask import Blueprint
from ..models import Permissions

main = Blueprint('main', __name__)

@main.app_context_processor
def inject_permissions():
	return dict(Permission=Permissions)

from . import views
from . import errors
