H = [H0, [H1, 'A * exp(-(t / sig) ** 2)']]
args = {'A': 9, 'sig': 5}
output = mcsolve(H, psi0, times, c_ops, [a.dag()*a], args=args)
opts = Options(rhs_reuse=True)
args = {'A': 10, 'sig': 3}
output = mcsolve(H, psi0, times, c_ops, [a.dag()*a], args=args, options=opts)