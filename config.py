# -*- coding: utf-8 -*-

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or '\xf3A\xe1\xe7\x05>\x97\xdd\x8e\xb9\xaa(\xe4\xb4\t\xa9\x14\n"j\x89G1|'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	FLASK_BLOG_SUBJECT_PREFIX = '[FlaskBlog]'
	FLASK_BLOG_SENDER = 'FlaskBlog Admin <flask.blog@example.com>'
	FLASK_BLOG_ADMIN = os.environ.get('FLASK_ADMIN')
	SQLALCHEMY_TRACK_MODIFICATIONS = True

	@staticmethod
	def init_app(app):
		pass


class DevelopmentConfig(Config):
	DEBUG = True
	MAIL_SERVER = 'smtp.163.com'
	MAIL_PORT = '465'
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
	MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
	SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
	'development': DevelopmentConfig,
	'testing': TestingConfig,
	'production': ProductionConfig,
	'default': DevelopmentConfig
}
