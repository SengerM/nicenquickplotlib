# The idea of this script is to have a call to all functions of the
# nicenquickplotlib module in order to test all.

import numpy as np
import nicenquickplotlib as nq

x = []
x.append(np.linspace(0,6))
x.append(np.linspace(0,5))
x.append(np.linspace(0,4))

# Testing for data input combinations ----
nq.plot(x[0], title="data input x1")
nq.plot([x[0], x[1]], title="data input [x[0], x[1]]")
nq.plot(x[0], np.sin(x[0]), title="data input x[0], np.sin(x[0])")
nq.plot(x[0],[np.sin(x[0]), np.cos(x[0])], title="data input x[0],[np.sin(x[0]), np.cos(x[0])]")
nq.plot([x[0], x[1]], [np.sin(x[0]), np.cos(x[1])], title="data input [x[0], x[1]], [np.sin(x[0]), np.cos(x[1])]")
nq.plot(x, [np.sin(x[0]), np.cos(x[1]), np.sqrt(x[2])], title="data input x, [np.sin(x[0]), np.cos(x[1]), np.sqrt(x[2])]")
# Testingh the "togheter" option ----------
nq.plot(x, [np.sin(x[0]), np.cos(x[1]), np.sqrt(x[2])], together=False, title="together x, [np.sin(x[0]), np.cos(x[1]), np.sqrt(x[2])], toghether=False")
# Testing axis labels ---------------------
nq.plot(x, [np.sin(x[0]), np.cos(x[1]), np.sqrt(x[2])], xlabel='xlabel', ylabel='ylabel', title='labels all with the same ylabel')
nq.plot(x, [np.sin(x[0]), np.cos(x[1]), np.sqrt(x[2])], xlabel='xlabel', ylabel=['height', 'length', 'weight'], together=False, title='labels all with different ylabel')
# Changing the figstyle -------------------
nq.set_figstyle('blacknwhite') # All the plots from now on will use the 'blacknwhite' preset.
# Testing legend --------------------------
nq.plot(x[0], np.sin(x[0]), legend=r'$\sin (x)$', title='legend passing the legend as a string')
nq.plot(x[0], np.sin(x[0]), legend=[r'$\sin (x)$'], title='legend passing the legend as a list')
nq.plot(x, [np.sin(x[0]), np.cos(x[1]), np.sqrt(x[2])], legend=[r'$\sin(x)$', r'$\cos(x)$', r'$\sqrt{x}$'], title='legend multiple legends together')
nq.plot(x, [np.sin(x[0]), np.cos(x[1]), np.sqrt(x[2])], legend=[r'$\sin(x)$', r'$\cos(x)$', r'$\sqrt{x}$'], together=False, title='legend multiple legends together=False')
# Test colors -----------------------------
random_y = []
for k in range(10):
	random_y.append(np.random.normal(loc=k, size=10))
nq.set_figstyle('default')
nq.plot(random_y, title='colors')

nq.save_all()
