import numpy as np
import math
from galaxy.galaxy import galaxy

def dataGen(f):
	r"""
	Generates a dictionary of galaxy objects from a file

	Parameters
		f - Type: str. The name of the file

	Returns
		galaxies - Type: dict. A dictionary of galaxy objects with object IDs as keys
	"""

	data = np.genfromtxt(f, dtype=None, delimiter=",", names=True, encoding=None)

	galaxies = {}
	if 'modelMag_u' in data.dtype.names:  # As of now, this column is always included in datasets not
										  # including object IDs of nearby galaxies and never in
										  # data sets that do include them
		# Include number of nearby neighbors if it is present
		if 'Column1' in data.dtype.names:
			for i in range(len(data['objID'])):
				galaxies[int(data['objID'][i])] = galaxy(int(data['objID'][i]), data['ra'][i], data['dec'][i], data['z'][i], redshift=data['redshift'][i], u=data['modelMag_u'][i], r=data['modelMag_r'][i], 0., 0., data['bpt'][i], int(data['Column1'][i] - 1))
		# Exclude number of nearby neighbors if it is not present
		else:
			for i in range(len(data['objID'])):
				galaxies[int(data['objID'][i])] = galaxy(int(data['objID'][i]), data['ra'][i], data['dec'][i], data['z'][i], redshift=data['redshift'][i], u=data['modelMag_u'][i], r=data['modelMag_r'][i], 0., 0., data['bpt'][i])
	# This works slightly different when we want to get IDs of nearby galaxies
	else:
		keys = set(data['objID'])
		skipKeys = []
		i = 0
		j = 1
		fivePercent = math.ceil(len(keys) / 20)
		# iterate through unique object IDs
		for key in keys:
			# print approximate completion percent because this could take a while
			if (i % fivePercent) == 0:
				print("%s\% complete" % (5 * j))
				j += 1
			tempList = []
			# iterate through whole dataset to gather information from all duplicates of that object
			while i < (len(data['objID']) - 1) and data['objID'][i + 1] == data['objID'][i]:
				if data['objID'][i] in skipKeys or data['objID'][i] != key:
					continue
				tempList.append(data['nearbyID'][i])
				skipKeys.append(data['nearbyID'][i])
				i += 1
			else:
				# if this is not an edge case and we have gathered data from every duplicate,
				# add this object to the galaxies dictionary
				if i < (len(data['objID']) - 1) and data['objID'][i] != data['objID'][-1]:
					tempList.append(data['nearbyID'][i])
					skipKeys.append(data['nearbyID'][i])
					galaxies[int(data['objID'][i])] = galaxy(int(data['objID'][i]), data['ra'][i], data['dec'][i], data['z'][i], Mr=0., color=0., agn=data['bpt'][i], nearbyIDs=tempList)
				# if we haven't reached the end of the list but the tem we're on is a duplicate
				# of the last item
				elif i <= (len(data['objID']) - 1) and data['objID'][i] == data['objID'][-1]:
					# iterate through remaining items to gather necessary data
					while i < len(data['objID']):
						if data['objID'][i] in skipKeys:
							i += 1
							continue
						tempList.append(data['nearbyID'][i])
						skipKeys.append(data['nearbyID'][i])
						i += 1
					# add final object to galaxies dictionary
					else:
						galaxies[int(data['objID'][i])] = galaxy(int(data['objID'][i]), data['ra'][i], data['dec'][i], data['z'][i], Mr=0., color=0., agn=data['bpt'][i], nearbyIDs=tempList)
				# if the last object has no duplicates, add both it and the previous object
				# to the galaxies dictionary
				elif i == (len(data['objID']) - 1) and data['objID'][-1] != data['objID'][-2]:
					galaxies[int(data['objID'][i])] = galaxy(int(data['objID'][i]), data['ra'][i], data['dec'][i], data['z'][i], Mr=0., color=0., agn=data['bpt'][i], nearbyIDs=tempList)
					tempList = []
					tempList.append(data['nearbyID'][-1])
					skipKeys.append(data['nearbyID'][-1])
					galaxies[int(data['objID'][-1])] = galaxy(int(data['objID'][i]), data['ra'][i], data['dec'][i], data['z'][i], Mr=0., color=0., agn=data['bpt'][i], nearbyIDs=tempList)
				# catch unexpected cases and print potentially useful error message
				else:
					print("Unexpected case!")
					print("i =", i)
					print("list len =", len(data['objID']))
					print("Most recent objID =", data['objID'][i])
					print("NearbyID for this iteration ", data['nearbyID'][i])
					raise ValueError("End error message")
	return galaxies
