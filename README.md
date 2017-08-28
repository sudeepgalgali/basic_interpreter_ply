# basic_interpreter_ply
This is a basic interpreter constructed in python using ply package. It accepts any input string defined by the language:

 statements  s ::=  x = e  |   print e  | s s
 
 expressions e ::=  x  |  n  |  e + e  |  e - e  |  e * e  | e / e
 
 variables   x
 
 integers    n

As we can see, this language is ambiguous, so I have converted it to an ambiguous one which is described by the language:


statements s ::= x = e | print e

expressions e ::= t | e + t | e - t

term t ::= f | t * f | t / f

factor f::= x | n

variables x

integers n

Usage:

Pass the name of the input file to mini_interpreter.py as a commandline argument

EX: python mini_interpreter.py ex1.py

Roadmap of the repository:

1. mini_interpreter.py : This is the script which performs the interpretation.

2. ex1.py : This is a sample input to the interpreter.

3. sample_inputs: This is another set of sample inputs to the interpreter.

4. tests.py: This script executes mini_interpreter.py with different arguments.

5. All other files are the bare minimum required either by travis or git.
