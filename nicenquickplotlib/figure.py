class Figure:
	"""This class is the main container of the figures created using 
	nicenquickplotlib.
	
	Attributes
	----------
	fig : matplotlib figure
		The actual figure object of the matplotlib package. You can call
		any of the "official matplotlib" methods of figures.
	axes : list
		A list with the axis objects in the figure. You can access all
		axes objects in the current figure and use any of the "official
		matplotlib" methods to modofy them. For example:
		
		my_fig = nicenquickplotlib.plot(data)
		my_fig.axes[0].set_xscale('log')
	
	__title : str
		The title of the figure.
	__xdata : list of numpy arrays
		Even if there is only one numpy array, this will be a list.
	__ydata : list of numpy arrays
		Even if there is only one numpy array, this will be a list.
	"""
	
	def __init__(self, fig, axes):
		"""
		Parameters
		----------
		fig : matplotlib figure
			The actual figure object of the matplotlib package.
		axes : list
			A list with the axis objects in the figure.
		"""
		self.fig = fig
		self.axes = axes
		self.__title = ''
		self.__xdata = None
		self.__ydata = None
	
	@property
	def title(self):
		return self.__title
	
	@title.setter
	def title(self, title):
		if not isinstance(title, str):
			title = ''
		self.__title = title
		self.fig.suptitle(title)
	
	@property
	def xdata(self):
		return self.__xdata
	
	@xdata.setter
	def xdata(self, xdata):
		if not isinstance(xdata, list):
			raise ValueError('xdata must be a list')
		self.__xdata = xdata
	
	@property
	def ydata(self):
		return self.__ydata
	
	@ydata.setter
	def ydata(self, ydata):
		if not isinstance(ydata, list):
			raise ValueError('ydata must be a list')
		self.__ydata = ydata
	
