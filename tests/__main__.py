# Copyright 2013-2018 Adam Karpierz
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

from __future__ import absolute_import, print_function

import unittest
import sys
import os
import logging

from . import test_dir


def test_suite(names=None, omit=("convtest", "jarray_fixes")):

    from .jpypetest import __name__ as pkg_name
    from .jpypetest import __path__ as pkg_path
    import unittest
    import pkgutil
    if names is None:
        names = [name for _, name, _ in pkgutil.iter_modules(pkg_path)
                 if name != "__main__" and name not in omit]
    names = [".".join((pkg_name, name)) for name in names]
    tests = unittest.defaultTestLoader.loadTestsFromNames(names)
    return tests


def runTest():

    import jt.jpype as jpype
    jvm_path = jpype.getDefaultJVMPath()

    print("Running testsuite using JVM:", jvm_path, "\n", file=sys.stderr)

    try:
        tests = test_suite(sys.argv[1:] or None)
        result = unittest.TextTestRunner(verbosity=2).run(tests)
    finally:
        if jpype.isJVMStarted():
            jpype.shutdownJVM()

    sys.exit(0 if result.wasSuccessful() else 1)


def main():

    # logging.basicConfig(level=logging.INFO)  # <AK> commented
    # logging.basicConfig(level=logging.DEBUG)
    runTest()


main()
