from galaxy.galaxy import galaxy

def agnCount(galaxies, printCounts=False):
	r"""
	Counts the total number of each type of AGN in a set of galaxies

	Parameters
		galaxies - Type: dict. A dictionary of galaxy objects
		printCounts (optional) - Type: bool. Prints agn counts when set to True. Set to False by default

	Returns
		counts - Type: dict. A dictionary holding the number of each type of AGN
	
	AGN Types - These will be used as dictionary keys
		'Seyfert'
		'LINER'
		'Seyfert/LINER'
		'Composite'
		'Total' (this indicates the sum of above numbers)
		'None'
	"""

	counts = {
		'Seyfert'      : 0,
		'LINER'        : 0,
		'Seyfert/LINER': 0,
		'Composite'    : 0,
		'Total'        : 0,
		'None'         : 0}

	# Find counts of AGNs based on flags in galaxy objects
	for key in galaxies:
		if galaxies[key].agn == 0:
			counts['None'] += 1
		elif galaxies[key].agn == 1:
			counts['Seyfert'] += 1
			counts['Total'] += 1
		elif galaxies[key].agn == 2:
			counts['LINER'] += 1
			counts['Total'] += 1
		elif galaxies[key].agn == 3:
			counts['Seyfert/LINER'] += 1
			counts['Total'] += 1
		elif galaxies[key].agn == 4:
			counts['Composite'] += 1
			counts['Total'] += 1
		else:
			raise ValueError("Unexpected AGN value found. AGN values should be in range [0,4]. Got:", galaxy[key].agn, "from galaxy", key)

	# Print the counts of AGNs if desired
	if printCounts:
		print("Seyfert:", counts['Seyfert'])
		print("LINER:", counts['LINER'])
		print("Seyfert/LINER:", counts['Seyfert/LINER'])
		print("Composite:", counts['Composite'])
		print("Total:", counts['Total'])

	return counts
