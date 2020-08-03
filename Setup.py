import cx_Freeze
import sys
import os 
from setuptools import setup
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\ANKIT-PC\AppData\Local\Programs\Python\Python38-32\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\ANKIT-PC\AppData\Local\Programs\Python\Python38-32\tcl\tk8.6"
 
executables = [cx_Freeze.Executable("vpad.py", base=base, icon="icon.ico")]


cx_Freeze.setup(
    name = "WorkForWin Editor",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["icon.ico",'tcl86t.dll','tk86t.dll', 'icons2']}},
    version = "1.1",
    description = "Computer Science Community WorkForWin",
    executables = executables
    )
