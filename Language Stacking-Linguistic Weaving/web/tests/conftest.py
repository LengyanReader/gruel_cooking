import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
WEB = os.path.dirname(HERE)
if WEB not in sys.path:
    sys.path.insert(0, WEB)