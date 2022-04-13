# The size of the system:
N_sys = 3

def proj(i, j):
    """ A helper function for creating an interaction operator. """
    return basis(N_sys, i) * basis(N_sys, j).dag()

# Construct one bath for each system state:
baths = []
for i in range(N_sys):
    Q = proj(i, i)
    baths.append(DrudeLorentzBath(Q, lam, gamma, T, Nk))

# Construct the system Liouvillian from the system Hamiltonian and
# bath expansion terminators:
H_sys = sum((i + 0.5) * eps * proj(i, i) for i in range(N_sys))
H_sys += sum(
  (i + j + 0.5) * Del * proj(i, j)
  for i in range(N_sys) for j in range(N_sys)
  if i != j
)
HL = liouvillian(H_sys) + sum(bath.terminator()[1] for bath in baths)

# Construct the solver (pass a list of baths):
solver = HEOMSolver(HL, baths, max_depth=max_depth, options=options)

# Run the solver:
rho0 = basis(N_sys, 0) * basis(N_sys, 0).dag()
tlist = np.linspace(0, 5, 200)
e_ops = {
    f"P{i}": proj(i, i)
    for i in range(N_sys)
}
result = solver.run(rho0, tlist, e_ops=e_ops)

# Plot populations:
fig, axes = plt.subplots(1, 1, sharex=True, figsize=(8,8))
for label, values in result.expect.items():
    axes.plot(result.times, values, label=label)
axes.set_xlabel(r't', fontsize=28)
axes.set_ylabel(r"Population", fontsize=28)
axes.legend(loc=0, fontsize=12)