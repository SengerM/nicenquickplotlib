# Nice 'n quick plot lib

This package contains a set of functions that help the user to produce nice plots very quickly and without having to worry about formatting. The idea is that each call to "plot" produces one new figure that will be ready to save. The package automatically keeps track of all the figures and then you can do what you usually want with just one line: save all your figures just calling "save_all" function.

There are a set of "default configuration parameters" that can be modified in order to control things such as the default size of all figures, the default colors, etc. In the future the plan is to allow the user to define "custom presets".

Nice and quick plot lib uses Matplotlib to produce the plots. The nicenquickplotlib figures are stored in a self defined class called ```Figure```. You can access to any of the matplotlib objects through ```Figure.fig``` and ```Figure.axes```.

## Instalation
- Python 2
```
pip install git+https://github.com/SengerM/nicenquickplotlib.git
```
- Python 3
```
pip3 install git+https://github.com/SengerM/nicenquickplotlib.git
```

## Usage
```Python
import numpy as np
import nicenquickplotlib as nq
# Create some data to plot ---
x1 = np.linspace(0,6)
x2 = np.linspace(1,5,10)
# ----------------------------
nq.plot(np.sin(x1)) # This is figure number 1
figure_1 = nq.plot(x1, np.sin(x1), title='Figure with title') # This is figure number 2
nq.plot([x1,x2], [np.sin(x1), np.sin(x2)], marker='.', title='Multiple [x,y] datasets together') # Multiple [x,y] datasets.
nq.plot([x1,x2], [np.sin(x1), np.sin(x2)], together=False, marker='.', title='Multiple [x,y] datasets in subplots') # Multiple [x,y] datasets.
nq.plot(x1, [np.sin(x1), np.sqrt(x1), np.cos(x1)], title='Different "y" all with the same "x"')
nq.plot(x1, [np.sin(x1), np.sqrt(x1), np.cos(x1)], ylabel='Label', together=False) # Same label for all y axes.
nq.plot(x1, [np.sin(x1), np.sqrt(x1), np.cos(x1)], ylabel=['Label 1','Label 2', 'Label 3'], together=False) # Different labels for each y axis.

nq.save_all(csv=True) # Wow! You can save all your plots (and csv data files) with just one line! This is amazing!
```
See also the "example.py" file.
