import numpy as np
import nicenquickplotlib as nq

x = np.linspace(0,6)
y1 = x**2
y2 = np.sin(x)
y3 = np.sqrt(x)

nq.plot(y1) # Nice and quick plot!

figure_1 = nq.plot(x, y1, title='I dont like this title') # Add a title.
figure_1.title = 'I like this title'

nq.plot(x, [y1, y2, y3], title='Multiple functions together') # Plot multiple sets in one plot.
nq.plot(x, [y1, y2, y3], together=False, title='Multiple functions in subplots') # Plot multiple sets in different subplots.

nq.plot(x, [y1, y2, y3], ylabel='Same label', together=False, title='Same label for all y axes')
nq.plot(x, [y1, y2, y3], ylabel=['Label 1','Label 2', 'Label 3'], together=False, title='Different labels for all y axes')

# Logarithmig scales ---------------------------------------
nq.plot(x, [y1, y2, y3], xscale='L', xlabel='Log scale')
nq.plot(x, [y1, y2, y3], together=False, yscale='L', ylabel='Log scale')
nq.plot(x, [y1, y2, y3], together=False, yscale='llL', ylabel=['Lin scale', 'Lin scale', 'Log scale'])

nq.save_all() # Save all your plots!
# ~ nq.show()
