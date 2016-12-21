Flask-xAdmin
============

Flask-xAdmin is an ***extended*** Flask-Admin extension for admin apps, standing on the shoulders of giants: Flask, SQLAlchemy, Flask-Security and Flask-Admin. 

Introduction
------------

Flask-xAdmin is a ***extended*** *life batteries-included*, simple-to-use `Flask <http://flask.pocoo.org/>`_ extension that lets you
add admin interfaces to Flask applications. 

The goal of Flask-xAdmin is to give additional flexibility to Flask-Admin apps and to make admin developer job easier.  

*Extended life* means that apps built with Flask-xAdmin are smaller and more resistant to database model changes, thus providing admin app extended lifetime & flexibility (between changes).

Flask-xAdmin specific features are tested on  `SQLAlchemy <http://www.sqlalchemy.org/>`_. 

Flask-xAdmin is a new project. 

Examples
--------
Examples are included in the */examples* folder. Please feel free to add your own examples, or improve
on some of the existing ones, and then submit them via GitHub as a *pull-request*.

*simple.py*

1. start simple.py
2. open http://127.0.0.1:8001/xadmin/note/
3. enter email: admin@example.com, password: password
4. follow at User link in table
4. try edit (click at user icon to enter edit mode)
5. logout

User vadmin@example.com/password does not have edit mode role.
You can try to login as vadmin@example.com to see difference.


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
