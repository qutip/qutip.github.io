S = Cubic_Spline(t[0], t[-1], noisy_data)

plt.figure()
plt.plot(t, func(t))
plt.plot(t, noisy_data, 'o')
plt.plot(t, S(t), lw=2)
plt.show()