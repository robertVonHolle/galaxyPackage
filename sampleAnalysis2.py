from galaxy import galaxy
from galaxy.datagen import dataGen
from galaxy.agncount import agnCount
from galaxy.densityplot import densityPlot

# Grab the data to create our dictionary
galaxies = dataGen('galaxyData/galaxy_sample_2.csv')
#sampleGalaxy = 1237645879578460271
print("Generated 'galaxies' dictionary")

# Count each type and total number of AGNs
counts = agnCount(galaxies, printCounts=True)

# Plot the galaxies to make sure we're looking at the right shape
densityPlot(galaxies, 'galaxy_sample_2_nolim_hist2d.png')
