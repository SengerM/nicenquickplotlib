import numpy as np
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
