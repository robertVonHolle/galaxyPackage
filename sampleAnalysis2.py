from galaxy import galaxy
from galaxy.datagen import dataGen
from galaxy.agncount import agnCount
from galaxy.densityplot import densityPlot
from galaxy.nearbyhist import nearbyHist

# Grab the data to create our dictionary
galaxies = dataGen('galaxyData/nearby_gals_2.csv')
#sampleGalaxy = 1237645879578460271
print("Generated 'galaxies' dictionary")

# Count each type and total number of AGNs
counts = agnCount(galaxies, printCounts=True)

# Plot the galaxies to make sure we're looking at the right shape
densityPlot(galaxies, 'plots/galaxy_sample_2_nolim_hist2d.png')

# Plot a histogram of number of nearby galaxies vs percentage with an AGN
nearbyHist(galaxies, 'plots/galaxy_sample_2_nearby_hist_11bins.png', 10)
