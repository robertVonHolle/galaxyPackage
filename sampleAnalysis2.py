from galaxy import galaxy
from galaxy.datagen import dataGen
from galaxy.dividesample import divideSample
from galaxy.agncount import agnCount
from galaxy.densityplot import densityPlot
from galaxy.nearbyhist import nearbyHist

# Grab the data to create our dictionary
galaxies = dataGen('galaxyData/nearby_gals_2.csv')
#galaxies = dataGen('galaxyData/galaxy_sample_2.csv')
#sampleGalaxy = 1237645879578460271
#for key in galaxies:
#	if key in galaxiesSmall:
#		galaxies[key].nearby = galaxiesSmall[key].nearby
#	else:
#		galaxies[key].nearby = -1  # error flag
print("Generated 'galaxies' dictionary")

#for key in galaxies:
#	keys.append(key)
#	redshifts.append(galaxies[key].z)
#	if not key in galaxiesSmall:
#		print("%s has no nearby neighbors" % str(key))
# print("Lowest redshift galaxy is", keys[redshifts.index(min(redshifts))])

# Divide into red and blue subsections
divideSample(galaxies, 'galaxyData/galaxy_sample_2.csv')
#print("Created blue_file and red_file")

# Count each type and total number of AGNs
counts = agnCount(galaxies, printCounts=True)

# Plot the galaxies to make sure we're looking at the right shape
#densityPlot(galaxies, 'plots/galaxy_sample_2_nolim_hist2d.png')

# Plot a histogram of number of nearby galaxies vs percentage with an AGN
#nearbyHist(galaxies, 'plots/galaxy_sample_2_nearby_hist_11bins.png', 10)
