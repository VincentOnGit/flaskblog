# -*- coding: utf-8 -*-

import unittest
from app.models import User, Role, Permissions, AnonymousUser
from app import create_app, db


class UserModelTestCase(unittest.TestCase):
	def setUp(self):
		self.app = create_app('testing')
		self.app_context = self.app.app_context()
		self.app_context.push()
		db.create_all()

	def tearDown(self):
		db.session.remove()
		db.drop_all()
		self.app_context.pop()

	def test_password_setter(self):
		u = User(password='cat')
		self.assertTrue(u.password_hash is not None)

	def test_no_password_getter(self):
		u = User(password='cat')
		with self.assertRaises(AttributeError):
			u.password

	def test_password_verification(self):
		u = User(password='cat')
		self.assertTrue(u.verify_password('cat'))
		self.assertFalse(u.verify_password('dog'))

	def test_password_salts_are_random(self):
		u1 = User(password='cat')
		u2 = User(password='cat')
		self.assertTrue(u1.password_hash != u2.password_hash)

	def test_user_confirmed(self):
		u = User(email='123@qq.com', username='william', password='cat')
		token = u.generate_confirmation_token()
		self.assertTrue(u.confirm(token))

	def test_roles_and_permissions(self):
		Role.insert_roles()
		u = User(email='john@example.com', password='cat')
		self.assertTrue(u.can(Permissions.WRITE_ARTICLES))
		self.assertFalse(u.can(Permissions.MODERATE_COMMENTS))

	def test_anonymous_user(self):
		u = AnonymousUser()
		self.assertFalse(u.can(Permissions.FOLLOW))
