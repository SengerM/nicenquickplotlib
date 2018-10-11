import numpy as np
import matplotlib.pyplot as plt
import os
from . import timestamp
from .default_configuration_params import *
from .figure import Figure

# Do not touch this ----------------
__figs_list = []
__session_timestamp = timestamp.get_timestamp()
# ----------------------------------

def plot(x, y=None, xlabel=None, ylabel=None, legend=None, title=None, 
	together=True, xscale='', yscale='', *args, **kwargs):
	"""This is the function you have to use to produce a nice and quick plot.
	
	Arguments
	---------
	x : numpy array
		If 'y' is not provided, the 'x' argument must be a numpy array
		containing the data or a list of numpy arrays to plot. In this 
		case the data in 'x' is ploted in the y axis and the x
		axis is the "number of element in the array".
		If 'y' data is providen then:
			1) If 'x' is a numpy array it is used to plot all 'y' data
			sets.
			2) If 'x' is a list of numpy arrays each is used with each
			'y' data set.
	y : numpy array or list of numpy arrays, optional
		y values to plot. 
	xlabel : string, optional
		String containing the label for the x axis.
	ylabel : string or list of strings, optional
		String or list of strings containing the labels for the y axes.
	legend : string or list of strings, optional
		Labels to be put in the legend. Passing data_labels automatically
		enables the legend.
	title : string, optional
		Title of the figure.
	together : bool, optional
		If together is True then only one plot is placed in the figure
		and all data is plotted in this plot.
		If together is False then each set of data is plotted in a different
		subplot. Note that all the subplots will share the same x axis.
		Default value is True.
	xscale : string, optional
		'l' means linear.
		'L' means log.
	yscale : string, optional
		See 'xscale' for reference. If multiple subplots are configured
		then 'yscale' can be a string containing one character for each
		of the subplots. For example
		
		niceandquickplotlib.plot(x, [y1,y2], yscale='Ll')
		
		will produce a log scale for y1 and a linear scale for y2.
	
	Returns
	-------
	Figure
		A nicenquickplotlib type Figure object.
	"""
	
	xx = [] # This is what will actually be plotted.
	yy = [] # This is what will actually be plotted.
	# Validation of data ---------------
	if y is None:
		if isinstance(x, np.ndarray): # This means there is only one data set to plot. Otherwise I would expect a list of numpy arrays.
			yy.append(x);
		elif isinstance(x, list):
			yy = x
		for k in range(len(yy)):
			xx.append(np.arange(len(yy[k])))
	elif isinstance(y, np.ndarray):
		if not isinstance(x, np.ndarray):
			raise ValueError('I have received a numpy array with "y" data but "x" data is not a numpy array')
		xx.append(x)
		yy.append(y)
	elif isinstance(y, list):
		yy = y
		if isinstance(x, list):
			if len(y) != len(x):
				raise ValueError('Different number of data sets received with "x" data and "y" data')
			xx = x
		if isinstance(x, np.ndarray):
			for k in range(len(yy)):
				xx.append(x)
	else:
		raise ValueError('"y" must be a numpy array with data, or a list containing numpy arrays')
	if not legend is None:
		if isinstance(legend, str):
			if len(yy) == 1:
				legend = [legend]
			else:
				if len(yy) > 1:
					temp = legend
					legend = []
					for k in range(len(yy)):
						legend.append(temp)
		elif isinstance(legend, list):
			if len(legend) != len(yy):
				raise ValueError('Number of legend must be equal to number of "y" datasets')
		else:
			raise ValueError('Cannot recognize "legend" object')
	# Create the matplotlib objects ----------------------
	if together is False:
		f, ax = plt.subplots(len(yy), sharex=True, figsize=(default_fig_width*default_fig_ratio[0]/25.4e-3, default_fig_width*default_fig_ratio[1]/25.4e-3))
		f.subplots_adjust(hspace=default_hspace)
		axes = ax
	else:
		f, ax = plt.subplots(1, figsize=(default_fig_width*default_fig_ratio[0]/25.4e-3, default_fig_width*default_fig_ratio[1]/25.4e-3))
		axes = []
		for k in range(len(yy)):
			axes.append(ax)
	# Create the Figure object for the current figure ----
	current_fig = Figure(f, axes)
	__figs_list.append(current_fig)
	current_fig.title = title
	current_fig.xdata = xx
	current_fig.ydata = yy
	# Plot -----------------------------------------------
	for k in range(len(yy)):
		axes[k].plot(xx[k], yy[k], color=default_colors[k], *args, **kwargs)
		default_grid(axes[k])
		if not legend is None:
			if together is True:
				axes[k].legend(legend)
			else:
				axes[k].legend([legend[k]])
		if ylabel is not None:
			if isinstance(ylabel, list):
				axes[k].set_ylabel(ylabel[k])
			else:
				axes[k].set_ylabel(ylabel)
		if xlabel != None:
			axes[-1].set_xlabel(xlabel)
		if len(yscale) > k:
			if yscale[k] is 'l':
				axes[k].set_yscale('linear')
			if yscale[k] is 'L':
				axes[k].set_yscale('log')
	if 'l' in xscale:
		axes[0].set_xscale('linear')
	if 'L' in xscale:
		axes[0].set_xscale('log')
	if len(yscale) == 1:
		for k in range(len(axes)):
			if yscale[0] is 'l':
				axes[k].set_yscale('linear')
			if yscale[0] is 'L':
				axes[k].set_yscale('log')
	return current_fig
	
def show():
	"""This is the same as 'plt.show()'"""
	plt.show()

def save_all(timestamp=False, mkdir=True, csv=False):
	"""Calling this function will save all plots created with 
	nicenquickplotlib
	
	Arguments
	---------
	timestamp : bool, optional
		If true then all file names will be identified with one (and the
		same) timestamp. This is usefull when you want not to overwrite
		the plots each time you run your code.
		Default value is False.
	mkdir : bool, optional
		If true then a directory will be created (with name specified
		by the 'default_save_directory' variable) and all figures will
		be saved in there. If fallse all figures will be saved in the 
		current working directory.
		Default value is True.
	csv : bool, optional
		If true then a csv file is created along with each image file 
		containing the data that is plotted.
	"""
	if mkdir is True:
		if timestamp is False:
			directory = default_save_directory
		else:
			directory = __session_timestamp
		if not os.path.exists(directory):
			os.makedirs(directory)
	for k in range(len(__figs_list)):
		file_name = ''
		if timestamp is True:
			file_name += __session_timestamp + '_'
		if __figs_list[k].title is '':
			file_name += 'plot' + str(k+1)
		else:
			file_name += __figs_list[k].title
		file_name = file_name.replace(' ','_').lower()
		
		__figs_list[k].fig.savefig(directory + '/' + file_name + '.' + default_file_format, dpi=default_dpi_rasterization, bbox_inches='tight')
		
		if csv is True:
			for l in range(len(__figs_list[k].ydata)):
				np.savetxt(directory + '/' + file_name + '_' + 'dataset' + str(l+1) + '.csv', np.array([__figs_list[k].xdata[l],__figs_list[k].ydata[l]]).transpose(), header='x\ty')
