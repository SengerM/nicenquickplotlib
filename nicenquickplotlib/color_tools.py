from numbers import Number
import numpy as np

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

def get_brightness(color):
	"""
	Returns the brightness of the color normalized between 0 and 1. This
	is (r+g+b)/3.
	
	Parameters
	----------
	color : (r,g,b) tuple
	
	Returns
	-------
	float
	"""
	if not isinstance(color, tuple):
		raise TypeError('color must be a (r,g,b) tuple')
	return np.array(color).sum()/3

def change_brightness(color, brightness):
	"""
	Given a color and a brightness, returns the same color but with the
	new brightness.
	NOTE: THIS IS NOT PROPERLY IMPLEMENTED!
	
	Parameters
	----------
	color : rgb tuple
	brightness : real number between 0 and 1
	
	Returns
	-------
	rgb tuple
	"""
	if not isinstance(color, tuple):
		raise TypeError('color must be a (r,g,b) tuple')
	if not isinstance(brightness, Number):
		raise TypeError('brightness must be a number')
	if brightness < 0 or brightness > 1:
		raise ValueError('brightness must be between 0 and 1')
	newcolor = np.array(color)*brightness/get_brightness(color)
	for k in range(3):
		if newcolor[k] > 1:
			newcolor[k] = 1
	newcolor = np.array(newcolor)*brightness/get_brightness(tuple(newcolor))
	for k in range(3):
		if newcolor[k] > 1:
			newcolor[k] = 1
	return tuple(newcolor)
