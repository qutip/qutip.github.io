delta = 0.1  * 2 * np.pi  # qubit sigma_x coefficient
w = 2.0  * 2 * np.pi      # driving frequency
T = 2 * np.pi / w         # driving period
gamma1 = 0.00001          # relaxation rate
gamma2 = 0.005            # dephasing  rate

eps_list = np.linspace(-10.0, 10.0, 51) * 2 * np.pi  # epsilon
A_list = np.linspace(0.0, 20.0, 51) * 2 * np.pi      # Amplitude

sx = sigmax(); sz = sigmaz(); sm = destroy(2); sn = num(2)

c_ops = [np.sqrt(gamma1) * sm, np.sqrt(gamma2) * sz]  # relaxation and dephasing
H0 = -delta / 2.0 * sx
H1 = [sz, '-eps / 2.0 + A / 2.0 * sin(w * t)']
H_td = [H0, H1]
Hargs = {'w': w, 'eps': eps_list[0], 'A': A_list[0]}