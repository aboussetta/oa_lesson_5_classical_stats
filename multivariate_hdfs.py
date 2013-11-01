#! /usr/bin/env python

from function_generator import *

if __name__ == "__main__":
  x,y = multivariate(3,-25,25,50000)
  for i in range(len(x)):
    print x,y
