H = 2*np.pi * 0.1 * sigmax()
psi0 = basis(2, 0)
times = np.linspace(0.0, 10.0, 20)
result = sesolve(H, psi0, times, [sigmaz()])
