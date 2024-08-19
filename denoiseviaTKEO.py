#Algorithm Description:
#The TKEO algorithm is a straightforward method for denoising signas, in this
#applciation, we will denoise an EMG signa. The essence of the TKEO algorithm
#is to amplify the energy of the true signal while supressing the noise.

import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio
import copy

emgdata= sio.loadmat('emg4TKEO.mat')
emgtime= emgdata['emgtime'][0]
emg= emgdata['emg'][0]

#Initialize the filtered signal with a copy of the original singla
emgf= copy.deepcopy(emg)

#Aplyl TKEO algorithm (Loop version), loop through each point exluding the first and last points
for i in range(1, len(emgf) - 1):
	emgf[i]= emg[i]**2 - emg[i-1]*emg[i+1]

#Create another copy of the original signal for vectorized computation
emgf2= copy.deepcopy(emg)
#Apply the TKEO formula in vectorized operations for speed
emgf2[1:-1]= emg[1:-1]**2 - emg[0:-2]*emg[2:]

#convert both signals to zscore
#find the index of the time point closest to zero
time0= np.argmin(emgtime**2)

#convert original EMG to zscore based on the pre-zero period
emgZero= (emg - np.mean(emg[:time0])) / np.std(emg[:time0])

#convert filtered EMG to zscore based on the pre-zero period
emgZf= (emgf - np.mean(emgf[:time0])) / np.std(emgf[:time0])

#plot the raw signal (normalized to max value)
plt.plot(emgtime, emg / np.max(emg), 'b', label='EMG')
plt.plot(emgtime, emgf / np.max(emgf), 'm', label= 'TKEO energy')
plt.xlabel('Time (ms)')
plt.ylabel('Amplitude or energy')
plt.legend()
plt.show()

# Plot the z-scored signals
plt.plot(emgtime, emgZero, 'b', label='EMG')
plt.plot(emgtime, emgZf, 'm', label='TKEO energy')
plt.xlabel('Time (ms)')
plt.ylabel('Z-score relative to pre-stimulus')
plt.legend()
plt.show()


