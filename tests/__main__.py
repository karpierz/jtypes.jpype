# Copyright 2013-2018 Adam Karpierz
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

from __future__ import absolute_import, print_function

import unittest
import sys
import os
import importlib
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


def main():

    sys.modules["jpype"]            = importlib.import_module("jt.jpype")
    sys.modules["jpypex"]           = importlib.import_module("jt.jpypex")
    sys.modules["jpype.awt"]        = importlib.import_module("jt.jpype.awt")
    sys.modules["jpype.imports"]    = importlib.import_module("jt.jpype.imports")
    sys.modules["jpype.JClassUtil"] = importlib.import_module("jt.jpype.JClassUtil")
    sys.modules["jpype.nio"]        = importlib.import_module("jt.jpype.nio")
    sys.modules["jpype.reflect"]    = importlib.import_module("jt.jpype.reflect")
    sys.modules["jpype._jboxed"]    = importlib.import_module("jt.jpype._jboxed")
    sys.modules["jpype._jwrapper"]  = importlib.import_module("jt.jpype._jwrapper")
    sys.modules["jpype._jvmfinder"] = importlib.import_module("jt.jpype._jvmfinder")
    sys.modules["jpype._linux"]     = importlib.import_module("jt.jpype._linux")
    sys.modules["jpype._darwin"]    = importlib.import_module("jt.jpype._darwin")
    sys.modules["jpype._cygwin"]    = importlib.import_module("jt.jpype._cygwin")
    sys.modules["jpype._windows"]   = importlib.import_module("jt.jpype._windows")

    import jpype
    jvm_path = jpype.getDefaultJVMPath(java_version=1.8)

    print("Running testsuite using JVM:", jvm_path, "\n", file=sys.stderr)

    try:
        tests = test_suite(sys.argv[1:] or None)
        result = unittest.TextTestRunner(verbosity=2).run(tests)
    finally:
        if jpype.isJVMStarted():
            jpype.shutdownJVM()

    sys.exit(0 if result.wasSuccessful() else 1)


if __name__.rpartition(".")[-1] == "__main__":
    # logging.basicConfig(level=logging.INFO)  # <AK> commented
    # logging.basicConfig(level=logging.DEBUG)
    main()
