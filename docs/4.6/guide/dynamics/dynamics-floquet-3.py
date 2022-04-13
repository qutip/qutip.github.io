delta = 0.2 * 2*np.pi
eps0  = 0.0 * 2*np.pi
omega = 1.0 * 2*np.pi
A_vec = np.linspace(0, 10, 100) * omega
T = (2*np.pi)/omega
tlist = np.linspace(0.0, 10 * T, 101)
spsi0 = basis(2,0)
q_energies = np.zeros((len(A_vec), 2))
H0 = delta/2.0 * sigmaz() - eps0/2.0 * sigmax()
args = {'w': omega}
for idx, A in enumerate(A_vec): # doctest: +SKIP
  H1 = A/2.0 * sigmax() # doctest: +SKIP
  H = [H0, [H1, lambda t, args: np.sin(args['w']*t)]] # doctest: +SKIP
  f_modes, f_energies = floquet_modes(H, T, args, True) # doctest: +SKIP
  q_energies[idx,:] = f_energies # doctest: +SKIP
plt.figure() # doctest: +SKIP
plt.plot(A_vec/omega, q_energies[:,0] / delta, 'b', A_vec/omega, q_energies[:,1] / delta, 'r') # doctest: +SKIP
plt.xlabel(r'$A/\omega$') # doctest: +SKIP
plt.ylabel(r'Quasienergy / $\Delta$') # doctest: +SKIP
plt.title(r'Floquet quasienergies') # doctest: +SKIP
plt.show() # doctest: +SKIP
