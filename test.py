import numpy as np
import nicenquickplotlib as nq

x = np.linspace(1,6)
nq.set_figstyle('blacknwhite')
nq.plot(x, [np.sin(x), np.cos(x), np.log(x)], marker=True)

nq.save_all()
