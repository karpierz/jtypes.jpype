# Copyright 2013-2018 Adam Karpierz
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

from ..jtypes      import _jproxy
from ..jtypes._jvm import JVM


class JProxy(_jproxy.JProxy):

    jvm = JVM._jvm_ref()

    def __new__(cls, intf, dict=None, inst=None):

        if dict is not None and inst is not None:
            raise RuntimeError("Specify only one of dict and inst")

        proxy = super(JProxy, cls).__new__(cls,
                                           inst if inst is not None else dict,
                                           intf)
        return proxy.asObject()


del _jproxy
del JVM
