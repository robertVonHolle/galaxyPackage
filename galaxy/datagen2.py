import numpy as np
import pandas as pd
import math
from astropy.utils.console import ProgressBar
from galaxy.galaxy import galaxy

def dataGen2(f):
	r"""
	Generates a dictionary of galaxy objects from a file

	Parameters
		f - Type: str. The name of the file

	Returns
		galaxies - Type: dict. A dictionary of galaxy objects with object IDs as keys
	"""

	data = pd.read_csv(f)
	#print(data['objID'])

	galaxies = {}
	if not 'nearbyID' in data.columns:    # As of now, this column is always included in datasets not
										  # including object IDs of nearby galaxies and never in
										  # data sets that do include them
		print("If this shows up, it's a problem")   # Debug
		return ValueError()
		# Include number of nearby neighbors if it is present
		if 'modelMag_u' in data.columns:
			if 'Column1' in data.columns:
				for i in range(len(data['objID'])):
					galaxies[int(data['objID'][i])] = galaxy(int(data['objID'][i]), data['ra'][i], data['dec'][i], data['z'][i], 0., 0., data['bpt'][i], u=data['modelMag_u'][i], r=data['modelMag_r'][i], nearby=(int(data['Column1'][i])-1))
			# Exclude number of nearby neighbors if it is not present
			else:
				for i in range(len(data['objID'])):
					galaxies[int(data['objID'][i])] = galaxy(int(data['objID'][i]), data['ra'][i], data['dec'][i], data['z'][i], 0., 0., data['bpt'][i], u=data['modelMag_u'][i], r=data['modelMag_r'][i])
		else:
			if 'Column1' in data.columns:
				for i in range(len(data['objID'])):
					galaxies[int(data['objID'][i])] = galaxy(int(data['objID'][i]), data['ra'][i], data['dec'][i], data['z'][i], 0., 0., data['bpt'][i],  nearby=(int(data['Column1'][i])-1))
			# Exclude number of nearby neighbors if it is not present
			else:
				for i in range(len(data['objID'])):
					galaxies[int(data['objID'][i])] = galaxy(int(data['objID'][i]), data['ra'][i], data['dec'][i], data['z'][i], 0., 0., data['bpt'][i])
	# This works slightly different when we want to get IDs of nearby galaxies
	else:
		sampleKey = 1237645879551066262   # Debug
		sampleKey2 = 1237645941824356443   # Debug
		print("Checkpoint 1")   # Debug
		bar = ProgressBar(len(data['objID']))
		for i in range(len(data['objID'])):
			objid = int(data['objID'][i])
			nearID = int(data['nearbyID'][i])
			#if data['nearbyID'][i] in data['objID']:
			if objid in galaxies:
				print("\nCheckpoint 2")   # Debug
				print("Target ID:",objid)   # Debug
				print("Nearby ID:",nearID)   # Debug
				print("Key 1:", galaxies[objid].nearbyIDs)   # Debug
				galaxies[objid].nearbyIDs.append(nearID)
				print("Key 1:", galaxies[objid].objId)   # Debug
				print("Key 1:", galaxies[objid].nearbyIDs)   # Debug
				#print("Key 1:", galaxies[sampleKey].nearbyIDs)   # Debug
				if sampleKey2 in galaxies:   # Debug
					print("Found key 2!")   # Debug
					print("Key 2:", galaxies[sampleKey2].nearbyIDs)   # Debug
			else:
				print("\nCheckpoint 3")   # Debug
				print("Target ID:",objid)   # Debug
				print("Nearby ID:",nearID)   # Debug
				galaxies[objid] = galaxy(objid, data['ra'][i], data['dec'][i], data['z'][i], 0., 0., data['bpt'][i])
				#galaxies[objID].nearbyIDs.append(nearID)
				print("Key 1:", galaxies[sampleKey].nearbyIDs)   # Debug
				if sampleKey2 in galaxies:
					print("Found key 2!")   # Debug
					print("Key 2:", galaxies[sampleKey2].nearbyIDs)   # Debug
			bar.update()
			del objid
			del nearID

		print("\n")
		for key in galaxies:  # Iterate through dictionary of galaxies
			galaxies[key].nearby = len(galaxies[key].nearbyIDs)  # Set number of nearby neighbors as length of list of nearby neighbors

		print("Key 1 before pass:", galaxies[sampleKey].nearbyIDs)   # Debug
		print("Key 1 Mr before pass:", galaxies[sampleKey].u)   # Debug
		print("Key 2 before pass:", galaxies[sampleKey2].nearbyIDs)   # Debug

	return galaxies
