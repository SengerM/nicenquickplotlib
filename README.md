# Nice 'n quick plot lib

This package contains a set of functions that help the user to produce nice plots very quickly and without having to worry about formatting. The idea is that each call to ```plot``` produces one new figure that will be ready to save. The package automatically keeps track of all the figures and then you can do what you usually want to with just one line: save all your figures just calling ```save_all``` function. The ```save_all``` function also allows to save a CSV file containing the data ploted. This means that if you are in the lab taking measurements, you can use *nicenquickplotlib* to plot and save your data with the same command. Great, huh? 

There are a set of "default configuration parameters" that can be modified in order to control things such as the default size of all figures, the default colors, etc. In the future the plan is to allow the user to define "custom presets".

Nice and quick plot lib uses Matplotlib to produce the plots. The *nicenquickplotlib* figures are stored in a self defined class called ```Figure```. You can access to any of the matplotlib objects through ```Figure.fig``` and ```Figure.axes```.

## Instalation
Make sure you have Pip installed, then open a terminal (cmd in Windows or any terminal in Ubuntu) and type:
- Python 2
```
pip install git+https://github.com/SengerM/nicenquickplotlib.git
```
- Python 3
```
pip3 install git+https://github.com/SengerM/nicenquickplotlib.git
```

## Usage
You have to worry about nothing but plot. Just call the ```plot``` function N times and then call the ```save_all``` function:
```Python
import numpy as np
import nicenquickplotlib as nq
# Create some data to plot ---
x1 = np.linspace(0,6)
x2 = np.linspace(1,5,10)
# ----------------------------
nq.plot(np.sin(x1)) # This is figure number 1
nq.plot(x1, np.sin(x1), title='Figure with title') # This is figure number 2
nq.plot([x1,x2], [np.sin(x1), np.sin(x2)], marker='.', title='Multiple [x,y] datasets together') # Multiple [x,y] datasets.
nq.plot([x1,x2], [np.sin(x1), np.sin(x2)], together=False, marker='.', title='Multiple [x,y] datasets in subplots') # Multiple [x,y] datasets.
nq.plot(x1, [np.sin(x1), np.sqrt(x1), np.cos(x1)], title='Different "y" all with the same "x"')
nq.plot(x1, [np.sin(x1), np.sqrt(x1), np.cos(x1)], ylabel='Label', together=False) # Same label for all y axes.
nq.plot(x1, [np.sin(x1), np.sqrt(x1), np.cos(x1)], ylabel=['Label 1','Label 2', 'Label 3'], together=False) # Different labels for each y axis.

nq.save_all(csv=True, timestamp='now') # Wow! You can save all your plots (and csv data files) with just one line! This is amazing!
nq.show()
```
See also the "test_all_all.py" file.

### Important usage tips

- Currently *nicenquickplotlib* only supports plotting numpy arrays. This means that **the data you pass to the ```plot``` function must be stored in numpy arrays**.
- If multiple data sets are to be plotted in the same figure, then ```plot``` expects a list of numpy arrays, but **not a bidimensional numpy array (not a numpy matrix)**. 
For example:
```Python
xdata_list = [1,2,3,4] # This is a list! And its currently unsoported.
xdata_np = np.array(xdata_list) # Now it was converted into a numpy array.
ydata_1 = np.array([1,2,3,4])
ydata_2 = np.array([1,3,5,7])
y_list = [ydata_1, ydata_2] # This is a list of numpy arrays, and it is what we want.
y_wrong = np.array([ydata_1, ydata_2]) # This is a "numpy matrix" and we don't want this!
```
If we call the ```plot``` function we should expect what follows:
```Python
plot(xdata_list, ydata_1) # Error because x data is a list.
plot(xdata_np, ydata_1) # This sould work fine.
plot(xdata_np, y_list) # This should work because y_list is a list of numpy arrays.
plot(xdata_np, y_wrong) # This should not work.
plot(xdata_np, [[1,2,3,4],[1,3,5,7]]) # This should not work because y data is a list of lists.
```
### Change the default plotting style
```Python
import numpy as np
import nicenquickplotlib as nq
x = np.linspace(0,6)
nq.set_figstyle('blacknwhite')
nq.plot(x, [np.sin(x), np.sqrt(x), np.cos(x)]) # This will be plotted using the 'blacknwhite' figstyle.
nq.set_figstyle('default')
nq.plot(x, [np.sin(x), np.sqrt(x), np.cos(x)]) # This will be plotted using the 'default' figstyle.
nq.save_all()
```
### Use the timestamp
If you want to run your code multiple times and keep all the figures and data each time without loosing the previous ones, you can call the ```save_all``` function with the ```timestamp``` option:
```Python
import numpy as np
import nicenquickplotlib as nq
x = np.linspace(0,6)
nq.plot(x, [np.sin(x), np.sqrt(x), np.cos(x)])
nq.save_all(timestamp=True) # or timestamp='now' if you are using Spyder or a similar program.
```
### Image file format
Change the default (png) file format for saving the images. Any of the formats supported by the [savefig](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.savefig.html) function is supported.
```Python
import numpy as np
import nicenquickplotlib as nq
x = np.linspace(0,6)
nq.plot(x, [np.sin(x), np.sqrt(x), np.cos(x)])
nq.save_all(image_format='pdf')
```
## Future plans
- Include plotting with error bars in a *nice and quick approach*.
- Implement the custom user preset feauture so you can configure your plots as you like in a *nice and quick approach*.
- Give support for plotting with measurement units (maybe using *pint* package) in a *nice and quick approach*.
