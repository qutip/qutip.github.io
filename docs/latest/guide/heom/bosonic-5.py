# Define the operators that measure the populations of the two
# system states:
P11p = basis(2,0) * basis(2,0).dag()
P22p = basis(2,1) * basis(2,1).dag()

# Define the operator that measures the 0, 1 element of density matrix
# (corresonding to coherence):
P12p = basis(2,0) * basis(2,1).dag()

# Run the solver:
tlist = np.linspace(0, 20, 101)
result = solver.run(rho0, tlist, e_ops={"11": P11p, "22": P22p, "12": P12p})

# Plot the results:
fig, axes = plt.subplots(1, 1, sharex=True, figsize=(8,8))
axes.plot(result.times, result.expect["11"], 'b', linewidth=2, label="P11")
axes.plot(result.times, result.expect["12"], 'r', linewidth=2, label="P12")
axes.set_xlabel(r't', fontsize=28)
axes.legend(loc=0, fontsize=12)