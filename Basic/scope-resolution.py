# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

# Local Scope

def func1():
  a=1 
#  print(b)        # this is invalid as a variable initialized in a function is only visible to that function. print(a) would be correct

def func2():
  b=2
#  print(a)        # this is invalid as a variable initialized in a function is only visible to that function. print(b) would be correct


# Enclosed scope

def funca():
  x = 1

  def funcb():
    x =  2            
    print(x)      # this will print 2
  funcb()
funca()


# Global Scope

def func01():
  print(z)

def func02():
  print(z)

z=3

func01()
func02()

# Built-in Scope

#Case - 1

from math import e

def func():
  print(e)      # this will print built in version of e

func()

#Case - 2

def funct():
  print(e)

e=4

funct()       # this will print e as 4 since order of hierarcy is LEGB hence, local is searched first and since found local value = 4, it is printed