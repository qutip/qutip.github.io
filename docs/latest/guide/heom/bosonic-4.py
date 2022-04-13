from qutip.nonmarkov.heom import HEOMSolver
from qutip import Options

max_depth = 5  # maximum hierarchy depth to retain
options = Options(nsteps=15_000)

solver = HEOMSolver(H_sys, bath, max_depth=max_depth, options=options)