# Fix for older setuptools
import re
import os

from setuptools import setup, find_packages


def fpath(name):
    return os.path.join(os.path.dirname(__file__), name)


def read(fname):
    return open(fpath(fname)).read()


def desc():
    info = read('README.rst')
    try:
        return info + '\n\n' + read('doc/changelog.rst')
    except IOError:
        return info


# grep flask_admin/__init__.py since python 3.x cannot import it before using 2to3
file_text = read(fpath('flask_xadmin/__init__.py'))


def grep(attrname):
    pattern = r"{0}\W*=\W*'([^']+)'".format(attrname)
    strval, = re.findall(pattern, file_text)
    return strval


setup(
    name='Flask-xAdmin',
    version=grep('__version__'),
    url='https://github.com/hexo-/flask-xadmin',
    license='MIT',
    author=grep('__author__'),
    author_email=grep('__email__'),
    description='eXtended Flask-Admin',
    long_description=desc(),
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask-Admin',
        'Flask-SQLAlchemy',
        'Flask-Security'
    ],
    tests_require=[
        'nose>=1.0',
        'Flask-Admin',
        'Flask-SQLAlchemy',
        'Flask-Security',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='nose.collector'
)
