import numpy as np
import nicenquickplotlib as nq

x = np.linspace(1,6)

nq.plot(x, [np.sin(x), np.cos(x), np.log(x)], title='Default colors and linestyles')
nq.plot(x, [np.sin(x), np.cos(x), np.log(x)], linestyle='--', title='Default colors and defined linestyle')
nq.plot(x, [np.sin(x), np.cos(x), np.log(x)], linestyle=['--','-.',':'], title='Default colors and defined linestyles')

nq.save_all()
