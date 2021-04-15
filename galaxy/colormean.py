from galaxy import galaxy
import math
import numpy as np

def colorMean(galaxies, f):
	r"""
	Finds mean and standard deviation of galaxy sample as function of absolute magnitude

	Parameters:
		galaxies - Type: dict. The dictionary of galaxies
		f - Type: str. The name of the file to be written to

	Returns: None
	"""
	withAGN = [i for i in galaxies if galaxies[i].agn != 0]
	withoutAGN = [i for i in galaxies if galaxies[i].agn == 0]
	listList = [withAGN, withoutAGN]

	meanFile = open(f,'w')

	for item in listList:
		if item == withAGN:
			meanFile.write("Galaxies with AGN:\n")
		else:
			meanFile.write("Galaxies without AGN:\n")
		for i in range(5):  # Iterate by number of neighbors
			meanFile.write("Nearby neighbors: "+str(i)+"\n")
			for j in range(4):  # Iterate by magnitude group
				tot_group = np.array([galaxies[k].color for k in item if galaxies[k].nearby == i])
				meanFile.write("Total mean: "+str(np.mean(tot_group)))
				meanFile.write("Total STD: "+str(np.std(tot_group))) 
				top = -17 - (1.75 * j)
				bottom = -17 - (1.75 *(j + 1))
				group = np.array([galaxies[k].color for k in item if galaxies[k].nearby == i and galaxies[k].Mr <= top and galaxies[k].Mr >= bottom])
				meanFile.write("Mean for magnitude range "+str(bottom)+" <= x <= "+str(top)+": "+str(np.mean(group))+"\n")
				meanFile.write("STD for magnitude range "+str(bottom)+" <= x <= "+str(top)+": "+str(np.std(group))+"\n")
	meanFile.close()
	print("Wrote meanFile")
