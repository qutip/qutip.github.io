kappa = 0.5

def col_coeff(t, args):  # coefficient function
    return np.sqrt(kappa * np.exp(-t))

N = 10  # number of basis states
a = destroy(N)
H = a.dag() * a  # simple HO
psi0 = basis(N, 9)  # initial state
c_ops = [[a, col_coeff]]  # time-dependent collapse term
times = np.linspace(0, 10, 100)
output = mesolve(H, psi0, times, c_ops, [a.dag() * a])