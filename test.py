import numpy as np
import nicenquickplotlib as nq

x = np.linspace(0,6)
y1 = x**2
y2 = np.sin(x)
y3 = np.sqrt(x)

nq.plot(y1)

my_fig = nq.plot(x, y1, xlabel='x label')
my_fig.title = 'Plot with x data and x label'

nq.plot(x, [y1, y2, y3], xlabel='x label', title='Multiple functions together')
nq.plot(x, [y1, y2, y3], xlabel='x label', together=False, title='Multiple subplots')

nq.plot(x, [y1, y2, y3], xlabel='x label', ylabel='Same label', together=False, title='Same label for all y axes')
log_x_fig = nq.plot(x, [y1, y2, y3], xlabel='x label', ylabel=['Label 1','Label 2', 'Label 3'], together=False, title='Different labels for all y axes')
log_x_fig.axes[0].set_xscale('log')

nq.save_all()
# ~ nq.show()
