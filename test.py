import numpy as np
import nicenquickplotlib as nq

x = []
x.append(np.linspace(0,6))
x.append(np.linspace(0,5))
x.append(np.linspace(0,4))

nq.set_figstyle('default')
nq.plot(x, [np.sin(x[0]), np.cos(x[1]), np.sqrt(x[2])], legend=[r'$\sin(x)$', r'$\cos(x)$', r'$\sqrt{x}$'], xlabel='x label', ylabel='y label')
nq.set_figstyle('blacknwhite')
nq.plot(x, [np.sin(x[0]), np.cos(x[1]), np.sqrt(x[2])], legend=[r'$\sin(x)$', r'$\cos(x)$', r'$\sqrt{x}$'], xlabel='x label', ylabel='y label')
nq.set_figstyle('soft')
nq.plot(x, [np.sin(x[0]), np.cos(x[1]), np.sqrt(x[2])], legend=[r'$\sin(x)$', r'$\cos(x)$', r'$\sqrt{x}$'], xlabel='x label', ylabel='y label')

nq.save_all()
