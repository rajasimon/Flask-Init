.. Flask-Init documentation master file, created by
   sphinx-quickstart on Mon Jul 24 16:44:32 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Flask-Init!
======================================

**Flask-Init** extension provides support for creating Flask application with ease. 
This includes creating boilerplate code from hello world application to complex blueprint apps in Flask.

Installing Flask-Init
---------------------

Install with **pip** and **easy_install**

.. code-block:: sh

    pip install Flask-Init

Usage
-----

**Flask-Init** works in a similar way to Flask itself. Comes with default optional 
commands that can able to create Flask application for you.

.. code-block:: sh

    $ flask init

Options
-------

.. code-block:: sh

  --simple

Very simple flask application. Contains only one url endpoint that prints `Hello World`

.. code-block:: sh

  --single-module

This is great for quick projects (like the ones used for tutorials), 
where you just need to serve a few routes and you’ve got less than a few hundred lines of application code.