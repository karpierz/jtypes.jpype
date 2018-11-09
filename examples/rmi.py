#*****************************************************************************
#   Copyright 2004-2008 Steve Menard
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
#
# porting for PY3, reformated (PEP8) and adopted for jt.jpype by Adam Karpierz

from __future__ import absolute_import, print_function

# the java classes used are defined the test harness.
# the class jpype.rmi.ServerImpl must be started before this script can be run.

from jt.jpype import *

import os.path
root = os.path.abspath(os.path.dirname(__file__))
startJVM(getDefaultJVMPath(),
         "-ea", "-Djava.class.path=%s/../tests/classes" % root)

if java.lang.System.getSecurityManager() is None:                     # <AK> fix: added
    java.lang.System.setSecurityManager(java.lang.SecurityManager())  # <AK> fix: added

p = java.rmi.Naming.lookup("rmi://localhost:2004/server")

print(p, p.__class__)

p.callRemote()

shutdownJVM()
