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
				galaxies[int(data['objID'][i])] = galaxy(int(data['objID'][i]), data['ra'][i], data['dec'][i], data['z'][i], 0., 0., data['bpt'][i], u=data['modelMag_u'][i], r=data['modelMag_r'][i], nearby=int(data['Column1'][i]))
		# Exclude number of nearby neighbors if it is not present
		else:
			for i in range(len(data['objID'])):
				galaxies[int(data['objID'][i])] = galaxy(int(data['objID'][i]), data['ra'][i], data['dec'][i], data['z'][i], 0., 0., data['bpt'][i], u=data['modelMag_u'][i], r=data['modelMag_r'][i])
	# This works slightly different when we want to get IDs of nearby galaxies
	else:
		for i in range(len(data['objID'])):
			galaxies[int(data['objID'][i])] = galaxy(int(data['objID'][i]), data['ra'][i], data['dec'][i], data['z'][i], 0., 0., data['bpt'][i])
		keys = set(data['objID'])
		i = 0
		j = 1
		onePercent = math.ceil(len(keys) / 100)
		# iterate through unique object IDs
		for key in keys:
			lastID = 0
			# print approximate completion percent because this could take a while
			if (i % onePercent) == 0 and i != 0:
				print(j, "% complete")
				j += 1
			tempList = []
			# iterate through whole dataset to gather information from all duplicates of that object
			while i < len(data['objID']) - 1:
				i += 1
				if data['objID'][i] == key:
					tempList.append(int(data['nearbyID'][i]))
					lastID == data['objID'][i]
				elif lastID == key:
					galaxies[key].nearbyIDs = tempList
					break
			else:
				tempList.append(int(data['nearbyID'][i]))
				galaxies[key].nearbyIDs = tempList
				galaxies[key].nearby = len(tempList)

	return galaxies
