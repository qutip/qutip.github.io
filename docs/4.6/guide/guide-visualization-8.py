N = 5

a = tensor(destroy(N), qeye(2))

b = tensor(qeye(N), destroy(2))

sx = tensor(qeye(N), sigmax())

H = a.dag() * a + sx - 0.5 * (a * b.dag() + a.dag() * b)

# visualize H

lbls_list = [[str(d) for d in range(N)], ["u", "d"]]

xlabels = []

for inds in tomography._index_permutations([len(lbls) for lbls in lbls_list]):
   xlabels.append("".join([lbls_list[k][inds[k]] for k in range(len(lbls_list))]))

fig, ax = matrix_histogram(H, xlabels, xlabels, limits=[-4,4])

ax.view_init(azim=-55, elev=45)

plt.show()