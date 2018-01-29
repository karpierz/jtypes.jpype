# Copyright 2013-2018 Adam Karpierz
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

__all__ = ('__title__', '__summary__', '__uri__', '__version_info__',
           '__version__', '__author__', '__email__', '__copyright__',
           '__license__')

__title__        = "jtypes.jpype"
__summary__      = "A Python to Java bridge (ctypes/cffi-based JPype)."
__uri__          = "http://pypi.python.org/pypi/jtypes.jpype/"
__version_info__ = type("version_info", (), dict(serial=2,
                        major=0, minor=6, micro=2, releaselevel="beta"))
__version__      = "{0.major}.{0.minor}.{0.micro}{1}{2}".format(__version_info__,
                   dict(final="", alpha="a", beta="b", rc="rc")[__version_info__.releaselevel],
                   "" if __version_info__.releaselevel == "final" else __version_info__.serial)
__author__       = "Adam Karpierz"
__email__        = "python@python.pl"
__copyright__    = "Copyright 2013-2018 {0}".format(__author__)
__license__      = "Apache License, Version 2.0 ; {0}".format(
                   "http://www.apache.org/licenses/LICENSE-2.0")
