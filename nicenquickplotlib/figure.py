class Figure:
	"""This class is the main container of the figures created using 
	nicenquickplotlib.
	
	Attributes
	----------
	__title : str
		The title of the figure.
	fig : matplotlib figure
		The actual figure object of the matplotlib package. You can call
		any of the "official matplotlib" methods of figures.
	axes : list
		A list with the axis objects in the figure. You can access all
		axes objects in the current figure and use any of the "official
		matplotlib" methods to modofy them. For example:
		
		my_fig = nicenquickplotlib.plot(data)
		my_fig.axes[0].set_xscale('log')
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
