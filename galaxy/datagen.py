import numpy as np
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
	# Include number of nearby neighbors if it is present
	if data.dtype.names[-1] == 'Column1':
		for i in range(len(data['objID'])):
			galaxies[int(data['objID'][i])] = galaxy(int(data['objID'][i]), data['ra'][i], data['dec'][i], data['z'][i], data['redshift'][i], data['modelMag_u'][i], data['modelMag_r'][i], 0., 0., data['bpt'][i], int(data['Column1'][i] - 1))
	# Exclude number of nearby neighbors if it is not present
	else:
		for i in range(len(data['objID'])):
			galaxies[int(data['objID'][i])] = galaxy(int(data['objID'][i]), data['ra'][i], data['dec'][i], data['z'][i], data['redshift'][i], data['modelMag_u'][i], data['modelMag_r'][i], 0., 0., data['bpt'][i])

	return galaxies
