import ply.lex as lex
import sys
import ply.yacc as yacc

reserved = {'print' : 'PRINT'}
tokens= ['VAR','NUMBER','PLUS','MINUS','MUL','DIV',] + list(reserved.values())
literals= ['+','=','-','*','/']

def t_VAR(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value,'VAR')
    return t

#match numbers and convert to float
def t_NUMBER(t):
    r'\d+'
    t.value=float(t.value)
    return t

t_ignore=" \t"

#counting line numbers, needed for effective debugging
def t_newline(t):
    r'\n+'
    t.lexer.lineno+=t.value.count("\n")

def t_error(t):
    print ("Invalid input '%s', please check input" % t.value[0])
    t.lexer.skip(1)

#intialize lexer
lex.lex(debug=1)

#define precedence
precedence =(('left','*'),('left','/'),('left','+'),('left','-'))

var={}

def p_equation(p):
    'S : VAR "=" EXP'
    var[p[1]] = p[3]

def p_print_op(p):
    'S : PRINT EXP'
    print(p[2])

def p_EXPoperations(p):
    '''EXP : EXP "+" TERM
        | EXP "-" TERM
        | TERM'''
    if '+' in p:
        p[0] = p[1] + p[3]
    elif '-' in p:
        p[0] = p[1] - p[3]
    else:
        p[0] = p[1]

def p_TERMoperations(p):
    '''TERM : TERM "*" FACT
        | TERM "/" FACT
        | FACT'''
    if '*' in p:
        p[0] = p[1] * p[3]
    elif '/' in p:
        p[0] = p[1] / p[3]
    else:
        p[0] = p[1]
def p_FACTvariable(p):
    'FACT : VAR'
    p[0] = var[p[1]]

def p_FACTName(p):
    'FACT : NUMBER'
    p[0] = p[1]
def p_error(p):
    if p:
        print("Error, Check '%s'" % p.value)
    else:
        print("Syntax Error at EOF")
        

yacc.yacc()
fp = open(sys.argv[1],"r")
ll=fp.readlines()
for l in ll:
    yacc.parse(l)
