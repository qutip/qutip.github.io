# Matsubara expansion:
bath = DrudeLorentzBath(Q, lam, gamma, T, Nk)

# Padé expansion:
bath = DrudeLorentzPadeBath(Q, lam, gamma, T, Nk)

# Add terminator to the system Liouvillian:
delta, terminator = bath.terminator()
HL = liouvillian(H_sys) + terminator

# Construct solver:
solver = HEOMSolver(HL, bath, max_depth=max_depth, options=options)