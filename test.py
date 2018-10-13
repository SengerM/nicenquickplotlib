import numpy as np
import nicenquickplotlib as nq

x = np.linspace(1,6)

nq.plot(x, [np.sin(x), np.cos(x), np.log(x)], title='default colors and linestyles')
nq.plot(x, [np.sin(x), np.cos(x), np.log(x)], linestyle='--', title='default colors and defined linestyle')
nq.plot(x, [np.sin(x), np.cos(x), np.log(x)], linestyle=['--','-.',':'], title='default colors and defined linestyles')

nq.set_figstyle('blacknwhite')
nq.plot(x, [np.sin(x), np.cos(x), np.log(x)], title='blacknwhite colors and linestyles')
nq.plot(x, [np.sin(x), np.cos(x), np.log(x)], linestyle='--', title='blacknwhite colors and defined linestyle')
nq.plot(x, [np.sin(x), np.cos(x), np.log(x)], linestyle=['--','-.',':'], title='blacknwhite colors and defined linestyles')

nq.save_all()
