from galaxy import galaxy

def isBlue(galaxy):
	r"""
	Determines if a galaxy is blue based on the u-r color divider

	Parameter:
		galaxy - Type: galaxy. The galaxy

	Returns:
		isBlue - Type: bool. True if the galaxy is blue, false if the galaxy is red
	"""

	Mr = galaxy.Mr + 21

	return galaxy.color < (-0.018 * Mr**2) - (0.137 * Mr) + 2.20
