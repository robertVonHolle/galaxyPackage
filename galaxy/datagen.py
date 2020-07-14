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
		onePercent = math.ceil(len(data['objID']) / 100)  # Find what is approximately 1% completion
		j = 0  # Completion tracker
		for i in range(len(data['objID'])):  # Iterate through every row in data table
			if i % onePercent == 0:  # Check if it's time to update completion percentage
				print(j, "% complete")  # Update completion percentage
				j += 1  # Iterate completion tracker
			if int(data['objID'][i]) in galaxies:  # Check if I already have data for this target galaxy
				if data['nearbyID'][i] in data['objID']:  # Check if I have data on this nearby galaxy in my data table
					galaxies[int(data['objID'][i])].nearbyIDs.append(int(data['nearbyID'][i]))  # Add this nearby galaxy to list of galaxies nearby target
			else:  # If I don't already have data on this target galaxy...
				galaxies[int(data['objID'][i])] = galaxy(int(data['objID'][i]), data['ra'][i], data['dec'][i], data['z'][i], 0., 0., data['bpt'][i], nearby=0)  # Grab all data from this row
				if data['nearbyID'][i] in data['objID']:  # Check if I have data on this nearby galaxy in my data table
					galaxies[int(data['objID'][i])].nearbyIDs.append(int(data['nearbyID'][i]))  # Add this nearby galaxy to list of galaxies nearby target

		for key in galaxies:  # Iterate through dictionary of galaxies
			galaxies[key].nearby = len(galaxies[key].nearbyIDs)  # Set number of nearby neighbors as length of list of nearby neighbors

	return galaxies
