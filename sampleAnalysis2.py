from galaxy import galaxy
from galaxy.datagen import dataGen
from galaxy.agncount import agnCount
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

# Grab the data to create our dictionary
galaxies = dataGen('galaxyData/galaxy_sample_2.csv')
sampleGalaxy = 1237645879578460271
print("Generated 'galaxies' dictionary")

# Debug checks. Feel free to comment/uncomment these as necessary
#print(galaxies[sampleGalaxy].objId)
#print(galaxies[sampleGalaxy].ra)
#print(galaxies[sampleGalaxy].dec)
#print(galaxies[sampleGalaxy].z)
#print(galaxies[sampleGalaxy].redshift)
#print(galaxies[sampleGalaxy].u)
#print(galaxies[sampleGalaxy].r)
#print(galaxies[sampleGalaxy].Mr)
#print(galaxies[sampleGalaxy].color)
#print(galaxies[sampleGalaxy].agn)

counts = agnCount(galaxies, printCounts=True)

# We're only interested in galaxies with color >0. Figure out the others later
galaxyList = list(galaxies.values())
color = []
Mr = []

elem = 0
for galaxy in galaxyList:
	if galaxy.color >= 0:
		color.append(galaxy.color)
		Mr.append(galaxy.Mr)
#	else:
#		print("Removing object:", galaxy.objId)
#		elem += 1
#print("Removed %s objects" % (elem))

# Plot the remaining galaxies to make sure we're looking at the right shape
plt.hist2d(color, Mr, bins=250, norm=LogNorm(), cmin=1, cmap=plt.cm.inferno)
plt.gca().invert_yaxis()
plt.xlim(0.5,4)
plt.ylim(-18,-24)
plt.colorbar()
plt.savefig('galaxy_sample_2_hist2d.png')
print("Created galaxy plot")
