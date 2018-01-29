from __future__ import absolute_import, print_function
from jt.jpype import *
import time

remote_pack="c:/tools/netbeean-remote-pack"

profiler_options = [
        "-agentpath:%s/lib/deployed/jdk15/windows/profilerinterface.dll=%s/lib,5140" % (remote_pack, remote_pack)
]

options = [
        '-verbose:gc',
        '-Xmx17m',  # <AK> was: '-Xmx16m'
] #+ profiler_options

startJVM(getDefaultJVMPath(), *options)

class MyStr(bytes):
    def __del__(self):
        print('string got deleted')

while True:
    buf = java.lang.String('5' * 1024 * 1024 * 5)
    buf = nio.convertToDirectBuffer(MyStr(b'5' * 1024 * 1024))
#       time.sleep(1)

shutdownJVM()  # <AK> added
