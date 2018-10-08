import numpy as np
import matplotlib.pyplot as plt
import timestamp
import os

# Configure your plots -------------
default_file_format = 'png'
default_save_directory = 'figures'
default_colors = np.array([(255, 102, 0), (51, 153, 255), (51, 102, 0), (255, 0, 255)])/255
default_fig_width = 160e-3 # Figure width in meters (size of the chart+axis_ticks, not counting legend, title, etc.).
default_fig_ratio = [1, 0.6] # XY ratio aspect of figures.
default_hspace = 0.1 # Vertical separation between subplots.
default_dpi_rasterization = 200 # Resolution for bitmap format.
def default_grid(ax):
	ax.grid(b=True, which='major', color='#000000', alpha=0.3, linestyle='-', linewidth=0.5)
	ax.grid(b=True, which='minor', color='#000000', alpha=0.15, linestyle='-', linewidth=0.25)
	ax.minorticks_on() # Enables minor ticks without text, only the ticks.
# ----------------------------------
__figs_list = []
__session_timestamp = timestamp.get_timestamp()
# ----------------------------------

class Figure:
	def __init__(self, fig, axes):
		self.__title = ''
		self.fig = fig
		self.axes = axes
	
	@property
	def title(self):
		return self.__title
	
	@title.setter
	def title(self, title):
		if not isinstance(title, str):
			title = ''
		self.__title = title
		self.fig.suptitle(title)
	
def plot(x, y=None, xlabel=None, ylabel=None, data_labels=None, title=None, together=True, *args, **kwargs):
	xx = [] # This is what will actually be plotted.
	yy = [] # This is what will actually be plotted.
	
	if y is None:
		if isinstance(x, np.ndarray): # This means there is only one data set to plot. Otherwise I would expect a list of numpy arrays.
			yy.append(x);
		elif isinstance(x, list):
			yy = x
		for k in range(len(yy)):
			xx.append(np.arange(len(yy[k])))
	elif isinstance(y, np.ndarray):
		xx.append(x)
		yy.append(y)
	elif isinstance(y, list):
		yy = y
		if not isinstance(x, np.ndarray):
			raise ValueError('"x" data must be providen in a numpy array')
		for k in range(len(yy)):
			xx.append(x)
	else:
		raise ValueError('"y" must be a numpy array with data, or a list containing numpy arrays')
	
	
	if together is False:
		f, ax = plt.subplots(len(yy), sharex=True, figsize=(default_fig_width*default_fig_ratio[0]/25.4e-3, default_fig_width*default_fig_ratio[1]/25.4e-3))
		f.subplots_adjust(hspace=default_hspace)
		axes = ax
	else:
		f, ax = plt.subplots(1, figsize=(default_fig_width*default_fig_ratio[0]/25.4e-3, default_fig_width*default_fig_ratio[1]/25.4e-3))
		axes = [ax]
	
	current_fig = Figure(f, axes)
	__figs_list.append(current_fig)
	current_fig.title = title
	
	for k in range(len(axes)):
		axes[k].plot(xx[k], yy[k], color=default_colors[k], *args, **kwargs)
		default_grid(axes[k])
		if data_labels != None:
			axes[k].legend()
		if ylabel is not None:
			if isinstance(ylabel, list):
				axes[k].set_ylabel(ylabel[k])
			else:
				axes[k].set_ylabel(ylabel)
		if xlabel != None:
			axes[-1].set_xlabel(xlabel)
	
	return current_fig
	
	
def show():
	plt.show()

def save_all(timestamp=False, mkdir=True):
	for k in range(len(__figs_list)):
		file_name = ""
		if mkdir is True:
			if timestamp is False:
				directory = default_save_directory
			else:
				directory = __session_timestamp
			if not os.path.exists(directory):
				os.makedirs(directory)
			file_name += directory + '/'
		if timestamp is True:
			file_name += __session_timestamp + '_'
		if __figs_list[k].title is '':
			file_name += str(k+1) + '_'
		else:
			file_name += __figs_list[k].title
		file_name += '.' + default_file_format
		file_name = file_name.replace(' ','_').lower()
		
		__figs_list[k].fig.savefig(file_name, dpi=default_dpi_rasterization)

