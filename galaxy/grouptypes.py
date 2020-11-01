from galaxy import galaxy
from galaxy.isblue import isBlue
from astropy.utils.console import ProgressBar
import math

def findStats(groupList, groupName, galaxies, f):
	r"""
	Finds and prints statistics on groups of nearby galaxies

	Parameters:
		groupList - Type: list. A list of groups of galaxies
		groupName - Type: str. The name of the current group
		galaxies - Type: dict. The dictionary of galaxies
		f - Type: str. The name of the file to be written to

	Returns:
	"""
	agnCount = 0       # Number of galaxies in a group with AGN
	majorityCount = 0  # Number of groups in which a majority of galaxies have AGN
	totCount = 0	   # Number of groups in which every galaxy has AGN
	noneCount = 0	   # Number of groups in which no galaxies have AGN
	blueCountTot = 0   # Total number of blue galaxies
	redCountTot = 0    # Total number of red galaxies
	blueAgnTot = 0     # Total number of blue galaxies with AGN
	redAgnTot = 0      # Total number of red galaxies with AGN
	for group in groupList:
		agnCount = len([item for item in group if galaxies[item].agn != 0])
		blueGroup = [item for item in group if isBlue(galaxies[item])]
		redGroup = [item for item in group if not isBlue(galaxies[item])]
		blueCountTot += len(blueGroup)
		redCountTot += len(redGroup)
		blueAgnTot += len([item for item in blueGroup if galaxies[item].agn != 0])
		redAgnTot += len([item for item in redGroup if galaxies[item].agn != 0])
		#for item in group:
		#	if galaxies[item].agn != 0:
		#		agnCount += 1
		if agnCount >= math.ceil(len(group) / 2) and not agnCount == len(group):
			majorityCount += 1
		elif agnCount == len(group):
			totCount += 1
		elif agnCount == 0:
			noneCount += 1
		agnCount = 0
	logFile = open(f, 'a')
	if len(groupList) > 0:
		logFile.write("Found " + str(len(groupList)) + groupName + " groups\n")
		logFile.write("Of these groups, " + str(100 * totCount/ len(groupList)) + "% have an AGN in every galaxy\n")
		logFile.write("Of these groups, " + str(100 * majorityCount / len(groupList)) + "% have an AGN in the majority of galaxies but not every galaxy\n")
		logFile.write("Of these groups, " + str(100 * noneCount / len(groupList)) + "% have no AGN\n")
		if blueCountTot > 0:
			logFile.write(str(100 * blueAgnTot / blueCountTot) + "% of blue galaxies in these groups have AGN.\n")
		if redCountTot > 0:
			logFile.write(str(100 * redAgnTot / redCountTot) + "% of red galaxies in these groups have AGN.\n")
		logFile.close()
	else:
		logFile.write("Found 0" + groupName + "groups")

def groupTypes(galaxies, f):
	r"""
	Performs some statistical analysis on groups of nearby galaxies

	Parameters:
		galaxies - Type: dict. A dictionary of all galaxies
		data - Type: pandas dataframe. The original data set
		f - Type: str. The name of the file in which results should be printed

	Returns:
		None, but prints a log of the statistical analysis
	"""
	usedKeys = []  # Keys already investigated that do not need to be iterated through again
	red = []       # Groups of galaxies in which all are red
	redBlue = []   # Groups of galaxies in which most are red
	split = []	   # Groups of galaxies which are exactly half red, half blue
	blueRed = []   # Groups of galaxies in which most are blue
	blue = []  	   # Groups of galaxies in which all are blue
	redCount = 0
	blueCount = 0
	i = 0
	j = 0
	print(type(galaxies))
	bar = ProgressBar(len(galaxies))
	keyslist = list(set([key for key in galaxies]))
	for key in galaxies:
		bar.update()
		if not key in usedKeys:
			target = galaxies[key]
			nearby_gals = galaxies[key].nearbyIDs
			nearby_gals.insert(0, key)
			usedKeys.append(key)
			if isBlue(galaxies[key]):
				blueCount += 1
			else:
				redCount += 1
			usedKeys += [item for item in nearby_gals]
			blueCount = len([1 for item in nearby_gals if isBlue(galaxies[item])])
			redCount = len([1 for item in nearby_gals if not isBlue(galaxies[item])])
			if redCount != 0 and blueCount == 0:
				red.append(nearby_gals)
			elif redCount > blueCount and blueCount != 0:
				redBlue.append(nearby_gals)
			elif redCount == blueCount and redCount != 0:
				split.append(nearby_gals)
			elif redCount < blueCount and redCount != 0:
				blueRed.append(nearby_gals)
			elif redCount == 0 and blueCount != 0:
				blue.append(nearby_gals)
			else:
				raise ValueError("Group found containing no galaxies. Target: %s" % (key))
		redCount = 0
		blueCount = 0

	print("\n")
	# Clear any existing contents of the log file
	logFile = open(f, 'w')
	logFile.seek(0)
	logFile.truncate()
	logFile.close()

	# Find statistics for red groups
	red = [group for group in red if len(group) > 1]
	print("Red list length:", len(red))
	findStats(red, "entirely red", galaxies, f)

	# Find statistics for majority red groups
	redBlue = [group for group in redBlue if len(group) > 1]
	print("redBlue list length:", len(redBlue))
	findStats(redBlue, "red/blue", galaxies, f)

	# Find statistics for equally red and blue groups
	split = [group for group in split if len(group) > 1]
	print("split list length:", len(split))
	findStats(split, "an equal number of red and blue", galaxies, f)

	# Find statistics for majority blue groups
	blueRed = [group for group in blueRed if len(group) > 1]
	print("blueRed list length:", len(blueRed))
	findStats(blueRed, "blue/red", galaxies, f)

	# Find statistics for blue groups
	blue = [group for group in blue if len(group) > 1]
	print("blue list length:", len(blue))
	findStats(blue, "entirely blue", galaxies, f)
