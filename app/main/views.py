# -*- coding: utf-8 -*-

from flask import redirect, url_for, render_template, session
from . import main
from .. import db
from .forms import NameForm
from ..models import User


@main.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')
