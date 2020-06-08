from galaxy import galaxy
import matplotlib.pyplot as plt
import math

def angularSeparation(ra1, ra2, d1, d2):
	r"""
	Calculates the angular separation between two galaixes

	Parameters:
		ra1 - Type: float. Right ascension of galaxy 1
		ra2 - Type: float. Right ascension of galaxy 2
		d1 - Type: float. Declination of galaxy 1
		d2 - Type: float. Declination of galaxy 2

	Returns:
		t - Type: float. Angular separation between galaxies in arcminutes
	"""
	t = math.degrees(math.atan(math.sqrt(math.cos(d2)**2 * math.sin(ra2 - ra1)**2
		+ (math.cos(d1) * math.cos(d2) - math.sin(d1) * math.cos(d2) * math.cos(ra2 - ra1))**2)
		/ (math.sin(d1) * math.sin(d2) + math.cos(d1) * math.cos(d2) * math.cos(ra2 - ra1))))

	t *= 60
	return t

def nearbyHist(galaxies, f, dist, bins=10):
	r"""
	Creates a histogram of number of galaxies within a specified distance of
	a target galaxy

	Parameters:
		galaxies - Type: dict. A dictionary of galaxies
		f - Type: str. The name of the file the histogram should be printed to
		dist - Type: float. The maximum distance in Mpc at which a galaxy is considered
			"nearby" the target galaxy
		bins (optional) - Type: int. The number of bins

	Returns:
		None, but creates a histogram in the specified file
	"""
	# Constants
	c = 3 * 10 ** 8
	H0 = 73.8 * 1000

	numNearby = []
	for key in galaxies:
		if galaxies[key].nearby <= 40:
			numNearby.append(galaxies[key].nearby)

#	# Find number of nearby galaxies for each galaxy
#	skipKeys = []
#	galaxiesNew = {}
#	numNearby = []
#	for key in galaxies:
#		galaxiesNew[key] = {'obj' : galaxies[key], 'numNearby' : 0}
#	
#	percent = math.ceil(len(galaxies) / 200)
#	showPercent = 0
#	for key1 in galaxiesNew:
#		skipKeys.append(key1)
#		for key2 in galaxies:
#			if not key2 in skipKeys:
#				if ((c / H0) * abs(galaxies[key1].z - galaxies[key2].z)) <= dist:
#					if angularSeparation(galaxies[key1].ra, galaxies[key2].ra, galaxies[key1].dec, galaxies[key2].dec) <= (0.1 / galaxies[key1].z) * (dist / 1.25):
#						galaxiesNew[key1]['numNearby'] += 1
#						galaxiesNew[key2]['numNearby'] += 1
#		showPercent += 1
#		if showPercent % percent == 0:
#			print((showPercent / len(galaxies)) * 100, "% complete")
#		numNearby.append(galaxiesNew[key1]['numNearby'])

#	print("Created galaxiesNew")

	# Since we are interested in the percentage of AGNs rather than the number of AGNs in
	# each bin, we will need to implement a histogram by hand using matplotlib.pyplot.bar
	# rather than simply using matplotlib.pyplot.hist

	# Determine the size of each bin
	binSize = math.ceil((max(numNearby) - min(numNearby)) / bins)

	# Determine the height of each bin
	binsList = [1,2,3,4,5,6,7,8,9,10]
	binHeights = []
	errs = []
	numAGN = 0
	numTot = 0
	for i in binsList:
		for key in galaxies:
#			if galaxies[key].nearby >= i * binSize and galaxies[key].nearby <= (i + 1) * binSize:
			if galaxies[key].nearby == i:
				numTot += 1
				if galaxies[key].agn != 0:
					numAGN += 1
		if numTot != 0:
			binHeights.append(numAGN / numTot)
			errs.append(math.sqrt(numAGN) / numTot)
		else:
			binHeights.append(0)
			errs.append(0)
		print("Bin", i, "covers range", i, "and includes a total of", numTot, "target galaxies.")
		numAGN = 0
		numTot = 0

	binsList.append(11)
	for key in galaxies:
		if galaxies[key].nearby >= 11:
			numTot += 1
			if galaxies[key].agn != 0:
				numAGN += 1
	if numTot != 0:
		binHeights.append(numAGN / numTot)
		errs.append(math.sqrt(numAGN) / numTot)
	else:
		binHeights.append(0)
		err.append(0)
	print("Bin 11 covers range 11+ and includes a total of %s target galaxies." % numTot)

	print("Bin heights found")

	# Plot the histogram
	plt.bar(binsList, binHeights, yerr = errs)
	plt.xlabel("Number of galaxies within projected distance of 1 Mpc of target")
	plt.ylabel("Fraction of targets with AGNs")
	plt.savefig(f)
	print("Created histogram")
	plt.clf()
