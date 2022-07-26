'''Modules & Packages'''

# Learn what a Python module is
# Learn how to make and use modules in our code
# Learn what a Python package is

'''Modules'''

# Modules are simply Python files with the .py extension which implement a set of functions. Modules are imported using the import command.

# The first time a module is loaded into a running Python script, it is initialized by executing the code in the module once. If another module in your code imports
#  the same module again, it will not be loaded twice but once only - so local variables inside the module act as a "singleton" - they are initialized only once.

# Now if we want to import the urllib.request module, which enables us to request data from URLs, we can simply import the module:

# import the library
from my_package.subdirectory import my_functions
import urllib.request
response = urllib.request.urlopen("http://www.codingdojo.com")
html = response.read()
print(html)

# Notice how we used urllib.request as a variable to refer to our module and then we called the methods using dot notation.

'''Creating Your Own Modules'''

# Writing your own Python modules is very simple. To create a module, we first create a new .py file with the module name in the same directory as
# the file that will import the module. Then we import it using the import command and the Python file name (without the .py extension)

# For example, let's create a module of arithmetic operations:

# CREATED TWO FILES IN FOLDER MODULAR_EXAMPLE

'''Standard (Built-In) Modules'''

# Python comes with a library of standard modules. Some modules are built into the interpreter; these provide access to operations that are not part of the core of the language but are nevertheless built-in, either for efficiency or to provide access to operating system primitives such as system calls. The set of such modules is a configuration option which also depends on the underlying platform. For example, the winreg module is only provided on Windows systems. One particular module deserves special mention: sys, which is built into every Python interpreter.

# A list of built-in modules could be found in this link.

'''Exploring Built-In Modules'''

# Two very important functions come in handy when exploring modules in Python - the dir and help functions. We can look for  which functions are implemented in each module by using the dir function

'''Packages'''
# A module is a single file (or files) that is imported under one import. A package is a collection of modules in directories that give a package hierarchy.


# Packages are namespaces which contain multiple packages and modules themselves. They are simply directories, but with a twist.

# sample_project
#      |_____ python_file.py
#      |_____ my_modules
#                |_____ __init__.py
#                |_____ test_module.py
#                |_____ another_module.py
#                |_____ third_module.py

# In the above diagram, the package name is my_modules.

'''Writing Packages'''

#If we create a directory called my_modules, which marks the package name, we can then create a module inside that package called test_module.

# To use the module test_module, we can import it in two ways:

import my_modules.test_module

from my_modules import test_module

'''__init__.py File'''

#You may have noticed the __init__.py file outlined in the structure above and wondered what it is. This file was required for all packages in Python 2.7; it would often be empty, but was required to indicate that the files in the folder were part of the package.

# In Python 3.3+, we only need this file if we need to customize what modules are available to anyone attempting to import the package. For example, if we didn't want another_module or third_module to be accessible for importing, we could override the __all__ variable, like so:

# sample_project/my_modules/__init__.py

__all__ = ["test_module"]