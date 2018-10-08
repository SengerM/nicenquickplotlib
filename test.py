import numpy as np
import nicenquickplotlib as nq

x = np.linspace(0,6)
y1 = x**2
y2 = np.sin(x)**2
y3 = np.sqrt(x)

nq.plot(x, [y1, y2, y3], xscale='L', xlabel='Log scale')
nq.plot(x, [y1, y2, y3], together=False, yscale='L', ylabel='Log scale')
nq.plot(x, [y1, y2, y3], together=False, yscale='llL', ylabel=['Lin scale', 'Lin scale', 'Log scale'])

nq.save_all()
# ~ nq.show()
