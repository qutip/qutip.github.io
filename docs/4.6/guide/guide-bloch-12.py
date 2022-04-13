b.clear()

xp = np.cos(th)
yp = np.sin(th)
zp = np.zeros(20)
pnts = [xp, yp, zp]
b.add_points(pnts, 'm')  # <-- add a 'm' string to signify 'multi' colored points
b.render()