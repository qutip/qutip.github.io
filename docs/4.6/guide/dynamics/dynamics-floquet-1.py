delta = 0.2 * 2*np.pi
eps0 = 1.0 * 2*np.pi
A = 2.5 * 2*np.pi
omega = 1.0 * 2*np.pi
H0 = - delta/2.0 * sigmax() - eps0/2.0 * sigmaz()
H1 = A/2.0 * sigmaz()
args = {'w': omega}
H = [H0, [H1, 'sin(w * t)']]
