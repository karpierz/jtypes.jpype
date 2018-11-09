# Copyright 2013-2018 Adam Karpierz
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

from ..jtypes._jclass import JavaClass
from ..jtypes._jclass import JavaObject


def JClass(name):

    from ..jtypes._jvm import JVM
    return JVM.jvm.JClass(name)
