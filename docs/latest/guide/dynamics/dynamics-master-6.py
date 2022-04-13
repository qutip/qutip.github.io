times = np.linspace(0.0, 10.0, 200)
psi0 = tensor(fock(2,0), fock(10, 5))
a  = tensor(qeye(2), destroy(10))
sm = tensor(destroy(2), qeye(10))
H = 2 * np.pi * a.dag() * a + 2 * np.pi * sm.dag() * sm + 2 * np.pi * 0.25 * (sm * a.dag() + sm.dag() * a)
result = mesolve(H, psi0, times, [np.sqrt(0.1)*a], [a.dag()*a, sm.dag()*sm])
plt.figure() # doctest: +SKIP
plt.plot(times, result.expect[0]) # doctest: +SKIP
plt.plot(times, result.expect[1]) # doctest: +SKIP
plt.xlabel('Time') # doctest: +SKIP
plt.ylabel('Expectation values') # doctest: +SKIP
plt.legend(("cavity photon number", "atom excitation probability")) # doctest: +SKIP
plt.show() # doctest: +SKIP
