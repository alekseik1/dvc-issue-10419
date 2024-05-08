import sys
import importlib
from importlib.util import find_spec

print(sys.path)
print("dvc.simple.deep.dep path:".ljust(30), find_spec("dvc_simple.deep.dep").origin)
print("deep.dep path:".ljust(30), find_spec("deep.dep").origin)

from dvc_simple.deep import dep

print(dep.my_str)

