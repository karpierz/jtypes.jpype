# Copyright 2013-2018 Adam Karpierz
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# <AK> added
#

from __future__ import absolute_import

from . import common

from jt.jpype import JPackage, JClass
from jt.jpype import JClassUtil


class JClassUtilTestCase(common.JPypeTestCase):

    def testIsInterface(self):

        itf1 = JPackage("jpype").jclassutil.TestInterface1
        itf2 = JClass("jpype.jclassutil.TestInterface2")
        itf3 = JPackage("java.lang").Cloneable
        itf4 = JClass("java.io.Serializable")
        cls1 = JPackage("java.lang").Integer
        cls2 = JClass("java.math.BigInteger")

        self.assertTrue(JClassUtil.isInterface(itf1))
        self.assertTrue(JClassUtil.isInterface(itf2))
        self.assertTrue(JClassUtil.isInterface(itf3))
        self.assertTrue(JClassUtil.isInterface(itf4))
        self.assertFalse(JClassUtil.isInterface(cls1))
        self.assertFalse(JClassUtil.isInterface(cls2))
        self.assertFalse(JClassUtil.isInterface("skdffr"))
        self.assertFalse(JClassUtil.isInterface(12))

