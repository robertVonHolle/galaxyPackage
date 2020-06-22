from galaxy import galaxy

def isBlue(galaxy):
	r"""
	Determines if a galaxy is blue based on the u-r color divider

	Parameter:
		galaxy - Type: galaxy. The galaxy

	Returns:
		isBlue - Type: bool. True if the galaxy is blue, false if the galaxy is red
	"""

	return galaxy.color < (-0.017 * (galaxy.Mr ** 2)) - (0.146 * galaxy.Mr) + 2.294
