from sympy import pretty_print as pp
from sympy.abc import a,b,n

expr = (a*b)**n
pp(expr) 


print("===========")
a,b,n = 2,1,5
expr = (a*b)**n
pp(expr)
