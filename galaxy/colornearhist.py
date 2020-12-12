from galaxy import galaxy
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm
import scipy.stats as stats
import seaborn as sns
#from scipy.stats import ks_2samp
#from scipy.stats.rv_discrete import cdf

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


	# Plot the histograms
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

	# Perform the KS test on the groups
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
	print("KS Test 0:", stats.ks_2samp(np.array(colorZeroes), np.array(colorZeroes2)))
	print("KS Test 1:", stats.ks_2samp(np.array(colorOnes), np.array(colorOnes2)))
	print("KS Test 2:", stats.ks_2samp(np.array(colorTwos), np.array(colorTwos2)))
	print("KS Test 3:", stats.ks_2samp(np.array(colorThrees), np.array(colorThrees2)))
	print("KS Test 4:", stats.ks_2samp(np.array(colorFours), np.array(colorFours2)))

	colorZeroes = [(galaxy.objId, galaxy.color) for galaxy in galaxyList if galaxy.color > errFlag and galaxy.agn > 0 and galaxy.nearby == 0]
	colorZeroes2 = [(galaxy.objId, galaxy.color) for galaxy in galaxyList if galaxy.color > errFlag and galaxy.agn == 0 and galaxy.nearby == 0]
	colorOnes = [(galaxy.objId, galaxy.color) for galaxy in galaxyList if galaxy.color > errFlag and galaxy.agn > 0 and galaxy.nearby == 1]
	colorOnes2 = [(galaxy.objId, galaxy.color) for galaxy in galaxyList if galaxy.color > errFlag and galaxy.agn == 0 and galaxy.nearby == 1]
	colorTwos = [(galaxy.objId, galaxy.color) for galaxy in galaxyList if galaxy.color > errFlag and galaxy.agn > 0 and galaxy.nearby == 2]
	colorTwos2 = [(galaxy.objId, galaxy.color) for galaxy in galaxyList if galaxy.color > errFlag and galaxy.agn == 0 and galaxy.nearby == 2]
	colorThrees = [(galaxy.objId, galaxy.color) for galaxy in galaxyList if galaxy.color > errFlag and galaxy.agn > 0 and galaxy.nearby == 3]
	colorThrees2 = [(galaxy.objId, galaxy.color) for galaxy in galaxyList if galaxy.color > errFlag and galaxy.agn == 0 and galaxy.nearby == 3]
	colorFours = [(galaxy.objId, galaxy.color) for galaxy in galaxyList if galaxy.color > errFlag and galaxy.agn > 0 and galaxy.nearby == 4]
	colorFours2 = [(galaxy.objId, galaxy.color) for galaxy in galaxyList if galaxy.color > errFlag and galaxy.agn == 0 and galaxy.nearby == 4]

	with open('galaxyData/withAGN.csv','w') as f:
		f.write("objID,numNear,color\n")
		for i in range(0, len(colorZeroes)):
			f.write(str(colorZeroes[i][0])+",0,"+str(colorZeroes[i][1])+"\n")
		for i in range(0, len(colorOnes)):
			f.write(str(colorOnes[i][0])+",1,"+str(colorOnes[i][1])+"\n")
		for i in range(0, len(colorTwos)):
			f.write(str(colorTwos[i][0])+",2,"+str(colorTwos[i][1])+"\n")
		for i in range(0, len(colorThrees)):
			f.write(str(colorThrees[i][0])+",3,"+str(colorThrees[i][1])+"\n")
		for i in range(0, len(colorFours)):
			f.write(str(colorFours[i][0])+",4,"+str(colorFours[i][1])+"\n")
		f.close()
	with open('galaxyData/withoutAGN.csv','w') as f:
		f.write("objID,numNear,color\n")
		for i in range(0, len(colorZeroes2)):
			f.write(str(colorZeroes2[i][0])+",0,"+str(colorZeroes2[i][1])+"\n")
		for i in range(0, len(colorOnes2)):
			f.write(str(colorOnes2[i][0])+",1,"+str(colorOnes2[i][1])+"\n")
		for i in range(0, len(colorTwos2)):
			f.write(str(colorTwos2[i][0])+",2,"+str(colorTwos2[i][1])+"\n")
		for i in range(0, len(colorThrees2)):
			f.write(str(colorThrees2[i][0])+",3,"+str(colorThrees2[i][1])+"\n")
		for i in range(0, len(colorFours2)):
			f.write(str(colorFours2[i][0])+",4,"+str(colorFours2[i][1])+"\n")
		f.close()

#	with open('galaxyData/colorZeroes.csv','w') as f:
#		f.write("objID,AGN,color\n")
#		for i in range(0, len(colorZeroes)):
#			f.write(str(colorZeroes[i][0])+",True,"+str(colorZeroes[i][1])+"\n")
#		for i in range(0, len(colorZeroes2)):
#			f.write(str(colorZeroes2[i][0])+",False,"+str(colorZeroes2[i][1])+"\n")
#		f.close()
#	with open('galaxyData/colorOnes.csv','w') as f:
#		f.write("objID,AGN,color\n")
#		for i in range(0, len(colorOnes)):
#			f.write(str(colorOnes[i][0])+",True,"+str(colorOnes[i][1])+"\n")
#		for i in range(0, len(colorOnes2)):
#			f.write(str(colorOnes2[i][0])+",False,"+str(colorOnes2[i][1])+"\n")
#		f.close()
#	with open('galaxyData/colorTwos.csv','w') as f:
#		f.write("objID,AGN,color\n")
#		for i in range(0, len(colorTwos)):
#			f.write(str(colorTwos[i][0])+",True,"+str(colorTwos[i][1])+"\n")
#		for i in range(0, len(colorTwos2)):
#			f.write(str(colorTwos2[i][0])+",False,"+str(colorTwos2[i][1])+"\n")
#		f.close()
#	with open('galaxyData/colorThrees.csv','w') as f:
#		f.write("objID,AGN,color\n")
#		for i in range(0, len(colorThrees)):
#			f.write(str(colorThrees[i][0])+",True,"+str(colorThrees[i][1])+"\n")
#		for i in range(0, len(colorThrees2)):
#			f.write(str(colorThrees2[i][0])+",False,"+str(colorThrees2[i][1])+"\n")
#		f.close()
#	with open('galaxyData/colorFours.csv','w') as f:
#		f.write("objID,AGN,color\n")
#		for i in range(0, len(colorFours)):
#			f.write(str(colorFours[i][0])+",True,"+str(colorFours[i][1])+"\n")
#		for i in range(0, len(colorFours2)):
#			f.write(str(colorFours2[i][0])+",False,"+str(colorFours2[i][1])+"\n")
#		f.close()
#	print("Wrote files for CDF calculation")


	# Check by manually plotting CDF
#	colorZeroesCDF = stats.rv_discrete.cdf(colorZeroes, 0.5)
#	colorZeroes2CDF = stats.rv_discrete.cdf(colorZeroes2, 0.5)
#	x1 = range(0, len(colorZeroesCDF))
#	x2 = range(0, len(colorZeroes2CDF))
#	plt.plot(x1, colorZeroesCDF, label="With AGN")
#	plt.plot(x2, colorZeroes2CDF, label="Without AGN")
#	plt.legend()
#	plt.savefig('../plots/zeroesCDF.png')
#	plt.clf()
#
#	colorOnesCDF = stats.rv_discrete.cdf(colorOnes, 0.5)
#	colorOnes2CDF = stats.rv_discrete.cdf(colorOnes2, 0.5)
#	x1 = range(0, len(colorOnesCDF))
#	x2 = range(0, len(colorOnes2CDF))
#	plt.plot(x1, colorOnesCDF, label="With AGN")
#	plt.plot(x2, colorOnesCDF, label="Without AGN")
#	plt.legend()
#	plt.savefig('../plots/onesCDF.png')
#	plt.clf()
#
#	colorTwosCDF = stats.rv_discrete.cdf(colorTwos, 0.5)
#	colorTwos2CDF = stats.rv_discrete.cdf(colorTwos, 0.5)
#	x1 = range(0, len(colorTwosCDF))
#	x2 = range(0, len(colorTwos2CDF))
#	plt.plot(x1, colorTwosCDF, label="With AGN")
#	plt.plot(x2, colorTwosCDF, label="Without AGN")
#	plt.legend()
#	plt.savefig('../plots/twosCDF.png')
#	plt.clf()
#	
#	colorThreesCDF = stats.rv_discrete.cdf(colorThrees, 0.5)
#	colorThrees2CDF = stats.rv_discrete.cdf(colorThrees2, 0.5)
#	x1 = range(0, len(colorThreesCDF))
#	x2 = range(0, len(colorThrees2CDF))
#	plt.plot(x1, colorThreesCDF, label="With AGN")
#	plt.plot(x2, colorThrees2CDF, label="Without AGN")
#	plt.legend()
#	plt.savefig('../plots/threesCDF.png')
#	plt.clf()
#
#	colorFoursCDF = stats.rv_discrete.cdf(colorFours, 0.5)
#	colorFours2CDF = stats.rv_discrete.cdf(colorFours2, 0.5)
#	x1 = range(0, len(colorFoursCDF))
#	x2 = range(0, len(colorFours2CDF))
#	plt.plot(x1, colorFoursCDF, label="With AGN")
#	plt.plot(x2, colorFours2CDF, label="Without AGN")
#	plt.legend()
#	plt.savefig('../plots/foursCDF.png')
#	plt.clf()
