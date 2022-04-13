N = 10  # number of basis states to consider

a = destroy(N)

H = a.dag() * a

psi0 = basis(N, 9)  # initial state

kappa = 0.2  # coupling to oscillator

a_ops = [[a+a.dag(), '{kappa}*exp(-t)*(w>=0)'.format(kappa=kappa)]]

tlist = np.linspace(0, 10, 100)

out = brmesolve(H, psi0, tlist, a_ops, e_ops=[a.dag() * a])

actual_answer = 9.0 * np.exp(-kappa * (1.0 - np.exp(-tlist)))

plt.figure()

plt.plot(tlist, out.expect[0])

plt.plot(tlist, actual_answer)

plt.show()