from sympy import symbols, solve, diff, integrate, sin
# afficher un symbols
x= symbols('x')
# resoudre une equation
eq= x**2+3*x+2
result=solve(eq, x)
# derivation et intégration
eq2= x**2*sin(x)
result2= diff(eq2, x)
result3= integrate(eq2, x)
print('\na=',result, '\nb=',result2, '\nc=',result3)
