times = np.linspace(0.0, 10.0, 100)
result = mesolve(H, psi0, times, [np.sqrt(0.05) * sigmax()], [sigmaz(), sigmay()])
fig, ax = plt.subplots()
ax.plot(times, result.expect[0]) # doctest: +SKIP
ax.plot(times, result.expect[1]) # doctest: +SKIP
ax.set_xlabel('Time') # doctest: +SKIP
ax.set_ylabel('Expectation values') # doctest: +SKIP
ax.legend(("Sigma-Z", "Sigma-Y"))  # doctest: +SKIP
plt.show() # doctest: +SKIP
