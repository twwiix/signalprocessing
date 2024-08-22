import numpy as np
import matplotlib.pyplot as plt

n = 10000
t = np.arange(n)  # Use np.arange for better consistency
k = 10  # Number of poles for generating slow drift

# Generating a slow drift signal
slowdrift = np.interp(np.linspace(1, k, n), np.arange(0, k), 100 * np.random.randn(k))
signal = slowdrift + 20 * np.random.randn(n)

# BIC to find optimal order
orders = range(5, 40)
sse = np.zeros(len(orders))

for i in range(len(orders)):
    yhat = np.polyval(np.polyfit(t, signal, orders[i]), t)
    sse[i] = np.sum((yhat - signal) ** 2) / n
bic = n * np.log(sse) + orders * np.log(n)
bestP = min(bic)
idx = np.argmin(bic)

# Prepare the figure and subplots
fig, ax = plt.subplots(2, 1, figsize=(10, 8))

# Plot BIC
ax[0].plot(orders, bic, 'ks-', label='BIC')
ax[0].plot(orders[idx], bestP, 'ro', label='Best Order')
ax[0].set_xlabel('Polynomial Order')
ax[0].set_ylabel('Bayesian Information Criterion')
ax[0].legend()
ax[0].set_title('Bayesian Information Criterion vs Polynomial Order')

# Filter for best polynomial order
polycofs = np.polyfit(t, signal, orders[idx])
yhat = np.polyval(polycofs, t)
filtsig = signal - yhat

# Plot original, polynomial fit, and filtered signal
ax[1].plot(t, signal, 'b', label='Original')
ax[1].plot(t, yhat, 'r', label='Polynomial Fit')
ax[1].plot(t, filtsig, 'k', label='Filtered Signal')
ax[1].set_xlabel('Time (a.u.)')
ax[1].set_ylabel('Amplitude')
ax[1].legend()
ax[1].set_title('Signal Detrending with Optimal Polynomial Fit')

# Display the plots
plt.tight_layout()
plt.show()
