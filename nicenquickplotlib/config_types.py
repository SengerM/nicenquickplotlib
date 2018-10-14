from numbers import Number
import yaml

def hex2rgb(hexstr):
	"""Converts a hex "#rrggbb" color string code to a tuble of (r,g,b)"""
	if not isinstance(hexstr, str):
		raise ValueError('I was expecting a string with the hex code color')
	if hexstr[0] is not '#':
		raise ValueError('Invalid hex color code: missing "#" at the begining')
	if len(hexstr) is not 7:
		raise ValueError('Invalid hex color code: length of the string code is not 7')
	hexstr = hexstr[1:]
	return tuple(int(hexstr[i:i+2], 16)/255 for i in (0, 2 ,4)) # Taken from https://stackoverflow.com/a/29643643/8849755

def __default_grid__(ax):
	"""This is a temporary function"""
	ax.grid(b=True, which='major', color='#000000', alpha=0.3, linestyle='-', linewidth=0.5)
	ax.grid(b=True, which='minor', color='#000000', alpha=0.15, linestyle='-', linewidth=0.25)
	ax.minorticks_on() # Enables minor ticks without text, only the ticks.

class FigStyle:
	def __init__(self, config_file):
		self.__width = None
		self.__ratio = None
		self.__hspace = None
		self.__colors = [None]
		self.__linestyles = [None]
		self.__markers = [None]
		self.__grid = __default_grid__
		self.__main_color = None
		
		self.read_config_file(config_file) # This is what actually initializes the values.
	
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
	@property
	def linestyles(self):
		return self.__linestyles
	@property
	def markers(self):
		return self.__markers
	@property
	def main_color(self):
		return self.__main_color
	
	def read_config_file(self, filename):
		if not isinstance(filename, str):
			raise ValueError('"file_name" must be a string')
		with open(filename, 'r') as stream:
			try:
				data = yaml.load(stream)
			except yaml.YAMLError as exc:
				print(exc)
		
		if 'width' not in data:
			raise ValueError('The "figstyle" file must have a "width" field')
		self.__width = 	float(data['width'])
		
		if 'ratio' not in data:
			raise ValueError('The "figstyle" file must have a "ratio" field')
		if isinstance(data['ratio'], list) and len(data['ratio']) == 2 and isinstance(data['ratio'][0], Number) and isinstance(data['ratio'][1], Number):
			self.__ratio = data['ratio']
		else:
			raise ValueError('Error reading "' + filename + '": ratio must be a list of two numbers [x_ratio, y_ratio]')
		
		if 'hspace' not in data:
			raise ValueError('The "figstyle" file must have a "hspace" field')
		self.__hspace = float(data['hspace'])
		
		if isinstance(data['colors'], list):
			self.__colors = [None]*len(data['colors'])
			for k in range(len(data['colors'])):
				self.__colors[k] = hex2rgb(data['colors'][k])
		
		if 'linestyles' in data:
			if isinstance(data['linestyles'], list):
				self.__linestyles = data['linestyles']
		
		if 'markers' in data:
			if isinstance(data['markers'], list):
				self.__markers = data['markers']
		
		if 'main_color' in data:
			if isinstance(data['main_color'], str):
				self.__main_color = data['main_color']

default_file_format = 'png'
default_save_directory = 'figures'
default_dpi_rasterization = 200 # Resolution for bitmap format.

