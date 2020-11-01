from galaxy import galaxy

def pairTypes(galaxies, f):
	r"""
	Performs some statistical analysis on pairs of nearby galaxies

	Parameters:
		galaxies - Type: dict. A dictionary of all galaxies
		f - Type: str. The name of the file in which results should be printed

	Returns:
		None, but prints a log of the statistical analysis
	"""
	usedKeys = []  # Keys already investigated that do not need to be iterated through again
	redRed = []    # Pairs of galaxies in which both are red
	redBlue = []   # Pairs of galaxies in which one is red and one is blue
	blueBlue = []  # Pairs of galaxies in which both are blue
	for key in galaxies:
		if not key in usedKeys and not galaxies[key].nearbyID in usedKeys:
			galaxy1 = galaxies[key]
			galaxy2 = galaxy1.nearbyID
			usedKeys.append(key)
			usedKeys.append(galaxy2.objID)
			if isBlue(galaxy1) != isBlue(galaxy2):
				redBlue.append((galaxy1.objID, galaxy2.objID))
			elif isBlue(galaxy1) and isBlue(galaxy2):
				blueBlue.append((galaxy1.objID, galaxy2.objID))
			else:
				redRed.append((galaxy1.objID, galaxy2.objID))
	
	logFile = open(f, 'w')
	logFile.write("Found %s red/red pairs\n" % len(redRed))

	# Are red/red pairs, red/blue pairs, or blue/blue pairs most likely to have AGNs?
	# First, find the percentage of red/red pairs with AGNs
	agnCount1 = 0  # Number of pairs with at least one AGN
	agnCount2 = 0  # Number of pairs with two AGNs
	# agnCount1 - agnCount2 = number of pairs with exactly 1 AGN
	for item in redRed:
		if galaxies[item[0]].agn != 0 and galaxies[item[1]].agn != 0:
			agnCount1 += 1
			agnCount2 += 1
		elif galaxies[item[0]].agn != 0 or galaxies[item[1]].agn != 0:
			agnCount1 += 1
	
	logFile.write("Of these red/red pairs, %s\% have at least one AGN\n" % (100 * (agnCount1 / len(redRed))))
	logFile.write("Of these red/red pairs, %s\% have exactly one AGN\n" % (100 * ((agnCount1 - agnCount2) / len(redRed))))
	logFile.write("Of these red/red pairs, %s\% have two AGNs\n" % (100 * (agnCount2 / len(redRed))))
	logFile.write("\n")

	logFile.write("Found %s blue/blue pairs\n" % len(blueBlue))

	# Next, find the percentage of blue/blue pairs with AGNS
	agnCount1 = 0  # Reset count of pairs with at least one AGN
	agnCount2 = 0  # Reset count of pairs with two AGNs
	for item in blueBlue:
		if galaxies[item[0]].agn != 0 and galaxies[item[1]].agn != 0:
			agnCount1 += 1
			agnCount2 += 1
		elif galaxies[item[0]].agn != 0 or galaxies[item[1]].agn != 0:
			agnCount1 += 1
	
	logFile.write("Of these blue/blue pairs, %s\% have at least one AGN\n" % (100 * (agnCount1 / len(blueBlue))))
	logFile.write("Of these blue/blue pairs, %s\% have exactly one AGN\n" % (100 * ((agnCount1 - agnCount2) / len(blueBlue))))
	logFile.write("Of these blue/blue pairs, %s\% have two AGNs\n" % (100 * (agnCount2/ len(blueBlue))))
	logFile.write("\n")

	logFile.write("Found %s red/blue pairs\n" % len(blueBlue))
	
	# Lastly, the red/blue pairs require a little more analysis
	agnCount1 = 0  # Reset count of pairs with at least one AGN
	agnCount2 = 0  # Reset count of pairs with two AGNs
	redAGN = 0     # If a pair has exaclty one AGN, in how many is the AGN in the red galaxy
	blueAGN = 0    # If a pair has exactly one AGN, in how many is the AGN in the blue galaxy
	for item in redBlue:
		if galaxies[item[0]].agn != 0 and galaxies[item[1]].agn != 0:
			agnCount1 += 1
			agnCount2 += 1
		elif galaxies[item[0]].agn != 0 or galaxies[item[1]].agn != 0:
			agnCount1 += 1
			if galaxies[item[0]].agn != 0:
				if isBlue(galaxies[item[0]]):
					blueAGN += 1
				else:
					redAGN += 1
			else:
				if isBlue(galaxies[item[1]]):
					blueAGN += 1
				else:
					redAGN += 1
	
	logFile.write("Of these red/blue pairs, %s\% have at least one AGN\n" % (100 * (agnCount1 / len(redBlue))))
	logFile.write("Of these red/blue pairs, %s\% have exactly one AGN\n" % (100 * ((agnCount1 - agnCount2)) / len(redBlue)))
	logFile.write("Of these red/blue pairs with exactly one AGN, the AGN is in the red galaxy for %s\% of pairs\n" % (100 * redAGN / (agnCount1 - agnCount2)))
	logFile.write("Of these red/blue pairs with exactly one AGN, the AGN is in the blue galaxy for %s\% of pairs\n" % (100 * blueAGN / (agnCount1 - agnCount2)))
	logFile.write("Of these red/blue pairs, %s\% have two AGNs\n" % (100 * (agnCount2 / len(redBlue))))
