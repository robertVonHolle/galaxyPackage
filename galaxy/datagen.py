import numpy as np
import pandas as pd
import math
from astropy.utils.console import ProgressBar
from galaxy.galaxy import galaxy

def dataGen(f):
	r"""
	Generates a dictionary of galaxy objects from a file

	Parameters
		f - Type: str. The name of the file

	Returns
		data - Type: pandas dataframe. The full set of data
		galaxies - Type: dict. A dictionary of galaxy objects with object IDs as keys
	"""

	data = np.genfromtxt(f, dtype=None, delimiter=",", names=True, encoding=None)
	#print(data['objID'])

	galaxies = {}
	bar = ProgressBar(len(data['objID']))
	if not 'nearbyID' in data.dtype.names:    # As of now, this column is always included in datasets not
										  # including object IDs of nearby galaxies and never in
										  # data sets that do include them

		# Include number of nearby neighbors if it is present
		if 'modelMag_u' in data.dtype.names:
			if 'Column1' in data.dtype.names:
				for i in range(len(data['objID'])):
					galaxies[int(data['objID'][i])] = galaxy(int(data['objID'][i]), data['ra'][i], data['dec'][i], data['z'][i], 0., 0., data['bpt'][i], u=data['modelMag_u'][i], r=data['modelMag_r'][i], nearby=(int(data['Column1'][i])-1))
					bar.update()
			# Exclude number of nearby neighbors if it is not present
			else:
				for i in range(len(data['objID'])):
					galaxies[int(data['objID'][i])] = galaxy(int(data['objID'][i]), data['ra'][i], data['dec'][i], data['z'][i], 0., 0., data['bpt'][i], u=data['modelMag_u'][i], r=data['modelMag_r'][i])
					bar.update()
		else:
			if 'Column1' in data.dtype.names:
				for i in range(len(data['objID'])):
					galaxies[int(data['objID'][i])] = galaxy(int(data['objID'][i]), data['ra'][i], data['dec'][i], data['z'][i], 0., 0., data['bpt'][i],  nearby=(int(data['Column1'][i])-1))
					bar.update()
			# Exclude number of nearby neighbors if it is not present
			else:
				for i in range(len(data['objID'])):
					galaxies[int(data['objID'][i])] = galaxy(int(data['objID'][i]), data['ra'][i], data['dec'][i], data['z'][i], 0., 0., data['bpt'][i])
					bar.update()
	# This works slightly different when we want to get IDs of nearby galaxies
	else:
		nearby_gals = []
		for i in range(len(data['objID'])):
			objid = int(data['objID'][i])
			nearID = int(data['nearbyID'][i])
			if data['nearbyID'][i] in data['objID']:
				if objid in galaxies:
					nearby_gals.append(nearID)
				else:
					galaxies[objid] = galaxy(objid, data['ra'][i], data['dec'][i], data['z'][i], 0., 0., data['bpt'][i])
			elif not objid in galaxies:
				galaxies[objid] = galaxy(objid, data['ra'][i], data['dec'][i], data['z'][i], 0., 0., data['bpt'][i])
			if i >= len(data['objID']) - 1 or data['objID'][i] != data['objID'][i+1]:
				galaxies[objid].nearbyIDs = nearby_gals
				nearby_gals = []
			bar.update()

		print("\n")
		for key in galaxies:  # Iterate through dictionary of galaxies
			galaxies[key].nearby = len(galaxies[key].nearbyIDs)  # Set number of nearby neighbors as length of list of nearby neighbors

	return galaxies
