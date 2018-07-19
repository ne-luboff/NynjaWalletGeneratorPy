# -*- coding: utf-8 -*-
#
# Project name: NynjaWalletPy
# File name: environment.py
# Created: 2017-07-11
#
# Author: Liubov M. <liubov.mikhailova@gmail.com>

import os

ROOT = os.path.abspath(os.path.dirname(__file__))


env = {
    'debug': True,
    'api_key': '6A8826b1dC1f1B55D4d3EDa121bcB784',
    'api_pass': 'LfFtZvUwSYKkTJDxLiGXoMBrKJEeHXhB',
    'cookie_secret': 'SOjpvZZANGhA0GX7FeHbnPkrQfckxh0g',
    'password_salt': 'mNxFM11by7RDBuEUiyvR59ermxxZq4zZ',
    'daemon': True,
    'ssl': False,
    'port': '8888',
    'logfile': os.path.join(ROOT, 'NynjaWalletPy.log'),
    'pidfile': os.path.join(ROOT, 'pid'),
    'url_prefix': '',
    'site_url': 'http://localhost:8888/',
    'static_url': 'http://localhost:8888/s/',
    'serve_static': True
}