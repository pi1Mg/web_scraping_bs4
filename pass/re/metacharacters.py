import re


#  Specialised language which can be used to search for text
#  within a given document with precision and efficiency

#  Expression --> compiled into bytecode --> executed by a
#  matching engine written in C

#  Usage:
#  Matching characters
"""
a simple expression matches itself in the given string

abc

Exception --> Meta characters: . ^ * + ? { } [ ] \ | ( )
They don't match themselves

"""

#  Character class --> [  ]
#  user inputs b than z
#  [abcdef] will match user input --> for b returns True, for z returns F
#  [a-f] --> all characters between a and f are included


