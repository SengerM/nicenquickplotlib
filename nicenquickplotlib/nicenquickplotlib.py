# ~ import numpy as np
# ~ import matplotlib.pyplot as plt
# ~ import os

# ~ from . import timestamp

# ~ # Configure your plots -------------
# ~ default_file_format = 'png'
# ~ default_save_directory = 'figures'
# ~ default_colors = np.array([(255, 102, 0), (51, 153, 255), (51, 102, 0), (255, 0, 255)])/255
# ~ default_fig_width = 160e-3 # Figure width in meters (size of the chart+axis_ticks, not counting legend, title, etc.).
# ~ default_fig_ratio = [1, 0.6] # XY ratio aspect of figures.
# ~ default_hspace = 0.1 # Vertical separation between subplots.
# ~ default_dpi_rasterization = 200 # Resolution for bitmap format.
# ~ def default_grid(ax):
	# ~ ax.grid(b=True, which='major', color='#000000', alpha=0.3, linestyle='-', linewidth=0.5)
	# ~ ax.grid(b=True, which='minor', color='#000000', alpha=0.15, linestyle='-', linewidth=0.25)
	# ~ ax.minorticks_on() # Enables minor ticks without text, only the ticks.
# ~ # Do not touch this ----------------
# ~ __figs_list = []
# ~ __session_timestamp = timestamp.get_timestamp()
# ~ # ----------------------------------

# ~ class Figure:
	# ~ """This class is the main container of the figures created using 
	# ~ nicenquickplotlib.
	
	# ~ Attributes
	# ~ ----------
	# ~ __title : str
		# ~ The title of the figure.
	# ~ fig : matplotlib figure
		# ~ The actual figure object of the matplotlib package. You can call
		# ~ any of the "official matplotlib" methods of figures.
	# ~ axes : list
		# ~ A list with the axis objects in the figure. You can access all
		# ~ axes objects in the current figure and use any of the "official
		# ~ matplotlib" methods to modofy them. For example:
		
		# ~ my_fig = nicenquickplotlib.plot(data)
		# ~ my_fig.axes[0].set_xscale('log')
	# ~ """
	
	# ~ def __init__(self, fig, axes):
		# ~ """
		# ~ Parameters
		# ~ ----------
		# ~ fig : matplotlib figure
			# ~ The actual figure object of the matplotlib package.
		# ~ axes : list
			# ~ A list with the axis objects in the figure.
		# ~ """
		# ~ self.__title = ''
		# ~ self.fig = fig
		# ~ self.axes = axes
	
	# ~ @property
	# ~ def title(self):
		# ~ return self.__title
	
	# ~ @title.setter
	# ~ def title(self, title):
		# ~ if not isinstance(title, str):
			# ~ title = ''
		# ~ self.__title = title
		# ~ self.fig.suptitle(title)
	
# ~ def plot(x, y=None, xlabel=None, ylabel=None, data_labels=None, title=None, 
	# ~ together=True, xscale='', yscale='', *args, **kwargs):
	# ~ """This is the function you have to use to produce a nice and quick plot.
	
	# ~ Arguments
	# ~ ---------
	# ~ x : numpy array
		# ~ If 'y' is not provided, the 'x' argument must be a numpy array
		# ~ containing the data or a list of numpy arrays to plot. In this 
		# ~ case the data in 'x' is ploted in the y axis and the x
		# ~ axis is the "number of element in the array".
		# ~ If 'y' data is providen then:
			# ~ 1) If 'x' is a numpy array it is used to plot all 'y' data
			# ~ sets.
			# ~ 2) If 'x' is a list of numpy arrays each is used with each
			# ~ 'y' data set.
	# ~ y : numpy array or list of numpy arrays, optional
		# ~ y values to plot. 
	# ~ xlabel : string, optional
		# ~ String containing the label for the x axis.
	# ~ ylabel : string or list of strings, optional
		# ~ String or list of strings containing the labels for the y axes.
	# ~ data_labels : string or list of strings, optional
		# ~ Labels to be put in the legend. Passing data_labels automatically
		# ~ enables the legend.
	# ~ title : string, optional
		# ~ Title of the figure.
	# ~ together : bool, optional
		# ~ If together is True then only one plot is placed in the figure
		# ~ and all data is plotted in this plot.
		# ~ If together is False then each set of data is plotted in a different
		# ~ subplot. Note that all the subplots will share the same x axis.
		# ~ Default value is True.
	# ~ xscale : string, optional
		# ~ 'l' means linear.
		# ~ 'L' means log.
	# ~ yscale : string, optional
		# ~ See 'xscale' for reference. If multiple subplots are configured
		# ~ then 'yscale' can be a string containing one character for each
		# ~ of the subplots. For example
		
		# ~ niceandquickplotlib.plot(x, [y1,y2], yscale='Ll')
		
		# ~ will produce a log scale for y1 and a linear scale for y2.
	
	# ~ Returns
	# ~ -------
	# ~ Figure
		# ~ A nicenquickplotlib type Figure object.
	# ~ """
	
	# ~ xx = [] # This is what will actually be plotted.
	# ~ yy = [] # This is what will actually be plotted.
	
	# ~ if y is None:
		# ~ if isinstance(x, np.ndarray): # This means there is only one data set to plot. Otherwise I would expect a list of numpy arrays.
			# ~ yy.append(x);
		# ~ elif isinstance(x, list):
			# ~ yy = x
		# ~ for k in range(len(yy)):
			# ~ xx.append(np.arange(len(yy[k])))
	# ~ elif isinstance(y, np.ndarray):
		# ~ if not isinstance(x, np.ndarray):
			# ~ raise ValueError('I have received a numpy array with "y" data but "x" data is not a numpy array')
		# ~ xx.append(x)
		# ~ yy.append(y)
	# ~ elif isinstance(y, list):
		# ~ yy = y
		# ~ if isinstance(x, list):
			# ~ if len(y) != len(x):
				# ~ raise ValueError('Different number of data sets received with "x" data and "y" data')
			# ~ xx = x
		# ~ if isinstance(x, np.ndarray):
			# ~ for k in range(len(yy)):
				# ~ xx.append(x)
	# ~ else:
		# ~ raise ValueError('"y" must be a numpy array with data, or a list containing numpy arrays')
	
	
	# ~ if together is False:
		# ~ f, ax = plt.subplots(len(yy), sharex=True, figsize=(default_fig_width*default_fig_ratio[0]/25.4e-3, default_fig_width*default_fig_ratio[1]/25.4e-3))
		# ~ f.subplots_adjust(hspace=default_hspace)
		# ~ axes = ax
	# ~ else:
		# ~ f, ax = plt.subplots(1, figsize=(default_fig_width*default_fig_ratio[0]/25.4e-3, default_fig_width*default_fig_ratio[1]/25.4e-3))
		# ~ axes = []
		# ~ for k in range(len(yy)):
			# ~ axes.append(ax)
	
	# ~ current_fig = Figure(f, axes)
	# ~ __figs_list.append(current_fig)
	# ~ current_fig.title = title
	
	# ~ for k in range(len(yy)):
		# ~ axes[k].plot(xx[k], yy[k], color=default_colors[k], *args, **kwargs)
		# ~ default_grid(axes[k])
		# ~ if data_labels != None:
			# ~ axes[k].legend()
		# ~ if ylabel is not None:
			# ~ if isinstance(ylabel, list):
				# ~ axes[k].set_ylabel(ylabel[k])
			# ~ else:
				# ~ axes[k].set_ylabel(ylabel)
		# ~ if xlabel != None:
			# ~ axes[-1].set_xlabel(xlabel)
		# ~ if len(yscale) > k:
			# ~ if yscale[k] is 'l':
				# ~ axes[k].set_yscale('linear')
			# ~ if yscale[k] is 'L':
				# ~ axes[k].set_yscale('log')
			
	# ~ if 'l' in xscale:
		# ~ axes[0].set_xscale('linear')
	# ~ if 'L' in xscale:
		# ~ axes[0].set_xscale('log')
	# ~ if len(yscale) == 1:
		# ~ for k in range(len(axes)):
			# ~ if yscale[0] is 'l':
				# ~ axes[k].set_yscale('linear')
			# ~ if yscale[0] is 'L':
				# ~ axes[k].set_yscale('log')
	
	# ~ return current_fig
	
# ~ def show():
	# ~ """This is the same as 'plt.show()'"""
	# ~ plt.show()

# ~ def save_all(timestamp=False, mkdir=True):
	# ~ """Calling this function will save all plots created with 
	# ~ nicenquickplotlib
	
	# ~ Arguments
	# ~ ---------
	# ~ timestamp : bool, optional
		# ~ If true then all file names will be identified with one (and the
		# ~ same) timestamp. This is usefull when you want not to overwrite
		# ~ the plots each time you run your code.
		# ~ Default value is False.
	# ~ mkdir : bool, optional
		# ~ If true then a directory will be created (with name specified
		# ~ by the 'default_save_directory' variable) and all figures will
		# ~ be saved in there. If fallse all figures will be saved in the 
		# ~ current working directory.
		# ~ Default value is True.
	# ~ """
	# ~ for k in range(len(__figs_list)):
		# ~ file_name = ""
		# ~ if mkdir is True:
			# ~ if timestamp is False:
				# ~ directory = default_save_directory
			# ~ else:
				# ~ directory = __session_timestamp
			# ~ if not os.path.exists(directory):
				# ~ os.makedirs(directory)
			# ~ file_name += directory + '/'
		# ~ if timestamp is True:
			# ~ file_name += __session_timestamp + '_'
		# ~ if __figs_list[k].title is '':
			# ~ file_name += str(k+1) + '_'
		# ~ else:
			# ~ file_name += __figs_list[k].title
		# ~ file_name += '.' + default_file_format
		# ~ file_name = file_name.replace(' ','_').lower()
		
		# ~ __figs_list[k].fig.savefig(file_name, dpi=default_dpi_rasterization, bbox_inches='tight')