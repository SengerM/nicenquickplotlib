# Nice 'n quick plot lib

**IMPORTANT NOTE** This package can be used but is obsolete. A new version with a slightly different approach is under development under the name [alfplotlib](https://github.com/SengerM/alfplotlib). It is recomended to use that package.

This package contains a set of functions that help the user to produce nice plots very quickly and without having to worry about formatting. The idea is that each call to ```plot``` produces one new figure that will be ready to save. The package automatically keeps track of all the figures and then you can do what you usually want to with just one line: save all your figures just calling ```save_all``` function. The ```save_all``` function also allows to save a CSV file containing the ploted data. This means that if you are in the lab taking measurements, you can use *nicenquickplotlib* to plot and save your data with the same command. Great, huh? 

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
Once it is installed you can test it running the following script:
```Python
import numpy as np
import nicenquickplotlib as nq
x = np.linspace(0,6)
nq.plot(x, [np.sin(x), np.sqrt(x), np.cos(x)])
nq.plot(x, x**2)
nq.save_all()
```
As a result a directory must be created inside the current working directory with the two figures as png files.

## Usage
You have to worry about nothing but to plot your data. Just call the ```plot``` function N times and in the end call the ```save_all``` function:
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
See also the [test_all_all.py](https://github.com/SengerM/nicenquickplotlib/blob/master/test_all_all.py) file for some examples.

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

### Use the timestamp
If you want to run your code multiple times and keep all the figures and data each time without loosing the previous ones, you can call the ```save_all``` function with the ```timestamp``` option:
```Python
import numpy as np
import nicenquickplotlib as nq
x = np.linspace(0,6)
nq.plot(x, [np.sin(x), np.sqrt(x), np.cos(x)])
nq.save_all(timestamp=True) # or timestamp='now' if you are using Spyder or a similar program.
```
The ```timestamp=True``` option uses a timestamp generated at the moment you import the *nicenquickplotlib*. The ```timestamp='now'``` option creates a new timestamp at the moment you call the ```save_all``` function.

### Image file format
Change the default (png) file format for saving the images. Any of the formats supported by the [savefig](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.savefig.html) function is supported.
```Python
import numpy as np
import nicenquickplotlib as nq
x = np.linspace(0,6)
nq.plot(x, [np.sin(x), np.sqrt(x), np.cos(x)])
nq.save_all(image_format='pdf')
```
### Change the figstyle
The *figstyle* contains some global parameters that define how your plots will look like. You can chose between any of the preset figstyles included with *nicenquickplotlib* or you can define your own figstyle to customize all your plots. The following code 
```Python
import numpy as np
import nicenquickplotlib as nq

x = []
x.append(np.linspace(0,6))
x.append(np.linspace(0,5))
x.append(np.linspace(0,4))

nq.set_figstyle('default') # This is not necesary.
nq.plot(x, [np.sin(x[0]), np.cos(x[1]), np.sqrt(x[2])], legend=[r'$\sin(x)$', r'$\cos(x)$', r'$\sqrt{x}$'], xlabel='x label', ylabel='y label')
nq.set_figstyle('blacknwhite')
nq.plot(x, [np.sin(x[0]), np.cos(x[1]), np.sqrt(x[2])], legend=[r'$\sin(x)$', r'$\cos(x)$', r'$\sqrt{x}$'], xlabel='x label', ylabel='y label')
nq.set_figstyle('soft')
nq.plot(x, [np.sin(x[0]), np.cos(x[1]), np.sqrt(x[2])], legend=[r'$\sin(x)$', r'$\cos(x)$', r'$\sqrt{x}$'], xlabel='x label', ylabel='y label')
nq.set_figstyle('my_figstyle.yaml') # User defined figstyle.
nq.plot(x, [np.sin(x[0]), np.cos(x[1]), np.sqrt(x[2])], legend=[r'$\sin(x)$', r'$\cos(x)$', r'$\sqrt{x}$'], xlabel='x label', ylabel='y label')

nq.save_all()
```
will produce the following images:

<p align="center">
  <img width="460" src="https://raw.githubusercontent.com/SengerM/nicenquickplotlib/master/doc/figstyle_doc/figures/plot1.png">
</p>
<p align="center">
  <img width="460" src="https://raw.githubusercontent.com/SengerM/nicenquickplotlib/master/doc/figstyle_doc/figures/plot2.png">
</p>
<p align="center">
  <img width="460" src="https://raw.githubusercontent.com/SengerM/nicenquickplotlib/master/doc/figstyle_doc/figures/plot3.png">
</p>
<p align="center">
  <img width="460" src="https://raw.githubusercontent.com/SengerM/nicenquickplotlib/master/doc/figstyle_doc/figures/plot4.png">
</p>

If you want to define your own *figstyle* you just have to create a [YAML](https://en.wikipedia.org/wiki/YAML) file. It is very easy. You can use the template from [this example](https://github.com/SengerM/nicenquickplotlib/tree/master/doc/figstyle_doc) or any of the [factory figstyles](https://github.com/SengerM/nicenquickplotlib/tree/master/nicenquickplotlib/figure_styles) that come with *nicenquickplotlib*. Once you have selected a figstyle, all your plots will use it.

### Plot with 'y' error bands
Call the ```plot``` function and pass to it an array of "uncertainty type objects" (see the [uncertainties](https://pythonhosted.org/uncertainties/index.html) library) to produce plots with 'y' error bands (not bars, but bands). You can see an example in the documentation (see [this link](https://github.com/SengerM/nicenquickplotlib/tree/master/doc/y_error_bars)). The figures look like this:

<p align="center">
  <img width="460" src="https://github.com/SengerM/nicenquickplotlib/blob/master/doc/y_error_bars/figures/y_error_bands.png">
</p>

<p align="center">
  <img width="460" src="https://github.com/SengerM/nicenquickplotlib/blob/master/doc/y_error_bars/figures/y_error_bands_with_blacknwhite_figstyle.png">
</p>

The code that produced those figures is
```Python
import nicenquickplotlib as nq
import uncertainties as unc # https://pythonhosted.org/uncertainties/index.html
import numpy as np

x = np.linspace(0,2,10) # Create x data.
y_vals_1 = x**2 # Create y_1 data.
y_errs_1 = y_vals_1*0.1 + np.random.rand(len(x))*0.1 # Create y_1 errors.
y_vals_2 = np.sqrt(x) # Create y_2 data.
y_errs_2 = y_vals_2*0.1 + np.random.rand(len(x))*0.1 # Create y_2 errors.
y_1 = unc.unumpy.uarray(y_vals_1, y_errs_1) # Create y_1 array of uncertainties.
y_2 = unc.unumpy.uarray(y_vals_2, y_errs_2) # Create y_2 array of uncertainties.
nq.plot(x, [y_1, y_2], title='y error bands', legend=['Data 1', 'Data 2'], marker=True)
nq.set_figstyle('blacknwhite')
nq.plot(x, [y_1, y_2], title='y error bands with blacknwhite figstyle', legend=['Data 1', 'Data 2'], marker=True)
nq.save_all(csv=True)
```

As can be seen in the example, the ```plot``` function automatically recognizes the data type and produces a plot with error bands. If you have some code that has no uncertainties and you want to add them, you only have to cast the data from *numpy array* to *unumpy array* (see [this link](https://pythonhosted.org/uncertainties/numpy_guide.html) for documentation about uncertainties in arrays).
Currently (December 2018) this is the only support for plotting with error bars. You MUST use the [uncertainties](https://pythonhosted.org/uncertainties/index.html) package and this feauture is available only for the 'y' axis.

### Functions you can use
The ```plot``` and ```save_all``` functions are the main (and usually the only) functions you have to call. The ```plot``` function is used to plot everything and the ```save_all``` function is used to... Save all! It saves all your plots in a directory, automatically. You don't have to worry to save each figure, the function does it all.

#### The ```plot``` function
You can see the source code of this function and its documentation in the file in [this link](https://github.com/SengerM/nicenquickplotlib/blob/master/nicenquickplotlib/nq_user_functions.py). The usage is very intuitive, you must pass the 'x' and 'y' data as numpy arrays. If you want to plot multiple data sets, you must provide to the plot function a list of numpy arrays containing each data set. 
Each time you call the ```plot``` function a figure is created and tracked internally by the *nicenquickplot* package. After you have made all your plots you just call once the ```save_all``` function and all your plots will be saved to files.
- ```plot``` example 1. Worry about nothing but to plot:
```Python
import numpy as np
import nicenquickplotlib as nq
x = np.linspace(0,3.14) # Create some data.
nq.plot(x, np.sin(x)) # This will be saved as plot 1.
nq.plot(np.sin(x)) # This will be saved as plot 2.
nq.plot(x, [np.sin(x), np.cos(x)]) # ... plot 3.
nq.plot([np.sin(x), np.cos(x)]) # plot 4.
x_data_list = [x, np.linspace(1,2), np.linspace(3,4)] # Create data.
y_data_list = [np.sqrt(x_data_list[0]), np.cos(x_data_list[1]), np.sin(x_data_list[2])] # Create data.
nq.plot(x_data_list, y_data_list)
nq.save_all() # Save all your plots!
```
- ```plot``` example 2. Add labels and indications:
```Python
import numpy as np
import nicenquickplotlib as nq
x = np.linspace(0,3.14) # Create some data.
y_data_sets = [np.sin(x), np.cos(x)]
labels = ['Signal 1', 'Signal 2']
nq.plot(x, y_data_sets, legend=labels, xlabel='Time (s)', ylabel='Amplitude (V)', title="I'll win the Nobel prize with this work")
nq.save_all()
```
- ```plot``` example 3. Use subplots:
```Python
import numpy as np
import nicenquickplotlib as nq
x = np.linspace(0,3.14) # Create some data.
y_data_sets = [np.sin(x), np.cos(x)]
labels = ['Signal 1', 'Signal 2']
nq.plot(x, y_data_sets, legend=labels, xlabel='Time (s)', ylabel='Amplitude (V)', together=True) # All plots in the same chart (default).
nq.plot(x, y_data_sets, legend=labels, xlabel='Time (s)', ylabel='Amplitude (V)', together=False) # Each data set is plotted in a new chart.
nq.save_all()
```
- ```plot``` example 4. Use logarithmic scales:
```Python
import numpy as np
import nicenquickplotlib as nq
x = np.logspace(0,2) # Create some data.
nq.plot(x, np.sqrt(x), xscale='l', marker='.') # Linear scale on both axes, default.
nq.plot(x, np.sqrt(x), xscale='L', marker='.') # Log scale for x axis.
nq.plot(x, np.sqrt(x), xscale='L', yscale='L', marker='.') # Log scale on both axes.
nq.save_all()
```
#### The ```save_all``` function
Its name says it all. This function saves all the plots you have made using the ```plot``` function. You can find the source code and documentation in [this link](https://github.com/SengerM/nicenquickplotlib/blob/master/nicenquickplotlib/nq_user_functions.py).
- ```save_all``` example 1. Just save all your plots:
```Python
import numpy as np
import nicenquickplotlib as nq
for k in range(10):
	nq.plot(np.linspace(0,2)**k)
nq.save_all() # Wow, you can save the 10 figures that easy!?
```
- ```save_all``` example 2. Use a timestamp in order to not override your old plots. If you request to ```save_all``` the usage of a timestamp, then it will create a new directory with a unique timestamp and the figures will be saved there. I you run the script multiple times the plots saved each time in a new directory. Code:
```Python
import numpy as np
import nicenquickplotlib as nq
nq.plot(np.linspace(0,2)**2)
nq.plot(np.linspace(0,2)**3)
nq.save_all(timestamp=True) # Use timestamp generated when 'import nicenquickplotlib as nq'
nq.save_all(timestamp='now') # Use a timestamp generated right now.
```
- ```save_all``` example 3. Use your custom directory:
```Python
import numpy as np
import nicenquickplotlib as nq
nq.plot(np.linspace(0,2)**2)
nq.plot(np.linspace(0,2)**3)
nq.save_all(mkdir='i like this directory')
```
- ```save_all``` example 4. Save the plotted data as csv files:
```Python
import numpy as np
import nicenquickplotlib as nq
nq.plot(np.linspace(0,2)**2)
nq.plot(np.linspace(0,2)**3)
nq.save_all(csv=True) # Wow, this is amazingly awesome!
```
- ```save_all``` example 5. Change the default image format. You can use any of the formats specified [here](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.savefig.html). Example code:
```Python
import numpy as np
import nicenquickplotlib as nq
nq.plot(np.linspace(0,2)**2)
nq.plot(np.linspace(0,2)**3)
nq.save_all(image_format='pdf')
```

### Accessing to the matplotlib original objects
If by some reason you want to tune your plot using the matplotlib's methods, you can access to the ```fig``` and ```ax``` objects as follows:
```Python
import numpy as np
import nicenquickplotlib as nq
x = np.linspace(0,3.14) # Create some data.
figure = nq.plot(x, [np.sqrt(x), np.sin(x)], together=False)
figure.axes[-1].set_xlabel('Distance in mega parsec')
figure.axes[0].set_ylabel('Density')
figure.axes[1].set_ylabel('Potential')
figure.fig.suptitle('Cosmic study')
nq.save_all()
```
In ```figure.axes``` there is a list containing each of the matplotlib's ```ax``` objects. In ```figure.fig``` you can find the matplotlib's ```fig``` object.
