# Copyright 2013-2018 Adam Karpierz
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

from ..jtypes._jarray import JavaArrayClass
from ..jtypes._jarray import JavaArray


def JArray(t, ndims=1):

    from ..jtypes._jvm import JVM
    return JVM.jvm.JArrayClass(t, ndims)
