H = 2*np.pi * 0.1 * sigmax()
psi0 = basis(2, 0)
times = np.linspace(0.0, 10.0, 100)
result = sesolve(H, psi0, times, [sigmaz(), sigmay()])
fig, ax = plt.subplots()
ax.plot(result.times, result.expect[0]) # doctest: +SKIP
ax.plot(result.times, result.expect[1]) # doctest: +SKIP
ax.set_xlabel('Time') # doctest: +SKIP
ax.set_ylabel('Expectation values') # doctest: +SKIP
ax.legend(("Sigma-Z", "Sigma-Y")) # doctest: +SKIP
plt.show() # doctest: +SKIP
