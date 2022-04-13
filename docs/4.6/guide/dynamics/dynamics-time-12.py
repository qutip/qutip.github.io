H = [H0, [H1, 'A * exp(-(t / sig) ** 2)']]
args = {'A': 9, 'sig': 5}
output = mesolve(H, psi0, times, c_ops, [a.dag()*a], args=args)