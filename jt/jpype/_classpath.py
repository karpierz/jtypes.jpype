# Copyright 2013-2018 Adam Karpierz
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

from __future__ import absolute_import

import os.path as _osp
import glob    as _glob
import sys
_is_cygwin = (sys.platform == "cygwin")
del sys

__all__ = ('addClassPath', 'getClassPath')

_CLASSPATHS = set()
_PATHSEP = ";" if _is_cygwin else _osp.pathsep


def _init():

    import os
    global _CLASSPATHS
    global _PATHSEP
    classpath = os.environ.get("CLASSPATH")
    if classpath:
        _CLASSPATHS |= set(classpath.split(_PATHSEP))


_init()


# Cygwin needs to convert to windows paths
if _is_cygwin:

    _root = None

    def _get_root():

        global _root
        if _root is None:
            import subprocess
            proc = subprocess.Popen("cygpath -wa /", shell=True,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT,
                                    close_fds=True)
            _root = proc.stdout.read().strip().decode("utf-8")
        return _root


    def _splitpath(path):

        parts = []
        while True:
            path, tail = _osp.split(path)
            if not (path and tail):
                break
            parts.insert(0, tail)
        return parts


    def _posix2win(directory):

        root  = _get_root()
        paths = _splitpath(_osp.abspath(directory))
        if paths[0] == "cygdrive":
            paths.pop(0)
            drive = paths.pop(0)
            paths.insert(0, "{}:".format(drive))
        else:
            paths.insert(0, root)
        return "\\".join(paths)


    # needed for testing
    __all__.append("_posix2win")


def addClassPath(path):

    """Add a path to the java class path"""

    global _CLASSPATHS
    path = _osp.abspath(path)
    if _is_cygwin:
        path = _posix2win(path)
    _CLASSPATHS.add(path)


def getClassPath():

    """Get the full java class path.

    Includes user added paths and the environment CLASSPATH.
    """

    global _CLASSPATHS
    global _PATHSEP
    out = []
    for path in _CLASSPATHS:
        if path.endswith("*"):
            # AK: fix: was: if len(path) == 0
            out.extend(_glob.glob(path + ".jar"))
        elif path:
            out.append(path)
    return _PATHSEP.join(out)
