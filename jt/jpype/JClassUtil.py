# Copyright 2013-2018 Adam Karpierz
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0


def isInterface(t):

    from ..jtypes._jclass import JavaObject
    return (isinstance(t, type) and issubclass(t, JavaObject) and
            t.__javaclass__.isInterface())
