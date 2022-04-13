from qutip import basis, sigmax, sigmaz

# The system Hamiltonian:
eps = 0.5  # energy of the 2-level system
Del = 1.0  # tunnelling term
H_sys = 0.5 * eps * sigmaz() + 0.5 * Del * sigmax()

# Initial state of the system:
rho0 = basis(2,0) * basis(2,0).dag()