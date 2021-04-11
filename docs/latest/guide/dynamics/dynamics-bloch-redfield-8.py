N = 10

w0 = 1.0 * 2 * np.pi

g = 0.05 * w0

kappa = 0.15

times = np.linspace(0, 25, 1000)

a = destroy(N)

H = w0 * a.dag() * a + g * (a + a.dag())

psi0 = ket2dm((basis(N, 4) + basis(N, 2) + basis(N, 0)).unit())

a_ops = [[ (a, a.dag()), ('{0} * (w >= 0)'.format(kappa), 'exp(1j*t)', 'exp(-1j*t)') ]]

e_ops = [a.dag() * a, a + a.dag()]

res_brme = brmesolve(H, psi0, times, a_ops, e_ops)

plt.figure()

plt.plot(times,res_brme.expect[0], label=r'$a^{+}a$')

plt.plot(times,res_brme.expect[1], label=r'$a+a^{+}$')

plt.legend()

plt.show()