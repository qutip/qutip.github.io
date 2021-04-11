Q_coherent = qfunc(rho_coherent, xvec, xvec)

Q_thermal = qfunc(rho_thermal, xvec, xvec)

Q_fock = qfunc(rho_fock, xvec, xvec)

fig, axes = plt.subplots(1, 3, figsize=(12,3))

cont0 = axes[0].contourf(xvec, xvec, Q_coherent, 100)

lbl0 = axes[0].set_title("Coherent state")

cont1 = axes[1].contourf(xvec, xvec, Q_thermal, 100)

lbl1 = axes[1].set_title("Thermal state")

cont0 = axes[2].contourf(xvec, xvec, Q_fock, 100)

lbl2 = axes[2].set_title("Fock state")

plt.show()