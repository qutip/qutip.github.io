from qutip.nonmarkov.heom import DrudeLorentzBath
from qutip.nonmarkov.heom import DrudeLorentzPadeBath

# Number of expansion terms to retain:
Nk = 2

# Matsubara expansion:
bath = DrudeLorentzBath(Q, lam, gamma, T, Nk)

# Padé expansion:
bath = DrudeLorentzPadeBath(Q, lam, gamma, T, Nk)