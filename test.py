import numpy as np
import nicenquickplotlib as nq

x1 = np.linspace(0,6)
x2 = np.linspace(1,5,10)
y1 = x1**2
y2 = np.sin(x1)
y3 = np.sqrt(x1)

nq.plot(y1, marker='.')
nq.plot([y1,y2,y3])
nq.plot(x1, y1)
nq.plot(x1, [y1,y2,y3])
nq.plot([x1,x2], [np.sin(x1), np.sin(x2)], marker='.')
nq.plot([x1,x2], [np.sin(x1), np.sin(x2)], together=False, marker='.', title='My beautiful plot')

nq.save_all(csv=True)
