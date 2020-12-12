import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

withAGN = pd.read_csv('galaxyData/withAGN.csv')
plt.figure(figsize=(8,6))
sns.ecdfplot(withAGN, x="color", hue="numNear")
plt.axis([1,4,0,1])
plt.savefig("plots/CDFwithAGN.png")
plt.clf()

withoutAGN = pd.read_csv('galaxyData/withoutAGN.csv')
plt.figure(figsize=(8,6))
sns.ecdfplot(withoutAGN, x="color", hue="numNear")
plt.axis([1,4,0,1])
plt.savefig("plots/CDFwithoutAGN.png")
plt.clf()

## Plot colorZeroes
#colorZeroes = pd.read_csv('galaxyData/colorZeroes.csv')
#plt.figure(figsize=(8,6))
#sns.ecdfplot(colorZeroes, x="color", hue="AGN")
#plt.savefig("plots/colorZeroesCDF.png")
#plt.clf()
#
## Plot colorOnes
#colorOnes = pd.read_csv('galaxyData/colorOnes.csv')
#plt.figure(figsize=(8,6))
#sns.ecdfplot(colorOnes, x="color", hue="AGN")
#plt.savefig("plots/colorOnesCDF.png")
#plt.clf()
#
## Plot colorTwos
#colorTwos = pd.read_csv('galaxyData/colorTwos.csv')
#plt.figure(figsize=(8,6))
#sns.ecdfplot(colorTwos, x="color", hue="AGN")
#plt.savefig("plots/colorTwosCDF.png")
#plt.clf()
#
## Plot colorThrees
#colorThrees = pd.read_csv('galaxyData/colorThrees.csv')
#plt.figure(figsize=(8,6))
#sns.ecdfplot(colorThrees, x="color", hue="AGN")
#plt.savefig("plots/colorThreesCDF.png")
#plt.clf()
#
## Plot colorFours
#colorFours = pd.read_csv('galaxyData/colorFours.csv')
#plt.figure(figsize=(8,6))
#sns.ecdfplot(colorFours, x="color", hue="AGN")
#plt.savefig("plots/colorFoursCDF.png")
#plt.clf()
