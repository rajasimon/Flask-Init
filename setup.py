"""
Flask-Init

Easy way to create Flask Web application.
"""
from setuptools import setup
from flask_init import __version__

setup(
    name="Flask-Init",
    version=__version__,
    url='https://github.com/rajasimon/flask-init',
    license='See License',
    author='Raja Simon',
    author_email='rajasimon@icloud.com',
    description='Easy way to create Flask Web application',
    packages=['flask_init'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    entry_points={
        'flask.commands': [
            'init=flask_init.commands:cli'
        ]
    },
    install_requires=[
        'Flask',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
