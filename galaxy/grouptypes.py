from galaxy import galaxy
from galaxy.isblue import isBlue
import math

def findStats(groupList, groupName, f):
	r"""
	Finds and prints statistics on groups of nearby galaxies

	Parameters:
		groupList - Type: list. A list of groups of galaxies
		groupName - Type: str. The name of the current group
		f - Type: str. The name of the file to be written to

	Returns:
	"""
	agnCount = 0       # Number of galaxies in a group with AGN
	majorityCount = 0  # Number of groups in which a majority of galaxies have AGN
	totCount = 0	   # Number of groups in which every galaxy has AGN
	noneCount = 0	   # Number of groups in which no galaxies have AGN
	for group in groupList:
		for key in group:
			if group[key].agn != 0:
				agnCount += 1
		if agnCount >= math.ceil(len(group) / 2) and not agnCount == len(group):
			majorityCount += 1
		elif agnCount == len(group):
			totCount += 1
		elif agnCount == 0:
			noneCount += 1
		agnCount = 0
	logFile = open(f, 'a')
	if len(groupList) > 0:
		logFile.write("Found" + str(len(groupList)) + groupName + "groups")
		logFile.write("Of these groups," + str(100 * totCount/ len(groupList)) + "% have an AGN in every galaxy\n")
		logFile.write("Of these groups," + str(100 * majorityCount / len(groupList)) + "% have an AGN in the majority of galaxies but not every galaxy\n")
		logFile.write("Of these groups," + str(100 * noneCount / len(groupList)) + "% have no AGNs\n")
		logFile.close()
	else:
		logFile.write("Found 0" + groupName + "groups")

def groupTypes(galaxies, f):
	r"""
	Performs some statistical analysis on groups of nearby galaxies

	Parameters:
		galaxies - Type: dict. A dictionary of all galaxies
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
	fivePercent = math.ceil(len(galaxies) / 20)
	for key in galaxies:
		if i % fivePercent == 0:
			print(j * 5, "% complete")
			j += 1
		if i == 1:
			print("usedKeyslen:", len(usedKeys))
		i += 1
		#hasUsedKey = False  # Check for used keys in nearbyIDs list
		#for key2 in galaxies[key].nearbyIDs:
			#if key2 in usedKeys and key2 != key:  # If nearbyIDs list has a used key,
								  # this group has already been investigated
			#	hasUsedKey = True
			#	break
		if not key in usedKeys:
			target = galaxies[key]
			nearby_gals = galaxies[key].nearbyIDs
			usedKeys.append(key)
			for item in nearby_gals:
				usedKeys.append(item)
				if isBlue(galaxies[item]):
					blueCount += 1
				else:
					redCount += 1
			if redCount != 0 and blueCount == 0:
				red.append(nearby_gals)
			elif redCount > blueCount and blueCount != 0:
				redBlue.append(nearby_gals)
			elif redCount == blueCount and redCount != 0:
				split.append(nearby_gals.append(key))
			elif redCount < blueCount and redCount != 0:
				blueRed.append(nearby_gals.append(key))
			elif redCount == 0 and blueCount != 0:
				blue.append(nearby_gals.append(key))
			else:
				raise ValueError("Group found containing no galaxies. Target: %s" % (key))
		#elif hasUsedKey:
		#	for key2 in galaxies[key].nearbyIDs:
		#		if not key2 in usedKeys:
		#			usedKeys.append(key2)
		redCount = 0
		blueCount = 0
	
	# Clear any existing contents of the log file
	logFile = open(f, 'w')
	logFile.seek(0)
	logFile.truncate()
	logFile.close()

	# Find statistics for red groups
	print("Red list length:", len(red))
	findStats(red, "entirely red", f)

	# Find statistics for majority red groups
	print("redBlue list length:", len(redBlue))
	findStats(redBlue, "red/blue", f)

	# Find statistics for equally red and blue groups
	print("split list length:", len(split))
	findStats(split, "an equal number of red and blue", f)

	# Find statistics for majority blue groups
	print("blueRed list length:", len(blueRed))
	findStats(blueRed, "blue/red", f)

	# Find statistics for blue groups
	print("blue list length:", len(blue))
	findStats(blue, "entirely blue", f)
