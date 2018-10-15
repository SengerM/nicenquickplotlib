import numpy as np
import matplotlib.pyplot as plt
import os
from . import timestamp
from .config_types import *
from .figure import Figure
from .color_tools import hex2rgb
from .color_tools import *

# Default values -------------------------------------------------------
default_dpi_rasterization = 200 # Resolution for bitmap format.
# Do not touch this ----------------------------------------------------
__figs_list = []
__session_timestamp = timestamp.get_timestamp()
__nq_instalation_path = os.path.dirname(os.path.abspath(__file__))
# ----------------------------------------------------------------------

def set_figstyle(figstyle):
	"""Change the current figstyle.
	Parameters
	----------
	figstyle : string
		Specifies which figstyle file to load.
	
	Examples
	-------
	set_figstyle('default')
	set_figstyle('blacknwhite')
	set_figstyle(path_to_my_figstyle_file)
	"""
	global __figstyle
	if figstyle is 'default':
		__figstyle = FigStyle(__nq_instalation_path + '/figure_styles/' + 'default.yaml')
	elif figstyle is 'blacknwhite':
		__figstyle = FigStyle(__nq_instalation_path + '/figure_styles/' + 'blacknwhite.yaml')
	else:
		raise ValueError('Not yet implemented!')

set_figstyle('default')

def __validate_data_and_generate_lists(x, y=None):
	"""
	This function is used internally to validate the (x,y) input data.
	Currently it is used only by the "plot" function.
	"""
	xx = []
	yy = []
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
	return xx,yy

def plot(x, y=None, xlabel=None, ylabel=None, legend=None, title=None, 
	together=True, xscale='', yscale='', linestyle=None, color=None, marker=None, *args, **kwargs):
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
	linestyle : same as in matplotlib or a list, optional
		If not specified then the current figstyle linestyles are used.
	color : same as in matplotlib or a list, optional
		If not specified then the current figstyle colors are used.
	markers : bool or string or list of strings, optional
		If False --> plot with no markers.
		If True --> plot with current figstyle markers.
		If a string --> the specified marker is used for all plots.
		If a list of stings --> each data set uses each marker.
		Default is False.
	
	Returns
	-------
	Figure
		An instance of the Figure class.
	"""
	xx,yy = __validate_data_and_generate_lists(x,y)
	# Create the matplotlib objects ------------------------------------
	if together is False:
		f, ax = plt.subplots(len(yy), sharex=True, figsize=(__figstyle.width*__figstyle.ratio[0]/25.4e-3, __figstyle.width*__figstyle.ratio[1]/25.4e-3))
		f.subplots_adjust(hspace=__figstyle.hspace)
		axes = ax
	else:
		f, ax = plt.subplots(1, figsize=(__figstyle.width*__figstyle.ratio[0]/25.4e-3, __figstyle.width*__figstyle.ratio[1]/25.4e-3))
		axes = []
		for k in range(len(yy)):
			axes.append(ax)
	# Create the Figure object for the current figure ------------------
	current_fig = Figure(f, axes)
	__figs_list.append(current_fig)
	current_fig.xdata = xx
	current_fig.ydata = yy
	if __figstyle.main_color is not None:
		current_fig.set_title(title, color=__figstyle.main_color)
	else:
		current_fig.set_title(title)
	# Configure linestyle ----------------------------------------------
	if linestyle is None:
		linestyles = __figstyle.linestyles
	else:
		if isinstance(linestyle, str):
			linestyles = [linestyle]
		elif isinstance(linestyle, list):
			linestyles = linestyle
		else:
			raise ValueError('Cannot understand what you passed as "linestyle"')
	# Configure line colors --------------------------------------------
	if color is None:
		colors = __figstyle.colors
	elif isinstance(color, str):
		colors = [color]
	elif isinstance(color, list):
		colors = color
	# Configure markers ------------------------------------------------
	if marker is None:
		markers = [None]
	else:
		if marker is True:
			markers = __figstyle.markers
		elif isinstance(marker, str):
			markers = [marker]
		elif isinstance(marker, list):
			markers = marker
		else:
			raise ValueError('Cannot understand what you passed as "marker"...')
	# Plot -------------------------------------------------------------
	for k in range(len(yy)):
		axes[k].plot(xx[k], yy[k], color=colors[k%len(__figstyle.colors)], linestyle=linestyles[k%len(linestyles)], marker=markers[k%len(markers)], *args, **kwargs)
		__figstyle.grid(axes[k])
		# Configure legend ---------------------------------------------
		if legend is not None:
			if isinstance(legend, str):
				legend = [legend]
			if len(legend) != len(yy):
				raise ValueError('I have received ' + str(len(yy)) + ' data sets and ' + str(len(legend)) + ' legend labels...')
			if together is True:
				leg = axes[k].legend(legend)
			else:
				leg = axes[k].legend([legend[k]], frameon=False)
			leg.get_frame().set_linewidth(0)
			if __figstyle.main_color is not None:
				for text in leg.get_texts():
					text.set_color(__figstyle.main_color)
		# Configure axes colors ----------------------------------------
		if __figstyle.main_color is not None:
			axes[k].spines['bottom'].set_color(__figstyle.main_color)
			axes[k].spines['top'].set_color(__figstyle.main_color)
			axes[k].spines['left'].set_color(__figstyle.main_color)
			axes[k].spines['right'].set_color(__figstyle.main_color)
			axes[k].xaxis.label.set_color(__figstyle.main_color)
			axes[k].yaxis.label.set_color(__figstyle.main_color)
			axes[k].tick_params(which='major', axis='both', colors=__figstyle.main_color)
			axes[k].tick_params(which='minor', axis='both', colors=__figstyle.main_color)
		# Configure y labels -------------------------------------------
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
		# Configure sacles ---------------------------------------------	
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
	"""This is the same as  matplotlib's plt.show()"""
	plt.show()

def save_all(timestamp=False, mkdir='figures', csv=False, image_format='png'):
	"""
	Calling this function will save all plots created with 
	nicenquickplotlib.
	
	Arguments
	---------
	timestamp : bool, optional
		If true then all file names will be identified with one (and the
		same) timestamp. This is usefull when you want not to overwrite
		the plots each time you run your code.
		Default value is False.
	mkdir : str or None, optional
		If a string is passed then a directory will be created (with the
		specified name) and all figures will be saved in there. If None
		all figures will be saved in the current working directory.
		Default value is 'figures'.
	csv : bool, optional
		If true then a csv file is created along with each image file 
		containing the data that is plotted.
	image_format : string, optional
		Format of image files. Default is 'png'. 
	"""
	if mkdir is not None:
		directory = mkdir + '/'
	else:
		directory = ''
	if timestamp is True:
		directory += __session_timestamp
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
		
		__figs_list[k].fig.savefig(directory + '/' + file_name + '.' + image_format, dpi=default_dpi_rasterization, bbox_inches='tight')
		
		if csv is True:
			for l in range(len(__figs_list[k].ydata)):
				np.savetxt(directory + '/' + file_name + '_' + 'dataset' + str(l+1) + '.csv', np.array([__figs_list[k].xdata[l],__figs_list[k].ydata[l]]).transpose(), header='x\ty')
