# Nice 'n quick plot lib
Package to produce nice plots quickly using matplotlib.

This package contains a set of functions to help the user to produce nice plots without having to worry about formatting them. It uses matplotlib to produce high quality plots. There are a set of "default config params" that can be modified in order that all plots to have the same format.

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

nq.save_all(csv=True) # Save all your plots (and csv data files) with just one line!
```
See also the "example.py" file.
