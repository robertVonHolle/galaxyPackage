from math import log10
from json import JSONEncoder

class galaxy:
	r"""
	Relevant values for galaxies in the dataset
	"""

	def __init__(self, objId, ra, dec, z, Mr, color, agn, u=0., r=0., nearby=0, nearbyIDs=[]):
		self.objId = objId  	    # Identification number of a galaxy
		self.ra = ra			    # Right ascension of the galaxy in degrees
		self.dec = dec			    # Declination of the galaxy in degrees
		self.z = z				    # Redshift of the galaxy
		self.u = u				    # u-band magnitude of the galaxy
		self.r = r				    # r-band magnitude of the galaxy
		self.Mr = Mr			    # Absolute magnitude of the galaxy
		self.color = color		    # The "color" of the galaxy as denoted by u-r
		self.agn = agn		  	    # A flag indicating the galaxy's classification based on AGN
		self.nearby = nearby        # Number of galaxies "nearby" target galaxy
								    # (definition of "nearby" changes between data sets)
		self.nearbyIDs = nearbyIDs  # A list of IDs of nearby galaxies

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

		Number of galaxies "nearby" the target galaxy
		(definition of "nearby" changes based on data set)
		"""
		return self._nearby

	@nearby.setter
	def nearby(self, value = 0):
		if isinstance(value, int):
			self._nearby = value
		else:
			raise TypeError("Attribute 'nearby' must be type int. Got: %s" % (type(value)))

	@property
	def nearbyIDs(self):
		r"""
		Type: list

		List of IDs of "nearby" galaxies
		(definition of "nearby" changes based on data set)
		"""
		return self._nearbyIDs

	@nearbyIDs.setter
	def nearbyIDs(self, value = []):
		if isinstance(value, list):
			if len(value) != 0 and all(isinstance(x, int) for x in value):
				self._nearbyIDs = value
			elif len(value) == 0:
				self._nearbyIDs = value
			else:
				raise TypeError("Attribute 'nearbyIDs' must be a list of ints.")
		else:
			raise TypeError("Attribute 'nearbyIDs' must be type list. Got %s" % (type(value)))

	def to_json(self): 
		r''' 
		convert the instance of this class to json 
		'''
		return json.dumps(self, indent = 4, default=lambda o: o.__dict__) 
