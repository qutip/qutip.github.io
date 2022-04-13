from qutip.nonmarkov.heom import HEOMSolver
from qutip import Options

max_depth = 5  # maximum hierarchy depth to retain
options = Options(nsteps=15_000)
baths = [bath_L, bath_R]

solver = HEOMSolver(H_sys, baths, max_depth=max_depth, options=options)