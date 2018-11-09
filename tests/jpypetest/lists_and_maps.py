from __future__ import absolute_import, print_function  # <AK> added
from . import common
from jpype import java

class ListsAndMapsTestCase(common.JPypeTestCase):

    def test_Lists(self):
        arr = java.util.ArrayList()
        data = [str(x) for x in range(20)]
        arr.addAll(data)
        #print(arr)
        #for x in arr: print(x, end="")
        #print()
        self.assertSequenceEqual(arr, data)

    def test_Maps(self):
        hmap = java.util.HashMap()
        data = {5:6, 7:8, "hello":"there"}
        hmap.putAll(data)
        #print(hmap)
        #for x in hmap: print(x, hmap[x], end="")
        #print()
        self.assertEqual(data, hmap)
        for x in range(5):
            hmap.put(str(x), str(x)) # this works:
            hmap.put(str(x), x)      # but this did'nt, but now works
        #for x in hmap: print(x, hmap[x], end="")
        #print()

    def test_Sets(self):
        hset = java.util.HashSet()
        data1 = (6, 8, "there")
        data2 = set((10, 12, "seven"))
        hset.addAll(data1)
        hset.addAll(data2)
        #print(hset)
        #for x in hset: print(x, end="")
        #print()
        self.assertCountEqual(hset, set(data1) | data2)
        for x in range(5):
            hset.add(x)
        #for x in hset: print(x, end="")
        #print()
        self.assertCountEqual(hset, set(data1) | data2 | set(range(5)))
