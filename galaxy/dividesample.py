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
	f_blue += "_blue.csv"  # The file blue galaxies will be written to
	f_red = f[:-4]
	f_red += "_red.csv"    # The file red galaxies will be written to

	galaxiesBlue = {}
	galaxiesRed = {}

	# Create lists of red and blue galaxies using isBlue function
	for key in galaxies:
		Mr = galaxies[key].Mr
		if isBlue(galaxies[key]):
			galaxiesBlue[key] = galaxies[key]
		else:
			galaxiesRed[key] = galaxies[key]

	print("Red galaxies:", len(galaxiesRed))
	print("Blue galaxies:", len(galaxiesBlue))

	# Write the blue file
	blueFile = open(f_blue, 'w')
	blueFile.write("objID,ra,dec,z,redshift,modelMag_u,modelMag_r,bpt,Column1\n")
	for key in galaxiesBlue:
	# First, expand AGN flag to appropriate classification
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

	# Write the red file
	redFile = open(f_red,'w')
	redFile.write("objID,ra,dec,z,redshift,modelMag_u,modelMag_r,bpt,Column1\n")
	for key in galaxiesRed:
	# First, expand AGN flag to appropriate classification
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
