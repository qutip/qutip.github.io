import numpy as np
import matplotlib.pyplot as plt
import qutip as qt

# parameters
DIM = 20             # Hilbert space dimension
DELTA = 5*2*np.pi    # cavity detuning
KAPPA = 2            # cavity decay rate
INTENSITY = 4        # intensity of initial state
NUMBER_OF_TRAJECTORIES = 500

# operators
a = qt.destroy(DIM)
x = a + a.dag()
H = DELTA*a.dag()* a

rho_0 = qt.coherent(DIM, np.sqrt(INTENSITY))
times = np.arange(0, 1, 0.0025)

stoc_solution = qt.smesolve(H, rho_0, times,
                            c_ops=[],
                            sc_ops=[np.sqrt(KAPPA) * a],
                            e_ops=[x],
                            ntraj=NUMBER_OF_TRAJECTORIES,
                            nsubsteps=2,
                            store_measurement=True,
                            dW_factors=[1],
                            method='homodyne')

fig, ax = plt.subplots()
ax.set_title('Stochastic Master Equation - Homodyne Detection')
ax.plot(times, np.array(stoc_solution.measurement).mean(axis=0)[:].real,
        'r', lw=2, label=r'$J_x$')
ax.plot(times, stoc_solution.expect[0], 'k', lw=2,
        label=r'$\langle x \rangle$')
ax.set_xlabel('Time')
ax.legend()