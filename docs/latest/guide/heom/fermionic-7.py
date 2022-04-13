# Run the solver (returning ADO states):
tlist = np.linspace(0, 100, 201)
result = solver.run(rho0, tlist, e_ops={
    "left_currents": heom_left_current,
    "right_currents": heom_right_current,
})

# Plot the results:
fig, axes = plt.subplots(1, 1, sharex=True, figsize=(8,8))
axes.plot(
    result.times, result.expect["left_currents"], 'b',
    linewidth=2, label=r"Bath L",
)
axes.plot(
    result.times, result.expect["right_currents"], 'r',
    linewidth=2, label="Bath R",
)
axes.set_xlabel(r't', fontsize=28)
axes.set_ylabel(r'Current', fontsize=20)
axes.set_title(r'System to Bath Currents', fontsize=20)
axes.legend(loc=0, fontsize=12)