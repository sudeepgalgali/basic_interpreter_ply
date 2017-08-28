import sys
print "Test 1, with ex1.py"
sys.argv = ['mini_interpreter.py','ex1.py']
execfile('mini_interpreter.py')
print "Test 2, with all arithmetic operations (sample_inputs)"
sys.argv = ['mini_interpreter.py','sample_inputs']
execfile('mini_interpreter.py')
