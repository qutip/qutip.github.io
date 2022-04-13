fig, axes = plt.subplots(1, 3, figsize=(12,3))

bar0 = axes[0].bar(np.arange(0, N)-.5, rho_coherent.diag())

lbl0 = axes[0].set_title("Coherent state")

lim0 = axes[0].set_xlim([-.5, N])

bar1 = axes[1].bar(np.arange(0, N)-.5, rho_thermal.diag())

lbl1 = axes[1].set_title("Thermal state")

lim1 = axes[1].set_xlim([-.5, N])

bar2 = axes[2].bar(np.arange(0, N)-.5, rho_fock.diag())

lbl2 = axes[2].set_title("Fock state")

lim2 = axes[2].set_xlim([-.5, N])

plt.show()