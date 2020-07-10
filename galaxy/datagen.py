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
	if not 'nearbyID' in data.dtype.names:  # As of now, this column is always included in datasets not
										  # including object IDs of nearby galaxies and never in
										  # data sets that do include them
		# Include number of nearby neighbors if it is present
		if 'modelMag_u' in data.dtype.names:
			if 'Column1' in data.dtype.names:
				for i in range(len(data['objID'])):
					galaxies[int(data['objID'][i])] = galaxy(int(data['objID'][i]), data['ra'][i], data['dec'][i], data['z'][i], 0., 0., data['bpt'][i], u=data['modelMag_u'][i], r=data['modelMag_r'][i], nearby=int(data['Column1'][i]))
			# Exclude number of nearby neighbors if it is not present
			else:
				for i in range(len(data['objID'])):
					galaxies[int(data['objID'][i])] = galaxy(int(data['objID'][i]), data['ra'][i], data['dec'][i], data['z'][i], 0., 0., data['bpt'][i], u=data['modelMag_u'][i], r=data['modelMag_r'][i])
		else:
			if 'Column1' in data.dtype.names:
				for i in range(len(data['objID'])):
					galaxies[int(data['objID'][i])] = galaxy(int(data['objID'][i]), data['ra'][i], data['dec'][i], data['z'][i], 0., 0., data['bpt'][i],  nearby=int(data['Column1'][i]))
			# Exclude number of nearby neighbors if it is not present
			else:
				for i in range(len(data['objID'])):
					galaxies[int(data['objID'][i])] = galaxy(int(data['objID'][i]), data['ra'][i], data['dec'][i], data['z'][i], 0., 0., data['bpt'][i])
	# This works slightly different when we want to get IDs of nearby galaxies
	else:
		usedKeys = []
		keys = set(data['objID'])
		for key in keys:
			i = np.amin(np.where(data['objID'] == key))
			galaxies[int(data['objID'][i])] = galaxy(int(data['objID'][i]), data['ra'][i], data['dec'][i], data['z'][i], 0., 0., data['bpt'][i])
		# iterate through unique object IDs
		onePercent = math.ceil(len(keys) / 1000)
		j = 0
		k = 0
		for key in keys:
			if j % onePercent == 0:
				print(k * 0.1, "% complete")
				k += 1
			j += 1
			if not key in list(usedKeys):
				tempList = []
				# iterate through whole dataset to gather information from all duplicates of that object
				for i in range(len(data['objID'])):
					if data['objID'][i] == key:
						tempList.append(int(data['nearbyID'][i]))
				galaxies[key].nearbyIDs = tempList
				galaxies[key].nearby = len(tempList)
				usedKeys = usedKeys + tempList

	return galaxies
