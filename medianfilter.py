#Algorithm Description:
#The Median Filter is filtering technique to remove spikes or outliers from a signal.
#Basically the algorithm replaces each spike with the median of the surroundings data
#points.

import numpy as np
import matplotlib.pyplot as plt
import copy

#Step 1: Create the Signal
n= 2000
signal= np.cumsum(np.random.randn(n))

#Step 2: Introduce Noise (Spikes)
propnoise= .05
noisepnts= np.random.permutation(n)
noisepnts= noisepnts[0:int(n*propnoise)]
signal[noisepnts]= 50 + np.random.rand(len(noisepnts)) * 100

#Step 3: Visualisze the Signal to select a threshold
plt.hist(signal, 100)
plt.show()

threshold= 40

#Step 4: Indentify and filter out Spikes
findspikes= np.where(signal > threshold)[0]
filtsig= copy.deepcopy(signal)

k=20

for ti in range(len(findspikes)):
	lowbnd= np.max((0, findspikes[ti] -k ))
	uppbnd= np.min((findspikes[ti] + k + 1, n))
	
	filtsig[findspikes[ti]]= np.median(signal[lowbnd:uppbnd])

#Step 5: Plot the original and filtered Signal
plt.plot(range(0,n), signal, range(0,n), filtsig)
plt.show()
