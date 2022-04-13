args = {'A': 9, 'sigma': 5}
output = mesolve(H, psi0, times, c_ops, [a.dag() * a], args=args)