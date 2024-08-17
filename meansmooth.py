#Algorithm description:
#The running mean filter is a powerful tool for reducing the noise and smoothing a time series data.
#The core idea of the Algorithm is to replace is each data point with the average of its neighboring
#data points. This will help to smooth out fluctuations caused by noise, making the underlying data
#more visible.

import numpy as np
import matplotlib.pyplot as plt

#Create a signal
srate= 1000
time= np.arange(0,3,1/srate)
n=len(time)
p=15

#noise level
noiseAmp= 5

#noise the signal
ampmod= np.interp(np.linspace(0,p,n), np.arange(0,p), np.random.rand(p)*30) #Amplitude modulator using linear interpolation
noise= noiseAmp*np.random.randn(n) #Gaussian noise added to the signal
signal= ampmod + noise #Combination of amplitude modulator and noise 

#initialize the filtered signal vector
filtsig= np.zeros(n)

#implement the filter
k=20 
for i in range(k, n-k):
	#each point is the average of k surroundings points
	filtsig[i]= np.mean(signal[i-k:i+k+1])

#convert window size from points to miliseconds
windowsize=1000*(k*2+1)/srate

#ploting
plt.plot(time,signal, label='Original Signal')
plt.plot(time,filtsig, label='Filtered Signal')

plt.legend()
plt.xlabel('Time (sec)')
plt.ylabel('Amplitude')
plt.title(f'Running-mean filter with a k=%d-ms filter' %windowsize)
plt.show()


