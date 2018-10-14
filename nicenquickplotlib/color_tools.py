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
