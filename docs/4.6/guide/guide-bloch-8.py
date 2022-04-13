x = (qutip.basis(2, 0) + (1+0j)*qutip.basis(2, 1)).unit()
y = (qutip.basis(2, 0) + (0+1j)*qutip.basis(2, 1)).unit()
z = (qutip.basis(2, 0) + (0+0j)*qutip.basis(2, 1)).unit()

b.add_states([x, y, z])
b.render()