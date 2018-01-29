# <AK> converted from pytest to unittest
#
"""
Checks for memory leak in the JVM when pushing array data from Python to Java.
"""
from __future__ import absolute_import, print_function

import sys
if sys.version_info.major <= 2: range = xrange
import jt.jpype as jpype
from . import common

#!!! These settings are finely tuned !!!
#!!! DO NOT fiddle with them unless you know what you are doing !!!

#   Size of array to be copied.
ARRAY_SIZE = 4000000

#   Number of iterations to run.
#   - raise this value to increase efficacy of the memory leak test.
ITERATIONS = 10

#   Maximum size of JVM heap.
#   - sets a cap to allow memory leak detection.
MAX_JVM_HEAP_SIZE_BYTES = 101384192 # 100994192 ## 390000  # <AK> originally was: 128647168

class ArrayFixesTestCase(common.JPypeTestCase):

    @classmethod
    def setUpClass(cls):
        #   Module-level setup.
        if not jpype.isJVMStarted():
            jvm_args = [
                '-Xmx%dM' % (MAX_JVM_HEAP_SIZE_BYTES // 1000 ** 2),
            ]
            jpype.startJVM(jpype.getDefaultJVMPath(), *jvm_args)
        cls.JavaDoubleArray = jpype.JArray(jpype.JDouble, 1)

    @classmethod
    def tearDownClass(cls):
        # <AK> added
        jpype.shutdownJVM()

    def test_memory_leak_fix(self):
        """
        This test raises java.lang.VirtualMachineErrorPyRaisable
        (java.lang.OutOfMemoryError: Java heap space) if the memory leak
        is present.

        """
        #   Check memory settings.
        rt = jpype.java.lang.Runtime.getRuntime()
        # <AK>: assertTrue -> assertEqual
        self.assertEqual(rt.maxMemory(), MAX_JVM_HEAP_SIZE_BYTES)

        #   Perform leak test.
        for i in range(ITERATIONS):
            print('iteration:', i)
            py_list1 = [float(f) for f in range(ARRAY_SIZE)]
            j_array1 = self.JavaDoubleArray(py_list1)
            py_list2 = j_array1[:]
            self.assertTrue(py_list1 == py_list2)

    def test_jarray_basic_slicing_fix(self):
        jl1 = self.JavaDoubleArray([1., 2., 3.])
        self.assertTrue(list(jl1) == [1., 2., 3.])
        self.assertTrue(list(jl1[0:-1]) == [1., 2.])
        self.assertTrue(list(jl1[0:1]) == [1.])

    def test_jarray_slice_copy_fix(self):
        jl1 = self.JavaDoubleArray([1., 2., 3.])
        pl1 = jl1[:]
        self.assertTrue(list(jl1) == pl1)

    def test_jarray_slice_assignment_fix(self):
        jl2 = self.JavaDoubleArray([1., 2., 3.])
        jl2[:] = [4., 5., 6.]
        self.assertTrue(list(jl2) == [4., 5., 6.])
