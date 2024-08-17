#Algorithm Description:
#In Gaussian smoothing filter each data is weighted by a Gaussian function of its neighbors,
#giving more weight to points closer to the center.

import numpy as np
import matplotlib.pyplot as plt

#Step 1: Create the signal
srate= 1000
time= np.arange(0, 3, 1/srate)
n= len(time)
p= 15
noiseamp= 5

ampl= np.interp(np.linspace(1,p,n), np.arange(0,p), np.random.rand(p) * 30)
noise= noiseamp*np.random.randn(n)
signal= ampl+noise

#Step 2: Create the Gaussian Kernel
#full-width half-maximum for the gaussian function
fwhm= 25

k=100
gtime=1000*np.arange(-k,k+1)/srate

#Gaussian window
gauswin= np.exp(-(4*np.log(2)*gtime**2)/fwhm**2)

#Compute empricial fwhm
pstPeakHalf= k+np.argmin((gauswin[k:] - 0.5)**2)
prePeakHalf= np.argmin((gauswin - 0.5)**2)
empFWHM= gtime[pstPeakHalf] - gtime[prePeakHalf]

# Plot the Gaussian window
plt.plot(gtime, gauswin, 'ko-')
plt.plot([gtime[prePeakHalf], gtime[pstPeakHalf]], [gauswin[prePeakHalf], gauswin[pstPeakHalf]], 'm')
plt.xlabel('Time (ms)')
plt.ylabel('Gain')
plt.title(f'Gaussian kernel with requested FWHM {fwhm} ms ({empFWHM:.2f} ms achieved)')
plt.show()

#Step 3: Normalize the Gaussian kernel to unit energy
gauswin= gauswin / np.sum(gauswin)


#Step 4: Apply the Gaussian Filter
filteredsig= np.zeros_like(signal)

for i in range(k, n-k):
	filteredsig[i]= np.sum(signal[i-k:i+k+1] * gauswin)
	
plt.figure(figsize=(12, 6))
plt.plot(time, signal, label='Original Signal')
plt.plot(time, filteredsig, label='Gaussian Filtered Signal', linewidth=2)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.title('Original and Gaussian Filtered Signal')
plt.show()
