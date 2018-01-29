from __future__ import absolute_import, print_function
from jt.jpype import *
import time

def run():
    print('Thread started')
    try:
        print(repr(java.awt.Frame))
        javax.swing.JFrame("Test Frame").setVisible(True)
        shutdownGuiEnvironment()
    except JException as ex:
        print(ex)


startJVM(getDefaultJVMPath())

setupGuiEnvironment(run)