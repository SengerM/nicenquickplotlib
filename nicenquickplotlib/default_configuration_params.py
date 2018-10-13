from numbers import Number
import yaml

def __default_grid__(ax):
	ax.grid(b=True, which='major', color='#000000', alpha=0.3, linestyle='-', linewidth=0.5)
	ax.grid(b=True, which='minor', color='#000000', alpha=0.15, linestyle='-', linewidth=0.25)
	ax.minorticks_on() # Enables minor ticks without text, only the ticks.

class FigStyle:
	def __init__(self):
		self.__colors = [(1, .5, 0), (.3, .5, 1), (.3, .4, 0), (1, 0, 1)] # List of (r,g,b) tuples containing the default plotting colors.
		self.__width = None
		self.__ratio = None
		self.__hspace = None
		self.__grid = __default_grid__
		self.read_config_file('/home/alf/nicenquickplotlib/nicenquickplotlib/figure_styles/default.yaml')
	
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
	@property
	def grid(self):
		return self.__grid
	
	def read_config_file(self, filename):
		if not isinstance(filename, str):
			raise ValueError('"file_name" must be a string')
		with open(filename, 'r') as stream:
			try:
				data = yaml.load(stream)
			except yaml.YAMLError as exc:
				print(exc)
		self.__width = 	float(data['width'])
		if isinstance(data['ratio'], list) and len(data['ratio']) == 2 and isinstance(data['ratio'][0], Number) and isinstance(data['ratio'][1], Number):
			self.__ratio = data['ratio']
		else:
			raise ValueError('Error reading "' + filename + '": ratio must be a list of two numbers [x_ratio, y_ratio]')
		self.__hspace = float(data['hspace'])


default_file_format = 'png'
default_save_directory = 'figures'
default_dpi_rasterization = 200 # Resolution for bitmap format.
