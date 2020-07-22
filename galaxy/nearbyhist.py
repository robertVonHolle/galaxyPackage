from galaxy import galaxy
import matplotlib.pyplot as plt
import math

def nearbyHist(galaxies, f, dist, bins=10, makeNearbyFile=False):
	r"""
	Creates a histogram of number of galaxies within a specified distance of
	a target galaxy

	Parameters:
		galaxies - Type: dict. A dictionary of all galaxies
		f - Type: str. The name of the file the histogram should be printed to
		dist - Type: float. The maximum distance in Mpc at which a galaxy is considered
			"nearby" the target galaxy
		bins (optional) - Type: int. The number of bins
		makeNearbyFile (optional) - Type: bool. Creates file containing info on galaxies
			with excessive neighbors if True

	Returns:
		None, but creates a histogram in the specified file
	"""

	# Constants
	c = 3 * 10 ** 8
	H0 = 73.8 * 1000

	# Since we are interested in the percentage of AGNs rather than the number of AGNs in
	# each bin, we will need to implement a histogram by hand using matplotlib.pyplot.bar
	# rather than simply using matplotlib.pyplot.hist

	# Determine the height of each bin
	binsList = [0,1,2,3,4,5,6,7,8,9,10]
	binHeights = []
	errs = []
	numAGN = 0
	numTot = 0
	for i in binsList:
		for key in galaxies:
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

	# Write galaxies with excessive numbers of neighbors to a file
	# so I can check them later
	if makeNearbyFile:
		badFile = open('tooManyGalaxies.txt', 'w')
		badFile.write("These galaxies have too many neighbors:\n")
		binsList.append(11)
		redshifts = []
		for key in galaxies:
			if galaxies[key].nearby >= 11:
				redshifts.append(galaxies[key].z)
				numTot += 1
				badFile.write(str(key) + " " + str(galaxies[key].ra) + " " + str(galaxies[key].dec) + " " + str(galaxies[key].z) + " " + str(galaxies[key].nearby) + "\n")
				if galaxies[key].agn != 0:
					numAGN += 1
		if numTot != 0:
			binHeights.append(numAGN / numTot)
			errs.append(math.sqrt(numAGN) / numTot)
		else:
			binHeights.append(0)
			errs.append(0)
		badFile.close()
	# Create final bin even if makeNearbyFile is False
	else:
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
			errs.append(0)

	print("Bin 11 covers range 11+ and includes a total of %s target galaxies." % numTot)

	print("Bin heights found")
	
	if makeNearbyFile:
		print("Max redshift of galaxies with too many neighbors:", max(redshifts))

	# Plot the histogram
	plt.bar(binsList, binHeights, yerr = errs)
	plt.title("Nearby Neighbors vs. AGN Probability",fontsize=14)
	plt.xlabel("Number of galaxies within distance of 0.5 Mpc of target",fontsize=14)
	plt.ylabel("Fraction of targets containing AGN",fontsize=14)
	plt.savefig(f)
	print("Created histogram")
	plt.clf()
