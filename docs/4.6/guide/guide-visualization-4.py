fig, axes = plt.subplots(1, 3, figsize=(12,3))

plot_fock_distribution(rho_coherent, fig=fig, ax=axes[0], title="Coherent state");

plot_fock_distribution(rho_thermal, fig=fig, ax=axes[1], title="Thermal state");

plot_fock_distribution(rho_fock, fig=fig, ax=axes[2], title="Fock state");

fig.tight_layout()

plt.show()