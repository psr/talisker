#!/usr/bin/env python
#
# Note: this file is autogenerated from setup.cfg for older setuptools
#
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

attrs = {
    "author": "Simon Davy",
    "author_email": "simon.davy@canonical.com",
    "classifiers": [
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware",
        "Topic :: System :: Logging",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython"
    ],
    "description": "A common WSGI stack",
    "entry_points": {
        "console_scripts": [
            "talisker=talisker:run_gunicorn",
            "talisker.run=talisker:run",
            "talisker.gunicorn=talisker:run_gunicorn",
            "talisker.gunicorn.eventlet=talisker:run_gunicorn_eventlet",
            "talisker.gunicorn.gevent=talisker:run_gunicorn_gevent",
            "talisker.celery=talisker:run_celery"
        ]
    },
    "extras_require": {
        "celery": [
            "celery>=3.1.13.0,<5.0"
        ],
        "dev": [
            "logging_tree",
            "pygments"
        ],
        "django": [
            "django>=1.8,<1.11"
        ],
        "flask": [
            "flask>=0.11,<0.13",
            "blinker>=1.4,<2.0"
        ],
        "pg": [
            "sqlparse>=0.2",
            "psycopg2>=2.4.5,<3.0"
        ],
        "prometheus": [
            "prometheus-client>=0.0.17,<0.1"
        ]
    },
    "include_package_data": True,
    "install_requires": [
        "gunicorn>=19.5.0,<20.0",
        "Werkzeug>=0.11.5,<0.13",
        "statsd>=3.2.1,<4.0",
        "requests>=2.10.0,<3.0",
        "raven>=5.27.0,<7.0",
        "future>=0.15.2,<0.17",
        "ipaddress>=1.0.16,<2.0;python_version<\"3.3\""
    ],
    "keywords": [
        "talisker"
    ],
    "license": "GPL3",
    "name": "talisker",
    "package_data": {
        "talisker": [
            "logstash/*"
        ]
    },
    "package_dir": {
        "talisker": "talisker"
    },
    "packages": [
        "talisker"
    ],
    "test_suite": "tests",
    "url": "https://github.com/canonical-ols/talisker",
    "version": "0.9.5",
    "zip_safe": False
}

attrs['long_description'] = open('README.rst').read()
setup(**attrs)
