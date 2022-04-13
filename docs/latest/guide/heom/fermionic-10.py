# Plot the results and steady state currents:
fig, axes = plt.subplots(1, 1, sharex=True, figsize=(8,8))
axes.plot(
    result.times, result.expect["left_currents"], 'b',
    linewidth=2, label=r"Bath L",
)
axes.plot(
    result.times, [steady_state_current_left] * len(result.times), 'b:',
    linewidth=2, label=r"Bath L (steady state)",
)
axes.plot(
    result.times, result.expect["right_currents"], 'r',
    linewidth=2, label="Bath R",
)
axes.plot(
    result.times, [steady_state_current_right] * len(result.times), 'r:',
    linewidth=2, label=r"Bath R (steady state)",
)
axes.set_xlabel(r't', fontsize=28)
axes.set_ylabel(r'Current', fontsize=20)
axes.set_title(r'System to Bath Currents (with steady states)', fontsize=20)
axes.legend(loc=0, fontsize=12)