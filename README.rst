**Currently only as placeholder (because a base package jtypes.jvm is still in development)**

jtypes.jpype
============

A Python to Java bridge.

Overview
========

  | **jtypes.jpype** is a bridge between Python and Java, allowing these to intercommunicate.
  | It is an effort to allow Python programs full access to Java class libraries.

  `PyPI record <https://pypi.python.org/pypi/jtypes.jpype>`__.

  | **jtypes.jpype** is a lightweight Python package, based on the *ctypes* or *cffi* library.
  | It is an almost fully compliant implementation of Steve Menard's **JPype** package
    by reimplementing whole its functionality in a clean Python instead of C/C++.

About JPype:
------------

Borrowed from the `original website <http://jpype.readthedocs.org>`__:

  | **JPype** is an effort to allow python programs full access to java class libraries.
  | This is achieved not through re-implementing Python, as Jython/JPython has done,
    but rather through interfacing at the native level in both virtual machines.
  |
  | Eventually, it should be possible to replace Java with python in many, though
  | not all, situations. JSP, Servlets, RMI servers and IDE plugins are good candidates.

Known Bugs/Limitations
----------------------

- Java classes outside of a package (in the ``<default>``) cannot be imported.
- Because of lack of JVM support, you cannot shutdown the JVM and then restart it.
- | Some methods rely on the "current" class/caller.
  | Since calls coming directly from python code do not have a current class,
    these methods do not work.
  | The User Manual lists all the known methods like that.

Requirements
============

- Either the Sun/Oracle JRE/JDK or OpenJDK.

Installation
============

Prerequisites:

+ Python 2.7 or higher or 3.4 or higher

  * http://www.python.org/
  * 2.7 and 3.6 are primary test environments.

+ pip and setuptools

  * http://pypi.python.org/pypi/pip
  * http://pypi.python.org/pypi/setuptools

To install run::

    python -m pip install --upgrade jtypes.jpype

To ensure everything is running correctly you can run the tests using::

    python -m jt.jpype.tests

Development
===========

Visit `development page <https://github.com/karpierz/jtypes.jpype>`__

Installation from sources:

Clone the `sources <https://github.com/karpierz/jtypes.jpype>`__ and run::

    python -m pip install ./jtypes.jpype

or on development mode::

    python -m pip install --editable ./jtypes.jpype

Prerequisites:

+ Development is strictly based on *tox*. To install it run::

    python -m pip install tox

License
=======

  | Copyright 2013-2018 Adam Karpierz
  |
  | Licensed under the Apache License, Version 2.0
  | http://www.apache.org/licenses/LICENSE-2.0
  | Please refer to the accompanying LICENSE file.

Authors
=======

* Adam Karpierz <adam@karpierz.net>
