from qutip import *
settings.colorblind_safe = True

import matplotlib.pyplot as plt
plt.rcParams['savefig.transparent'] = True

X = sigmax()
S = spre(X) * spost(X.dag())

hinton(S)