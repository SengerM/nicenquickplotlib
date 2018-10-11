import numpy as np
import nicenquickplotlib as nq

nq.default_fig_width = 200e-3 # Change the default figure width.

x1 = np.linspace(0,6)
x2 = np.linspace(1,5,10)
y1 = x1**2
y2 = np.sin(x1)
y3 = np.sqrt(x1)

nq.plot(y1) # Nice and quick plot with a nice grid.

figure_1 = nq.plot(x1, y1, title='I dont like this title') # Add a title.
figure_1.title = 'I like this title' # Change the title.

nq.plot([x1,x2], [np.sin(x1), np.sin(x2)], marker='.', title='Multiple [x,y] datasets together') # Multiple [x,y] datasets.
nq.plot([x1,x2], [np.sin(x1), np.sin(x2)], together=False, marker='.', title='Multiple [x,y] datasets in subplots') # Multiple [x,y] datasets.

nq.plot(x1, [y1, y2, y3], title='Multiple plots together') # Plot multiple 'y' datasets all with the same 'x' dataset.

nq.plot(x1, [y1, y2, y3], ylabel='Label', together=False) # Same label for all y axes.
nq.plot(x1, [y1, y2, y3], ylabel=['Label 1','Label 2', 'Label 3'], together=False) # Different labels for each y axis.

# Logarithmig scales ---------------------------------------
nq.plot(x1, [y1, y2, y3], xscale='L', xlabel='Log scale')
nq.plot(x1, [y1, y2, y3], together=False, yscale='L', ylabel='Log scale', xlabel='Lin scale')
nq.plot(x1, [y1, y2, y3], together=False, yscale='llL', ylabel=['Lin scale', 'Lin scale', 'Log scale'], xlabel='Lin scale')
I_want_log_axes = nq.plot(x1, [y1, y2, y3], together=False, ylabel=['Lin scale', 'Log scale', 'Lin scale'], xlabel='Lin scale')
I_want_log_axes.axes[1].set_yscale('log') # You can use the matplotlib methods too!

# Add a legend to your plots -----------------------------------
nq.plot(x1, [x1**2, np.sin(x1), np.sqrt(x1)], legend=[r'$x^2$',r'$\sin (x)$', r'$\sqrt{x}$']) # Use LaTeX!
nq.plot(x1, [x1**2, np.sin(x1), np.sqrt(x1)], legend=[r'$x^2$',r'$\sin (x)$', r'$\sqrt{x}$'], together=False)

nq.save_all(csv=True) # Save all your plots (and csv data files) with just one line!
