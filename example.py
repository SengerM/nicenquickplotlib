import numpy as np
import nicenquickplotlib as nq

x = np.linspace(0,6)
x1 = np.linspace(0,6)
x2 = np.linspace(1,5,10)
y1 = x**2
y2 = np.sin(x)
y3 = np.sqrt(x)

nq.plot(y1) # Nice and quick plot!

figure_1 = nq.plot(x, y1, title='I dont like this title') # Add a title.
figure_1.title = 'I like this title' # Change the title.

nq.plot([x1,x2], [np.sin(x1), np.sin(x2)], marker='.', title='Multiple [x,y] datasets together') # Multiple [x,y] datasets.
nq.plot([x1,x2], [np.sin(x1), np.sin(x2)], together=False, marker='.', title='Multiple [x,y] datasets in subplots') # Multiple [x,y] datasets.

nq.plot(x, [y1, y2, y3], title='Multiple plots together') # Plot multiple sets in one plot.
nq.plot(x, [y1, y2, y3], together=False, title='Subplot') # Plot multiple sets in different subplots.

nq.plot(x, [y1, y2, y3], ylabel='Label', together=False, title='Same label for all y axes')
nq.plot(x, [y1, y2, y3], ylabel=['Label 1','Label 2', 'Label 3'], together=False, title='Different labels for each y')

# Logarithmig scales ---------------------------------------
nq.plot(x, [y1, y2, y3], xscale='L', xlabel='Log scale')
nq.plot(x, [y1, y2, y3], together=False, yscale='L', ylabel='Log scale')
nq.plot(x, [y1, y2, y3], together=False, yscale='llL', ylabel=['Lin scale', 'Lin scale', 'Log scale'])
I_want_log_axes = nq.plot(x, [y1, y2, y3], together=False, ylabel=['Lin scale', 'Log scale', 'Lin scale'])
I_want_log_axes.axes[1].set_yscale('log') # You can use the matplotlib methods too!

nq.save_all() # Save all your plots!
# ~ nq.show()
