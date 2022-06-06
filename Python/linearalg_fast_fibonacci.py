#!/usr/bin/env python

import math

def quickfib(n):
	return 1/math.sqrt(5)*( (math.pow(((1 + math.sqrt(5))/2), n)
                         -
                         (math.pow(((1 - math.sqrt(5))/2), n)
                         +
                         (math.pow(((1 + math.sqrt(5))/2), n - 1)
                         -
                         (math.pow(((1 + math.sqrt(5))/2), n - 1))))) )



for x in range(10):
        print quickfib(x)
