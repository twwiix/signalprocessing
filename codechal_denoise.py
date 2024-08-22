import scipy.io
import scipy.signal
import matplotlib.pyplot as plt
import numpy as np
import copy



n=4000
time= np.arange(1, n+1)

file = 'denoising_codeChallenge.mat'
data = scipy.io.loadmat(file)


origsig = data['origSignal'].flatten()

filtsig= copy.deepcopy(origsig)

suprthr = np.where (origsig>5) [0]

k=5

for i in range(len(suprthr)):
	lowbnd= np.max((0,suprthr[i]-k))
	uppbnd= np.min((suprthr[i]+k+1, n))
	filtsig[suprthr[i]]= np.median(origsig[lowbnd:uppbnd])
	
suprthr = np.where (origsig<-5)[0]

k=5

for i in range(len(suprthr)):
	lowbnd= np.max((0,suprthr[i]-k))
	uppbnd= np.min((suprthr[i]+k+1, n))
	filtsig[suprthr[i]]= np.median(origsig[lowbnd:uppbnd])
	
k=150
for i in range(n):
	filtsig[i] = np.mean(filtsig[max(0, i-k): min(n, i+k+1)])
# Plot the results
plt.figure(figsize=(12, 8))

# Subplot 1: Original Signal
plt.subplot(2, 1, 1)
plt.plot(time, origsig, label='Original Signal', color='blue', linewidth=1.5)
plt.title('Original Signal')
plt.xlabel('Time (sec.)')
plt.ylabel('Amplitude')
plt.grid(True)

# Subplot 2: After Linear Detrending + Median Filtering
plt.subplot(2, 1, 2)
plt.plot(time, filtsig, label='Clean signal', color='green', linewidth=1.5)
plt.title('Filtered signal')
plt.xlabel('Time (sec.)')
plt.ylabel('Amplitude')
plt.grid(True)


# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plots
plt.show()
