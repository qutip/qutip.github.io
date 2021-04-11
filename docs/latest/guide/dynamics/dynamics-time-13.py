t = np.linspace(-15, 15, 100)
func = lambda t: 9*np.exp(-(t / 5)** 2)
noisy_func = lambda t: func(t)+(0.05*func(t))*np.random.randn(t.shape[0])
noisy_data = noisy_func(t)

plt.figure()
plt.plot(t, func(t))
plt.plot(t, noisy_data, 'o')
plt.show()