from galaxy import galaxy
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm
from scipy.stats import ks_2samp

def colorNearHist(galaxies, f):
	r"""
	Creates a 2d histogram of galaxies with color on the x-axis and
	number of nearby neighbors on the y-axis

	Parameters
		galaxies - Type: dict. A dictionary of galaxy objects to be plotted
		f - Type: str. The name of the plot's output file

	Returns none but prints two plots to the specified output files.
	"""

	errFlag = -9999
	galaxyList = list(galaxies.values())
	color = [galaxy.color for galaxy in galaxyList if galaxy.color > errFlag]
	colorSmall = [galaxy.color for galaxy in galaxyList if galaxy.color > errFlag and galaxy.agn > 0]
	colorSmall2 = [galaxy.color for galaxy in galaxyList if galaxy.color > errFlag and galaxy.agn == 0]
	numNear = [galaxy.nearby for galaxy in galaxyList if galaxy.color > errFlag]
	numNearSmall = [galaxy.nearby for galaxy in galaxyList if galaxy.color > errFlag and galaxy.agn > 0]
	numNearSmall2 = [galaxy.nearby for galaxy in galaxyList if galaxy.color > errFlag and galaxy.agn == 0]

	plt.hist2d(colorSmall2, numNearSmall2, bins=100, norm=LogNorm(), cmin=1, cmap=plt.cm.inferno)
	plt.title("Color vs. Number of Neighbors", fontsize=14)
	plt.xlabel("Color (u - r)", fontsize=14)
	plt.ylabel("Number of nearby neighbors", fontsize=14)
	plt.colorbar()
	plt.savefig(f + 'NoAGN.png')
	print("Created near hist 1")

	plt.hist2d(colorSmall, numNearSmall, bins=100, norm=LogNorm(), cmin=1, cmap=plt.cm.inferno)
	plt.savefig(f + 'AGNonly.png')
	print("Created near hist 2")
	plt.clf()

	colorZeroes = [galaxy.color for galaxy in galaxyList if galaxy.color > errFlag and galaxy.agn > 0 and galaxy.nearby == 0]
	colorZeroes2 = [galaxy.color for galaxy in galaxyList if galaxy.color > errFlag and galaxy.agn == 0 and galaxy.nearby == 0]
	colorOnes = [galaxy.color for galaxy in galaxyList if galaxy.color > errFlag and galaxy.agn > 0 and galaxy.nearby == 1]
	colorOnes2 = [galaxy.color for galaxy in galaxyList if galaxy.color > errFlag and galaxy.agn == 0 and galaxy.nearby == 1]
	colorTwos = [galaxy.color for galaxy in galaxyList if galaxy.color > errFlag and galaxy.agn > 0 and galaxy.nearby == 2]
	colorTwos2 = [galaxy.color for galaxy in galaxyList if galaxy.color > errFlag and galaxy.agn == 0 and galaxy.nearby == 2]
	colorThrees = [galaxy.color for galaxy in galaxyList if galaxy.color > errFlag and galaxy.agn > 0 and galaxy.nearby == 3]
	colorThrees2 = [galaxy.color for galaxy in galaxyList if galaxy.color > errFlag and galaxy.agn == 0 and galaxy.nearby == 3]
	colorFours = [galaxy.color for galaxy in galaxyList if galaxy.color > errFlag and galaxy.agn > 0 and galaxy.nearby == 4]
	colorFours2 = [galaxy.color for galaxy in galaxyList if galaxy.color > errFlag and galaxy.agn == 0 and galaxy.nearby == 4]

#	print("Color KS Test:", ks_2samp(np.array(colorSmall), np.array(colorSmall2)))
#	print("NumNear KS Test:", ks_2samp(np.array(numNearSmall), np.array(numNearSmall2)))
	print("KS Test 0:", ks_2samp(np.array(colorZeroes), np.array(colorZeroes2)))
	print("KS Test 1:", ks_2samp(np.array(colorOnes), np.array(colorOnes2)))
	print("KS Test 2:", ks_2samp(np.array(colorTwos), np.array(colorTwos2)))
	print("KS Test 3:", ks_2samp(np.array(colorThrees), np.array(colorThrees2)))
	print("KS Test 4:", ks_2samp(np.array(colorFours), np.array(colorFours2)))
