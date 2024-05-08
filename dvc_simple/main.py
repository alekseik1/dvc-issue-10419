import sys
import importlib
from importlib.util import find_spec

print(sys.path)
print(find_spec("dvc_simple.deep.dep").origin)
print(find_spec("deep.dep").origin)

from dvc_simple.deep import dep

print(dep.my_str)

