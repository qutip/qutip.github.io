# Convenience functions and parameters:

def cot(x):
    return 1. / np.tan(x)

beta = 1. / T

# Number of expansion terms to calculate:
Nk = 2

# C_real expansion terms:
ck_real = [lam * gamma / np.tan(gamma / (2 * T))]
ck_real.extend([
    (8 * lam * gamma * T * np.pi * k * T /
        ((2 * np.pi * k * T)**2 - gamma**2))
    for k in range(1, Nk + 1)
])
vk_real = [gamma]
vk_real.extend([2 * np.pi * k * T for k in range(1, Nk + 1)])

# C_imag expansion terms (this is the full expansion):
ck_imag = [lam * gamma * (-1.0)]
vk_imag = [gamma]