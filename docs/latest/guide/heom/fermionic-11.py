# Imports
from numpy.linalg import eigvalsh

# Convenience functions and parameters:
def deltafun(j, k):
    """ Kronecker delta function. """
    return 1.0 if j == k else 0.

def f_approx(x, Nk):
    """ Padé approxmation to Fermi distribution. """
    f = 0.5
    for ll in range(1, Nk + 1):
        # kappa and epsilon are calculated further down
        f = f - 2 * kappa[ll] * x / (x**2 + epsilon[ll]**2)
    return f

def kappa_epsilon(Nk):
    """ Calculate kappa and epsilon coefficients. """

    alpha = np.zeros((2 * Nk, 2 * Nk))
    for j in range(2 * Nk):
        for k in range(2 * Nk):
            alpha[j][k] = (
                (deltafun(j, k + 1) + deltafun(j, k - 1))
                / np.sqrt((2 * (j + 1) - 1) * (2 * (k + 1) - 1))
            )

    eps = [-2. / val for val in eigvalsh(alpha)[:Nk]]

    alpha_p = np.zeros((2 * Nk - 1, 2 * Nk - 1))
    for j in range(2 * Nk - 1):
        for k in range(2 * Nk - 1):
            alpha_p[j][k] = (
                (deltafun(j, k + 1) + deltafun(j, k - 1))
                / np.sqrt((2 * (j + 1) + 1) * (2 * (k + 1) + 1))
            )

    chi = [-2. / val for val in eigvalsh(alpha_p)[:Nk - 1]]

    eta_list = [
        0.5 * Nk * (2 * (Nk + 1) - 1) * (
            np.prod([chi[k]**2 - eps[j]**2 for k in range(Nk - 1)]) /
            np.prod([
                eps[k]**2 - eps[j]**2 + deltafun(j, k) for k in range(Nk)
            ])
        )
        for j in range(Nk)
    ]

    kappa = [0] + eta_list
    epsilon = [0] + eps

    return kappa, epsilon

kappa, epsilon = kappa_epsilon(Nk)

# Phew, we made it to function that calculates the coefficients for the
# correlation function expansions:

def C(sigma, mu, Nk):
    """ Calculate the expansion coefficients for C_\sigma. """
    beta = 1. / T
    ck = [0.5 * gamma * W * f_approx(1.0j * beta * W, Nk)]
    vk = [W - sigma * 1.0j * mu]
    for ll in range(1, Nk + 1):
        ck.append(
            -1.0j * (kappa[ll] / beta) * gamma * W**2
            / (-(epsilon[ll]**2 / beta**2) + W**2)
        )
        vk.append(epsilon[ll] / beta - sigma * 1.0j * mu)
    return ck, vk

ck_plus_L, vk_plus_L = C(1.0, mu_L, Nk)  # C_+, left bath
ck_minus_L, vk_minus_L = C(-1.0, mu_L, Nk)  # C_-, left bath

ck_plus_R, vk_plus_R = C(1.0, mu_R, Nk)  # C_+, right bath
ck_minus_R, vk_minus_R = C(-1.0, mu_R, Nk)  # C_-, right bath