# Copyright 2013-2018 Adam Karpierz
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# <AK> added
#

from __future__ import absolute_import, print_function

from . import common

from jt.jpype import java, reflect


class ReflectionTestCase(common.JPypeTestCase):

    def testReflection(self):

        String = java.lang.String

        modifiers             = reflect.getModifiers(String)
        constructors          = reflect.getConstructors(String)
        declared_constructors = reflect.getDeclaredConstructors(String)
        methods               = reflect.getMethods(String)
        declared_methods      = reflect.getDeclaredMethods(String)
        fields                = reflect.getFields(String)
        declared_fields       = reflect.getDeclaredFields(String)

        self.assertEqual(modifiers,                  0b10001)
        self.assertEqual(len(constructors),          15)
        self.assertEqual(len(declared_constructors), 16)
        self.assertEqual(len(methods),               76)
        self.assertEqual(len(declared_methods),      77)
        self.assertEqual(len(fields),                1)
        self.assertEqual(len(declared_fields),       5)

        constructors          = [item.toString() for item in constructors]
        declared_constructors = [item.toString() for item in declared_constructors]
        methods               = [item.toString() for item in methods]
        declared_methods      = [item.toString() for item in declared_methods]
        fields                = [item.toString() for item in fields]
        declared_fields       = [item.toString() for item in declared_fields]

        class_name = String.__javaclass__.getName()

        #print("Constructors of {}:         ".format(class_name), constructors)
        #print("Declared constructors of {}:".format(class_name), declared_constructors)
        #print("Methods of {}:              ".format(class_name), methods)
        #print("Declared methods of {}:     ".format(class_name), declared_methods)
        #print("Fields of {}:               ".format(class_name), fields)
        #print("Declared fields of {}:      ".format(class_name), declared_fields)

