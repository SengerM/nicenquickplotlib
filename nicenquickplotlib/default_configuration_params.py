class FigStyle:
	def __init__(self):
		self.__colors = [(1, .5, 0), (.3, .5, 1), (.3, .4, 0), (1, 0, 1)]
		self.__width = 160e-3 # Figure width in meters (size of the chart+axis_ticks, not counting legend, title, etc.).
		self.__ratio = [1, 0.6] # XY ratio aspect of figures.
		self.__hspace = 0.1 # Vertical separation between subplots.
	
	@property
	def colors(self):
		return self.__colors
	
	@property
	def width(self):
		return self.__width
	
	@property
	def ratio(self):
		return self.__ratio
	
	@property
	def hspace(self):
		return self.__hspace
	

def default_grid(ax):
	ax.grid(b=True, which='major', color='#000000', alpha=0.3, linestyle='-', linewidth=0.5)
	ax.grid(b=True, which='minor', color='#000000', alpha=0.15, linestyle='-', linewidth=0.25)
	ax.minorticks_on() # Enables minor ticks without text, only the ticks.

default_file_format = 'png'
default_save_directory = 'figures'
default_dpi_rasterization = 200 # Resolution for bitmap format.
