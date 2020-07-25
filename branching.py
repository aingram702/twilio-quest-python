#!/usr/bin/python3
import sys

# Set up a list for our code to work with that omits the first CLI argument, 
# which is the name of our script (fizzbuzz.py)
inp = sys.argv
inp.pop(0)

# Process the "inputs" list as directed in your code
def fizzBuzz(inp):
    for i in inp:
        print(i)
        n = int(i)
        for x in range(1, n+1):
            
