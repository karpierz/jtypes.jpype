from __future__ import absolute_import
import sys, os, runpy
cur_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(cur_dir))
runpy.run_module(os.path.basename(cur_dir))
