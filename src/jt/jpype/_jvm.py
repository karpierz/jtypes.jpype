# Copyright 2013-2018 Adam Karpierz
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

from __future__ import absolute_import


def get_default_jvm_path():

    from ..jtypes._jvm import JVM
    return JVM.defaultPath()

getDefaultJVMPath = get_default_jvm_path


def startJVM(jvm=None, *args):

    # <AK> Extension for the original JPype:
    # jvm can be None, will be treated as use of default JVM path

    import collections as abcoll
    from ..jvm.lib.compat import builtins, str
    from ..jtypes._jvm    import JVM
    from ..jtypes         import _imports

    jvmoptions = []
    for opt in args:
        if isinstance(opt, (builtins.str, str)):
            jvmoptions.append(opt)
        elif isinstance(opt, abcoll.Sequence):  # pragma: no cover
            name  = opt[0]  # String
            value = opt[1]  # Callable
            # TODO complete this for the hooks ...
        else:
            from ..jtypes._exceptions import InvalidArgumentError
            raise InvalidArgumentError("VM Arguments must be string or tuple")

    vm = JVM()
    vm.load(jvm)
    vm.options.definitions = jvmoptions
    ret = vm.start()
    _imports.unregister()
    return ret


def attachToJVM(jvm=None):

    # <AK> Extension for the original JPype:
    # jvm can be None, will be treated as use of default JVM path

    from ..jtypes._jvm import JVM
    from ..jtypes      import _imports
    vm = JVM()
    vm.load(jvm)
    ret = vm.attach()
    _imports.unregister()
    return ret


def shutdownJVM():

    from ..jtypes._jvm import JVM
    return JVM.jvm.shutdown()


def isJVMStarted():

    from ..jtypes._jvm import JVM
    try:
        jvm = JVM.jvm
    except:
        return False
    else:
        return jvm.isStarted()


def attachThreadToJVM():

    from ..jtypes._jvm import JVM
    return JVM.jvm.attachThread()


def detachThreadFromJVM():

    from ..jtypes._jvm import JVM
    return JVM.jvm.detachThread()


def isThreadAttachedToJVM():

    from ..jtypes._jvm import JVM
    return JVM.jvm.isThreadAttached()


def synchronized(obj):

    from ..jtypes._jvm import JVM
    return JVM.jvm.synchronized(obj)


def setUsePythonThreadForDeamon(v):

    from ..jtypes._jvm import JVM
    JVM._use_jthread_for_refdaemon = not bool(v)
