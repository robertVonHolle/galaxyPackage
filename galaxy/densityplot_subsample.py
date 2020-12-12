from galaxy import galaxy
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import scipy.stats as stats
import numpy as np

def densityPlot_subsample(galaxies):

	# Create subsample of galaxies with AGN and plot
	withAGN = [ID for ID in galaxies if galaxies[ID].agn != 0 and galaxies[ID].color >= 0 and galaxies[ID].color <= 5 and galaxies[ID].Mr >= -24 and galaxies[ID].Mr <= -17]
	colorWith = [galaxies[ID].color for ID in withAGN]
	mrWith = [galaxies[ID].Mr for ID in withAGN]
	plt.hist2d(colorWith, mrWith, bins=100, norm=LogNorm(), cmin=1, cmap=plt.cm.inferno)
	plt.gca().invert_yaxis()
	plt.xlabel("Color (u - r)", fontsize=14)
	plt.ylabel("Absolute Magnitude", fontsize=14)
	plt.colorbar()
	plt.savefig('plots/galaxiesWithAGN.png')
	plt.clf()

	# Create subsample of galaxies without AGN and plot
	withoutAGN = [ID for ID in galaxies if galaxies[ID].agn == 0 and galaxies[ID].color >= 0 and galaxies[ID].color <= 5 and galaxies[ID].Mr >= -24 and galaxies[ID].Mr <= -17]
	colorWithout = [galaxies[ID].color for ID in withoutAGN]
	mrWithout = [galaxies[ID].Mr for ID in withoutAGN]
	plt.hist2d(colorWithout, mrWithout, bins=100, norm=LogNorm(), cmin=1, cmap=plt.cm.inferno)
	plt.gca().invert_yaxis()
	plt.xlabel("Color (u - r)", fontsize=14)
	plt.ylabel("Absolute Magnitude", fontsize=14)
	plt.colorbar()
	plt.savefig('plots/galaxiesWithoutAGN.png')
	plt.clf()

	# Divide subsamples further by number of nearby neighbors
	withZeroes = [ID for ID in withAGN if galaxies[ID].nearby == 0]
	withoutZeroes = [ID for ID in withoutAGN if galaxies[ID].nearby == 0]
	withOnes = [ID for ID in withAGN if galaxies[ID].nearby == 1]
	withoutOnes = [ID for ID in withoutAGN if galaxies[ID].nearby == 1]
	withTwos = [ID for ID in withAGN if galaxies[ID].nearby == 2]
	withoutTwos = [ID for ID in withoutAGN if galaxies[ID].nearby == 2]
	withThrees = [ID for ID in withAGN if galaxies[ID].nearby == 3]
	withoutThrees = [ID for ID in withoutAGN if galaxies[ID].nearby == 3]
	withFours = [ID for ID in withAGN if galaxies[ID].nearby == 4]
	withoutFours = [ID for ID in withoutAGN if galaxies[ID].nearby == 4]

	# Create lists of x values for each subsample
	colorWithZeroes = [galaxies[ID].color for ID in withZeroes]
	colorWithoutZeroes = [galaxies[ID].color for ID in withoutZeroes]
	colorWithOnes = [galaxies[ID].color for ID in withOnes]
	colorWithoutOnes = [galaxies[ID].color for ID in withoutOnes]
	colorWithTwos = [galaxies[ID].color for ID in withTwos]
	colorWithoutTwos = [galaxies[ID].color for ID in withoutTwos]
	colorWithThrees = [galaxies[ID].color for ID in withThrees]
	colorWithoutThrees = [galaxies[ID].color for ID in withoutThrees]
	colorWithFours = [galaxies[ID].color for ID in withFours]
	colorWithoutFours = [galaxies[ID].color for ID in withoutFours]

	# Create lists of y values for each subsample
	mrWithZeroes = [galaxies[ID].Mr for ID in withZeroes]
	mrWithoutZeroes = [galaxies[ID].Mr for ID in withoutZeroes]
	mrWithOnes = [galaxies[ID].Mr for ID in withOnes]
	mrWithoutOnes = [galaxies[ID].Mr for ID in withoutOnes]
	mrWithTwos = [galaxies[ID].Mr for ID in withTwos]
	mrWithoutTwos = [galaxies[ID].Mr for ID in withoutTwos]
	mrWithThrees = [galaxies[ID].Mr for ID in withThrees]
	mrWithoutThrees = [galaxies[ID].Mr for ID in withoutThrees]
	mrWithFours = [galaxies[ID].Mr for ID in withFours]
	mrWithoutFours = [galaxies[ID].Mr for ID in withoutFours]

	# Create iterable lists of subsample x and y values
	colorWith = [colorWithZeroes, colorWithOnes, colorWithTwos, colorWithThrees, colorWithFours]
	colorWithout = [colorWithoutZeroes, colorWithoutOnes, colorWithoutTwos, colorWithoutThrees, colorWithoutFours]
	mrWith = [mrWithZeroes, mrWithOnes, mrWithTwos, mrWithThrees, mrWithFours]
	mrWithout = [mrWithoutZeroes, mrWithoutOnes, mrWithoutTwos, mrWithoutThrees, mrWithoutFours]

	# Iterate through lists to plot subsamples and perform KS tests
	for i in range(0,5):
		plt.hist2d(colorWith[i], mrWith[i], bins=60, norm=LogNorm(), cmin=1, cmap=plt.cm.inferno)
		plt.xlim(0,5)
		plt.ylim(-24,-17)
		plt.xlabel("Color (u-r)", fontsize=14)
		plt.ylabel("Absolute Magnitude")
		plt.colorbar()
		plt.gca().invert_yaxis()
		plt.savefig("plots/withAGN"+str(i)+".png")
		plt.clf()
		
		plt.hist2d(colorWithout[i], mrWithout[i], bins=60, norm=LogNorm(), cmin=1, cmap=plt.cm.inferno)
		plt.xlim(0,5)
		plt.ylim(-24,-17)
		plt.xlabel("Color (u-r)", fontsize=14)
		plt.ylabel("Absolute Magnitude")
		plt.colorbar()
		plt.gca().invert_yaxis()
		plt.savefig("plots/withoutAGN"+str(i)+".png")
		plt.clf()

		for j in range(i+1,5):
			print("With KS Test",i,"/",j, stats.ks_2samp(np.array(colorWith[i]), np.array(colorWith[j])))
			print("Without KS Test",i,"/",j, stats.ks_2samp(np.array(colorWithout[i]), np.array(colorWithout[j])))	
