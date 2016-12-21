Flask-xAdmin
============

Flask-xAdmin is an *extended* Flask-Admin extension (TODO) for admin apps, standing on the shoulders of giants: Flask, SQLAlchemy, Flask-Security and Flask-Admin. 

Introduction
------------

Flask-xAdmin is a *extended life batteries-included*, simple-to-use `Flask <http://flask.pocoo.org/>`_ extension that lets you
add admin interfaces to Flask applications. 

The goal of Flask-xAdmin is to give additional flexibility to Flask-Admin apps and to make admin developer job easier.  

*Extended life* means that apps built with Flask-xAdmin are smaller and more resistant to database model changes, thus providing admin app extended lifetime & flexibility (between changes).

Flask-xAdmin specific features are tested on  `SQLAlchemy <http://www.sqlalchemy.org/>`_. 

Flask-xAdmin is a new project. 

Examples
--------
Several usage examples are included in the */examples* folder. Please feel free to add your own examples, or improve
on some of the existing ones, and then submit them via GitHub as a *pull-request*.

Documentation (in progress)
---------------------------
Flask-xAdmin documentation will be published at `https://flask-xadmin.readthedocs.io/en/latest/ <https://flask-xadmin.readthedocs.io/en/latest/>`_.

The docs are auto-generated from the *.rst* files in the */doc* folder. So if you come across any errors, or
if you think of anything else that should be included, then please make the changes and submit them as a *pull-request*.

To build the docs in your local environment, from the project directory::

    pip install -r requirements-dev.txt
    sudo make html

And if you want to preview any *.rst* snippets that you may want to contribute, go to `http://rst.ninjs.org/ <http://rst.ninjs.org/>`_.

Installation
------------
To install Flask-xAdmin, simply::

    pip install flask-xadmin

Or alternatively, you can download the repository and install manually by doing::

    git clone git@github.com:flask-xadmin/flask-xadmin.git
    cd flask-xadmin
    python setup.py install

Tests (in progress)
-------------------
Test are run with *nose*. If you are not familiar with this package you can get some more info from `their website <https://nose.readthedocs.io/>`_.

To run the tests, from the project directory, simply::

    pip install -r requirements-dev.txt
    nosetests

You should see output similar to::

    .............................................
    ----------------------------------------------------------------------
    Ran 102 tests in 13.132s

    OK

Notes
-----
This document is created from Flask-Admin/README.rst 

Special thanks to Serge S. Koval, author of Flask-Admin and contributors.
