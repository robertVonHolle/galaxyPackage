from galaxy import galaxy
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import time
import numpy as np

def densityPlot(galaxies, f, xlim=None, ylim=None):
	r"""
	Creates a 2d histogram of galaxies with color on the x-axis and absolute magnitude
	on the y-axis

	Parameters
		galaxies - Type: dict. A dictionary of galaxy objects to be plotted
		f - Type: str. The name of the plot's output file
		xlim (optional) - Type: list. The bounds of the x axis
		ylim (optional) - Type: list. The bounds of the y axis
	
	Returns nothing but prints the plot to the specified output file.
	"""
	errFlag = -9999  # SDSS u-band error flag
	galaxyList = list(galaxies.values())
	color = []
	Mr = []

	# Create lists to use for plotting
	for galaxy in galaxyList:
		if galaxy.u > errFlag:
			color.append(galaxy.color)
			Mr.append(galaxy.Mr)

	Mr_div = np.linspace(min(Mr), max(Mr), 1000)
	Mr_21 = Mr_div + 21
	color_div = -0.018*(Mr_21**2) - 0.137*Mr_21 + 2.20

	# Create the 2d histogram
	plt.hist2d(color, Mr, bins=250, norm=LogNorm(), cmin=1, cmap=plt.cm.inferno)
	plt.gca().invert_yaxis()
	plt.title("Color vs. Absolute Magnitude", fontsize=14)
	plt.xlabel("Color (u - r)", fontsize=14)
	plt.ylabel("Absolute Magnitude", fontsize=14)

	# Implement plot limits if requested by user
	if xlim != None:
		if type(xlim) == list:
			if len(xlim) == 2:
				plt.xlim(min(xlim),max(xlim))
			else:
				raise ValueError("Argument 'xlim' must be a list of length 2. Got list of length %s" % (len(xlim)))
		else:
			raise TypeError("Argument 'xlim' must be a list of length 2. Got: %s" % (type(xlim)))

	if ylim != None:
		if type(ylim) == list:
			if len(ylim) == 2:
				plt.ylim(max(ylim),min(ylim))
			else:
				raise ValueError("Argument 'ylim' must be a list of length 2. Got list of length %s" % (len(ylim)))
		else:
			raise TypeError("Argument 'ylim' must be a list of length 2. Got: %s" % (type(ylim)))
	
	plt.colorbar()
	plt.plot(color_div, Mr_div)
	plt.savefig(f)
	print("Created galaxy plot")
	plt.clf()
