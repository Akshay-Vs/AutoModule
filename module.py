
"""
Package Handling Tool
======================
This will automatically install missing modules from the current working file\n
--------------------------------------------------------------------------
All you need to do is initialize the module 
>>> from module import intialize
>>> initialize(__file__) #with default iteration
>>> #you can also use custom iterations but not recommended eg:(__file__,3)
>>> #Write your code here
    Other functions
    -------------- 
>>> use("name")#install a single module
>>> all("name1","name2")#install multiple packages
>>> check("name")#check weather the package is not installed or not
>>> remove("name")#remove a module
>>> _list_("name")#list installed modules
>>> show("name")#show details about a specific module
>>> cache("name")#download a package
"""

import importlib, importlib.util
import sys
import os
import platform
import warnings
import termcolor

def use(name):
    r'''install a single module
    >>> eg: use('numpy')'''
    if name in sys.modules:
      print(f"{name!r} is already imported in your code")
      try:
        importlib.__import__(name)
      except ImportError:print(f"Failed to install {name}")
    elif (spec := importlib.util.find_spec(name)) is not None: 
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
        
        #Write some code to import the module
        print(f"{name!r} imported")
    else:
        print(f"\nInstalling{name!r}...")
        os.system(f'python -m pip install {name}')   

def all(*args):
   r'''installs multiple packages one by one
   >>> eg: all("numpy","matplotlib")'''
   for name in args:
      if name in sys.modules:
        print(f"{name!r} is already imported in your code")
        module=importlib.__import__(name) 
      elif (spec := importlib.util.find_spec(name)) is not None: 
          module = importlib.util.module_from_spec(spec)
          sys.modules[name] = module
          spec.loader.exec_module(module)

          #Write some code to import the module
          print(f"{name!r} imported")
      else:
          print(f"\nInstalling{name!r}...")
          os.system(f'python -m pip install {name}')   

def check(name):
  """check weather the module is installed or not
  >>> eg: check('numpy')"""
  if name in sys.modules:
    print(f"{name!r} is already imported in your code")
  elif (spec := importlib.util.find_spec(name)) is not None: 
    print(f"{name!r} is installed on your device")
  else:
    user_choice=input(f'{name} is not installed yet\nDo you want to install {name}? [y/n]')
    if user_choice=='y':use.single(name)
    elif user_choice=='n':pass
    else:print('Invalid input')

def show(name):
    """This will show the module"""
    try:os.system(f'python -m pip show {name}') 
    except Exception:
      user_choice=input(f"Seems like {name} not found")

def search(name):
    """This will search for the module"""
    try:print(f'Searching for {name}...');os.system(f'python -m pip search {name}')
    except Exception as e:print("something went wrong\n{e}")

def _list_():
    """\tlist installed packeges"""
    os.system('python -m pip list')

def cache(name):os.system(f"python -m pip download {name}")
  
def remove(name):
  """\tremove an installed package
  >>> eg: remove("numpy")"""
  if name=="autopy":
      print("\n\tUNINSTALLING WORKING MODULE WILL CAUSE ERRORS AND MAKE YOUR CODE UNUSABLE\n")
  choice=input(f"Are you sure to remove {name}?\nEnter YES,PROCEED to continue:")
  if choice == 'YES,PROCEED':os.system(f'python -m pip uninstall {name}')
  else:print("Operetion Cancelled")

############################################################## not stable ##############################################

def clear():
   if os.name=='posix':_=os.system('clear')
   else:_=os.system('cls')


'''
console = AutopyConsole()
console.shellify(__file__)
console.console()
error=console.get_error_message()
poss_error="ModuleNotFoundError"
if poss_error in error:print("A module is not installed")

class hook(AutopyConsole):
  #Hook differrrent distros for different operating systems
  processor=platform.processor()
  operating_system=platform.platform()

  def __init__(self,name,processor=None,operating_system=None):
    super().__init__()
    super().shellify(__file__)
    super().console()
    super().get_error_msg()
    self.processor=processor
    self.operating_system=operating_system
    self.name=name
    clear()
    self.system_spec()

  @classmethod
  def system_spec(self,operating_system="MAC OS",processor="M1"):
    if "Windows" in self.operating_system:
      operating_system="Windows Distro"
      self.install(self,spec_os=operating_system,name=None)

    elif "Ubuntu" in self.operating_system:
      operating_system="Ubuntu Distro"
      self.install(self,os=operating_system)

    elif "Mac" in self.operating_system:
      operating_system="Mac OS"
      self.install(self,os=operating_system)

    elif "Chrome" in self.operating_system:
      operating_system="Chrome OS"
      self.install(self,os=operating_system)


  def get_name():
    console = AutopyConsole()
    console.shellify(__file__)
    console.console()
    poss_error="ModuleNotFoundError"
    if poss_error in error:print("A module is not installed")
    print(ImportError.__class__.__name__ + ": " + ImportError)
  
  def install(self,name,spec_os=None):
    print(f"You are using {spec_os} with a {self.processor}")
    '''
    
def initialize(runfile,iteration=1):
  clear()
  termcolor.cprint("tracking errors...",'yellow')
  for i in range(iteration):
    try:
        with open(runfile,"r") as rnf:
            exec(rnf.read())
            print("No errors found")
            clear()
        
        
    except ImportError as e:
        termcolor.cprint("ERROR FOUND",'red')
        print(e);t=str(e) 
        name=(t.split("'")[-2])
        use(name)
        clear()

    
if __name__=="__main__":
  termcolor.cprint("warning",'yellow')
  initialize(__file__)
  console=AutopyConsole()
  error=console.get_error_msg()
  x=hook("numpy") 
  #print(x.system_spec())
  all("numpy","matplotlib")
