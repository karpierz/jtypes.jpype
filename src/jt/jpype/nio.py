# Copyright 2013-2018 Adam Karpierz
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0


def convertToDirectBuffer(obj):

    """Efficiently convert all array.array and numpy ndarray types,
    string and unicode to java.nio.Buffer objects."""

    from ..jtypes._jvm import JVM
    return JVM.jvm.asDirectByteBuffer(obj)
