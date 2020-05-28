from galaxy import galaxy
from galaxy.datagen import dataGen
import matplotlib.pyplot as plt

# Grab the data to create our dictionary
galaxies = dataGen('galaxyData/galaxy_sample_2.csv')
sampleGalaxy = 1237645879578460271
print("Generated 'galaxies' dictionary")

# Debug checks. Feel free to comment/uncomment these as necessary
print(galaxies[sampleGalaxy].objId)
print(galaxies[sampleGalaxy].ra)
print(galaxies[sampleGalaxy].dec)
print(galaxies[sampleGalaxy].z)
print(galaxies[sampleGalaxy].redshift)
print(galaxies[sampleGalaxy].u)
print(galaxies[sampleGalaxy].r)
print(galaxies[sampleGalaxy].Mr)
print(galaxies[sampleGalaxy].color)
print(galaxies[sampleGalaxy].agn)

# We're only interested in galaxies with color >0. Figure out the others later
galaxyList = list(galaxies.values())
color = []
Mr = []

for galaxy in galaxyList:
	color.append(galaxy.color)
	Mr.append(galaxy.Mr)

elem = 0
for i in color:
	if i <= 0:
		Mr.remove(Mr[color.index(i)])
		color.remove(i)
		print("Removed element")
		elem += 1
print(elem)

# Plot the remaining galaxies to make sure we're looking at the right shape
plt.plot(color, Mr, 'o')
plt.gca().invert_yaxis()
plt.xlim(0.5,4)
plt.ylim(-18,-24)
plt.savefig('galaxy_sample_2_plot.png')
print("Created galaxy plot")
