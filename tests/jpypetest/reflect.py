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
from jt.jpype import JPackage, JArray, JByte, java
from . import common

if sys.version > '3':
    unicode = str

class ReflectCase(common.JPypeTestCase):

    def setUp(self):
        common.JPypeTestCase.setUp(self)
        self.test1 = jpype.JClass('jpype.overloads.Test1')()
        self.Reflect = jpype.JClass('jpype.reflect.ReflectionTest')
        self.Annotation = jpype.JClass('jpype.reflect.Annotation')

    def testClass(self):
        t = jpype.JClass('java.lang.Object')
        obj = self.Reflect()
        print("Reflect")
        print("=======")
        print("@1@", type(self.Reflect),         self.Reflect,         id(self.Reflect))        
        print("@2@", type(self.Reflect.class_),  self.Reflect.class_,  id(self.Reflect.class_)) 
        print("@3@", type(obj.getClass()),       obj.getClass(),       id(obj.getClass()))      
        print("@4@", type(obj.__class__),        obj.__class__,        id(obj.__class__))       
        print("@5@", type(obj.__class__.class_), obj.__class__.class_, id(obj.__class__.class_))
        print()
        self.assertEquals('Class', self.test1.testClassVsObject(self.Reflect))
        self.assertEquals('Class', self.test1.testClassVsObject(self.Reflect.class_))
        self.assertEquals('Class', self.test1.testClassVsObject(obj.getClass()))
        self.assertEquals('Class', self.test1.testClassVsObject(obj.__class__.class_))

    def testAnnotation(self):
        method = self.Reflect.class_.getMethod('annotatedMethod')
        annotation = method.getAnnotation(self.Annotation)
        self.assertEquals('annotation', annotation.value())

    def testCallPublicMethod(self):
        method = self.Reflect.class_.getMethod('publicMethod')
        obj = self.Reflect()
        self.assertEquals('public', method.invoke(obj))

    def testCallPrivateMethod(self):
        method = self.Reflect.class_.getDeclaredMethod('privateMethod')
        obj = self.Reflect()
        self.assertEquals('private', method.invoke(obj))

    def testAccessPublicField(self):
        field = self.Reflect.class_.getField('publicField')
        obj = self.Reflect()
        self.assertEquals('public', field.get(obj))

    def testAccessPrivateField(self):
        field = self.Reflect.class_.getDeclaredField('privateField')
        obj = self.Reflect()
        self.assertEquals('private', field.get(obj))
