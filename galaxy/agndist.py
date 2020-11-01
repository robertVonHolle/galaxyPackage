from galaxy import galaxy
from galaxy.isblue import isBlue
import matplotlib.pyplot as plt
import math

def agnDist(galaxies, f):
	r"""
	Creates a histogram comparing the fraction of galaxies with AGN to the
	fraction of nearby neighbors with AGN

	Parameters:
		galaxies - Type: dict. A dictionary of galaxy objects to plot
		f - Type: str. The name of the file to put the galaxy plot in

	Returns nothing but prints histogram to specified file
	"""

	binsList = [0,1,2,3,4]
	binHeights = []
	errs = []
	galaxyPercents = {}
	for item in galaxies:
		if galaxies[item].nearby > 0:
			nearbyAGN = 100 * len([i for i in galaxies[item].nearbyIDs if galaxies[i].agn > 0]) / galaxies[item].nearby
			galaxyPercents.update({item: nearbyAGN})
		else:
			galaxyPercents.update({item: 0})
	
	binList = [i for i in galaxies if galaxyPercents[i] >= 0 and galaxyPercents[i] <= 20]
	if len(binList) > 0:
		agnList = [i for i in binList if galaxies[i].agn > 0]
		binHeights.append(len(agnList) / len(binList))
		errs.append(math.sqrt(len(agnList)) / len(binList))
	else:
		binHeights.append(0.)
		errs.append(0.)
	print("Bin 0 covers range 0% <= x <= 20% and includes a total of", len(binList), "galaxies.")

	for i in range(1,5):
		binList = [j for j in galaxies if galaxyPercents[j] > (20 * i) and galaxyPercents[j] <= (20 * (i + 1))]
		if len(binList) > 0:
			agnList = [j for j in binList if galaxies[j].agn > 0]
			binHeights.append(len(agnList) / len(binList))
			errs.append(math.sqrt(len(agnList)) / len(binList))
		else:
			binHeights.append(0.)
			errs.append(0.)
		print("Bin", i, "covers range", 20 * i, "< x <=", 20 * (i + 1), "and includes a total of", len(binList), "galaxies.")

	plt.bar(binsList, binHeights, yerr = errs)
	plt.title("Nearby AGN vs AGN probability", fontsize=14)
	plt.xlabel("Percent of nearby neighbors with AGN",fontsize=14)
	plt.ylabel("Fraction of targets containing AGN",fontsize=14)
	plt.savefig(f)
	print("Created AGN distribution histogram")
	plt.clf
