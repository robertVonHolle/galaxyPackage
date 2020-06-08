from math import log10

class galaxy:
	r"""
	Relevant values for galaxies in the dataset
	"""

	def __init__(self, objId, ra, dec, z, redshift, u, r, Mr, color, agn, nearby):
		self.objId = objId
		self.ra = ra
		self.dec = dec
		self.z = z
		self.redshift = redshift
		self.u = u
		self.r = r
		self.Mr = Mr
		self.color = color
		self.agn = agn
		self.nearby = nearby

	@property
	def objId(self):
		r"""
		Type: int

		Identification number of the galaxy
		"""
		return self._objId
	
	@objId.setter
	def objId(self, value):
		if isinstance(value, int):
			self._objId = value
		else:
			raise TypeError("Attribute 'objId' must be type int. Got: %s" % (type(value)))

	@property
	def ra(self):
		r"""
		Type: float

		Right ascension of the galaxy in degrees
		"""
		return self._ra

	@ra.setter
	def ra(self, value):
		if isinstance(value, float):
			self._ra = value
		else:
			raise TypeError("Attribute 'ra' must be type float. Got: %s" % (type(value)))
	
	@property
	def dec(self):
		r"""
		Type: float

		Declination of the galaxy in degrees
		"""
		return self._dec

	@dec.setter
	def dec(self, value):
		if isinstance(value, float):
			self._dec = value
		else:
			raise TypeError("Attribute 'dec' must be type float. Got: %s" % (type(value)))

	@property
	def z(self):
		r"""
		Type: float

		Redshift of the galaxy
		"""
		return self._z

	@z.setter
	def z(self, value):
		if isinstance(value, float):
			self._z = value
		else:
			raise TypeError("Attribute 'z' must be type float. Got: %s" % (type(value)))

	@property
	def redshift(self):
		r"""
		Type: float

		GANDALF-corrected redshift of the galaxy
		"""
		return self._redshift

	@redshift.setter
	def redshift(self, value):
		if isinstance(value, float):
			self._redshift = value
		else:
			raise TypeError("Attribute 'redshift' must be type float. Got: %s" % (type(value)))

	@property
	def u(self):
		r"""
		Type: float

		u-band magnitude of the galaxy
		"""
		return self._u

	@u.setter
	def u(self, value):
		if isinstance(value, float):
			self._u = value
		else:
			raise TypeError("Attribute 'u' must be type float. Got: %s" % (type(value)))

	@property
	def r(self):
		r"""
		Type: float

		r-band magnitude of the galaxy
		"""
		return self._r

	@r.setter
	def r(self, value):
		if isinstance(value, float):
			self._r = value
		else:
			raise TypeError("Attribute 'r' must be type float. Got: %s" % (type(value)))

	@property
	def Mr(self):
		r"""
		Type: float

		Absolute magnitude of the galaxy
		"""
		return self._Mr

	@Mr.setter
	def Mr(self, value):
		self._Mr = self.r - 43.23 - (5 * log10(self.z)) - (1.662 * self.z)

	@property
	def color(self):
		r"""
		Type: float

		The \"color\" of a galaxy as denoted by u - r.
		"""
		return self._color

	@color.setter
	def color(self, value):
		r"""
		Sets the color of a galaxy based on entered values of u and r.

		Please only call if u and r for this galaxy have been set.
		"""
		self._color = self._u - self._r

	@property
	def agn(self):
		r"""
		Type: int

		A flag indicating the galaxy's classification based on AGN
		0 = no AGN
		1 = Seyfert galaxy
		2 = LINER galaxy
		3 = Seyfert/LINER
		4 = Composite galaxy

		NOTE: The input to set the value of AGN must be a string. The value will be set as follows:
		agn = 1 if input = \"Seyfert\"
		agn = 2 if input = \"LINER\"
		agn = 3 if input = \"Seyfert/LINER\"
		agn = 4 if input = \"Composite\"
		agn = 0 for any other string input
		"""
		return self._agn

	@agn.setter
	def agn(self, value):
		if isinstance(value, str):
			if value == "Seyfert":
				self._agn = 1
			elif value == "LINER":
				self._agn = 2
			elif value == "Seyfert/LINER":
				self._agn = 3
			elif value == "Composite":
				self._agn = 4
			else:
				self._agn = 0
		else:
			raise TypeError("Attribute 'agn' must be type str. Got: %s" % (type(value)))

	@property
	def nearby(self):
		r"""
		Type: int

		Number of galaxies within 1 pc of the target galaxy
		"""
		return self._nearby

	@nearby.setter
	def nearby(self, value):
		if isinstance(value, int):
			self._nearby = value
		else:
			raise TypeError("Attribute 'nearby' must be type int. Got: %s" % (type(value)))
