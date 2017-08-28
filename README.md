# basic_interpreter_ply
This is a basic interpreter constructed in python using ply package. It accepts any input string defined by the language:

 statements  s ::=  x = e  |   print e  | s s
 expressions e ::=  x  |  n  |  e + e  |  e - e  |  e * e  | e / e
 variables   x
 integers    n

as we can see, this language is ambiguous, so I have converted it to an ambiguous one which is described by the language:

statements s ::= x = e | print e
expressions e ::= t | e + t | e - t
term t ::= f | t * f | t / f
factor f::= x | n
variables x
integers n

Usage:

Pass the name of the input file to mini_interpreter.py as a commandline argument
EX: python mini_interpreter.py ex1.py
