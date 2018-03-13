#*****************************************************************************
#   Copyright 2017 Karl Einar Nelson
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
#*****************************************************************************
from __future__ import absolute_import
try:
    import unittest2 as unittest
except ImportError:
    import unittest
import sys
import jt.jpype as jpype
from . import common

class StartJVMCase(common.JPypeTestCase):

    def setUp(self):
        common.JPypeTestCase.setUp(self)

    def testInvalidArgument(self):  # <AK> added
        with self.assertRaisesRegexp(RuntimeError, "VM Arguments must be string or tuple"):
            jpype.startJVM(None, 1)
        with self.assertRaisesRegexp(RuntimeError, "VM Arguments must be string or tuple"):
            jpype.startJVM(jpype.getDefaultJVMPath(), 1)

    def testStartup(self):
        # Test that we are robust to multiple startJVM
        try:
            self.assertRaises(OSError, jpype.startJVM, jpype.getDefaultJVMPath())
            self.assertRaises(OSError, jpype.startJVM, jpype.getDefaultJVMPath())  # pragma: no cover
        except RuntimeError:
            pass 
        # Verify that we don't crash after repeat
        jpype.JClass("java.lang.String")

