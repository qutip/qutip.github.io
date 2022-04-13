b.clear()

th = np.linspace(0, 2*np.pi, 20)
xp = np.cos(th)
yp = np.sin(th)
zp = np.zeros(20)

pnts = [xp, yp, zp]
b.add_points(pnts)
b.render()