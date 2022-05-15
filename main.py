import sys
import os

import PyInstaller.__main

from termcolor import colored




try:
  n = sys.argv[1]
  if n == "convert":
    file_name = input('Enter file name: ')
    with open(file_name) as file_handle:
      f = open(file_name, "r")
      f2 = open(file_name + ".py", "w")
      
      f2.write("import os \n")
      f2.write("os.system('''")
      f2.write(f.read() + "'''" + ')')
      f2.close()
      f.close()
      print("Built python file, use build to build!")
        
  if n == "build":
    file_name = input('Enter file name:')
    with open(file_name) as file_handle:
      f3 = open(file_name, "r")
      PyInstaller.__main__.run([
    file_name,
    '--onefile',
    '--windowed'
])
      
except (RuntimeError, NameError, BaseException): 
  print( colored('ERROR, NO FILE PASSED!', 'red'))
  input( colored("PRESS [ENTER] TO CONTINUE...", "red"))
  pass
