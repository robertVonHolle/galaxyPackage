from galaxy import galaxy
from galaxy.isblue import isBlue

def divideSample(galaxies, f):
	r"""
	Divides the sample of galaxies into red and blue populations
	based on the u-r color divider

	Parameters:
		galaxies - Type: dict. A dictionary of all galaxies
		f - Type: str. The name of the file the data was originally pulled from
	
	Returns:
		None, but prints two files, one containing red galaxies and one
			containing blue galaxies
	"""
	f_blue = f[:-4]
	f_blue += "_blue.csv"
	f_red = f[:-4]
	f_red += "_red.csv"

	galaxiesBlue = {}
	galaxiesRed = {}

	for key in galaxies:
		Mr = galaxies[key].Mr
		if isBlue(galaxies[key]):
			galaxiesBlue[key] = galaxies[key]
		else:
			galaxiesRed[key] = galaxies[key]

	blueFile = open(f_blue, 'w')
	blueFile.write("objID,ra,dec,z,redshift,modelMag_u,modelMag_r,bpt,Column1\n")
	for key in galaxiesBlue:
		if galaxiesBlue[key].agn == 1:
			bpt = "Seyfert"
		elif galaxiesBlue[key].agn == 2:
			bpt = "LINER"
		elif galaxiesBlue[key].agn == 3:
			bpt = "Seyfert/LINER"
		elif galaxiesBlue[key].agn == 4:
			bpt = "Composite"
		else:
			bpt = "BLANK"
		blueFile.write(str(key) + "," + str(galaxiesBlue[key].ra) + "," + str(galaxiesBlue[key].dec) + "," + str(galaxiesBlue[key].z) + "," + str(galaxiesBlue[key].redshift) + "," + str(galaxiesBlue[key].u) + "," + str(galaxiesBlue[key].r) + "," + bpt + "," + str(galaxiesBlue[key].nearby) + "\n")
	blueFile.close()

	redFile = open(f_red,'w')
	redFile.write("objID,ra,dec,z,redshift,modelMag_u,modelMag_r,bpt,Column1\n")
	for key in galaxiesRed:
		if galaxiesRed[key].agn == 1:
			bpt = "Seyfert"
		elif galaxiesRed[key].agn == 2:
			bpt = "LINER"
		elif galaxiesRed[key].agn == 3:
			bpt = "Seyfert/LINER"
		elif galaxiesRed[key].agn == 4:
			bpt = "Composite"
		else:
			bpt = "BLANK"
		redFile.write(str(key) + "," + str(galaxiesRed[key].ra) + "," + str(galaxiesRed[key].dec) + "," + str(galaxiesRed[key].z) + "," + str(galaxiesRed[key].redshift) + "," + str(galaxiesRed[key].u) + "," + str(galaxiesRed[key].r) + "," + bpt + "," + str(galaxiesRed[key].nearby) + "\n")
	redFile.close()
