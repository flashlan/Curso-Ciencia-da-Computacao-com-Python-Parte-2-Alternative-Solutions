# -*- coding: utf-8 -*-
"""
Created on Mon May 18 00:05:41 2020

@author: pcstream
"""

def fib(n,depth=0):
    print (''.join(["*"]*depth), n)

    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1,depth+1) + fib(n-2,depth+1)

fib(5)

'''
probaly is like  this:

                                          fib(5)
                       fib(4)               +                  fib(3)
              fib(3)     +      fib(2)      +         fib(2)     +   fib(1)   
     fib(2)     + fib(1) + fib(1) + fib(0)  +    fib(1) + fib(0) +     1
fib(1) + fib(0) +   1    +   1    +   1     +      1    +   1    +     1
  1    +   1    +   1    +   1    +   1     +      1    +   1    +     1
  
  
'''  