from qutip.nonmarkov.heom import LorentzianBath
from qutip.nonmarkov.heom import LorentzianPadeBath

# Number of expansion terms to retain:
Nk = 2

# Matsubara expansion:
bath_L = LorentzianBath(Q, gamma, W, mu_L, T, Nk, tag="L")
bath_R = LorentzianBath(Q, gamma, W, mu_R, T, Nk, tag="R")

# Padé expansion:
bath_L = LorentzianPadeBath(Q, gamma, W, mu_L, T, Nk, tag="L")
bath_R = LorentzianPadeBath(Q, gamma, W, mu_R, T, Nk, tag="R")