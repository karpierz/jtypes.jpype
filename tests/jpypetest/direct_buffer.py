# Copyright 2013-2018 Adam Karpierz
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# <AK> added
#

from __future__ import absolute_import

import jpype
from . import common


class DirectBufferTestCase(common.JPypeTestCase):

    DATA_SIZE = 5 * 1024 * 1024 # 5 MB

    @classmethod
    def setUpClass(cls):
        super(DirectBufferTestCase, cls).setUpClass()
        cls.ByteBuffer = jpype.JClass("java.nio.ByteBuffer")

    def testDirectBuffer(self):
        data = b'X' * self.DATA_SIZE
        buff = jpype.nio.convertToDirectBuffer(data)
        self.assertIsInstance(buff, self.ByteBuffer)

