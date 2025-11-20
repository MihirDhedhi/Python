import sympy as sp

n, z = sp.symbols('n z')

seq3 = 3**n

Z3 = sp.summation(seq3 * z**(-n), (n, 0, sp.oo))

print("Z-transform of x[n] = 3^n u[n]:")
sp.pprint(Z3, use_unicode=True)






import sympy as sp

n, z, omega = sp.symbols('n z omega')

seq_cos = sp.cos(omega * n)

Zcos = sp.summation(seq_cos * z**(-n), (n, 0, sp.oo))

print("Z-transform of x[n] = cos(ωn) u[n]:")
sp.pprint(Zcos, use_unicode=True)
