# Shared bath properties:
gamma = 0.01   # coupling strength
W = 1.0  # cut-off
T = 0.025851991  # temperature
beta = 1. / T

# Chemical potentials for the two baths:
mu_L = 1.
mu_R = -1.

# System-bath coupling operator:
Q = destroy(2)