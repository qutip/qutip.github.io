from qutip import basis, destroy

# The system Hamiltonian:
e1 = 1.  # site energy
H_sys = e1 * destroy(2).dag() * destroy(2)

# Initial state of the system:
rho0 = basis(2,0) * basis(2,0).dag()