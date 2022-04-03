import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

"""
parameters: 
rhp - spectral noise density unit/SQRT(Hz)
sr  - sample rate
n   - no of points
mu  - mean value, optional

returns:
n points of noise signal with spectral noise density of rho
"""


def white_noise(rho, sr, n, mu=0):
    sigma = rho * np.sqrt(sr/2)
    noise = np.random.normal(mu, sigma, n)
    return noise


rho = 1
sr = 1000
n = 1000
period = n/sr
time = np.linspace(0, period, n)
signal_pure = 100*np.sin(2*np.pi*13*time)
noise = white_noise(rho, sr, n)
signal_with_noise = signal_pure + noise

f, psd = signal.periodogram(signal_with_noise, sr)

print("Mean spectral noise density = ", np.sqrt(
    np.mean(psd[50:])), "arb.u/SQRT(Hz)")

plt.plot(time, signal_with_noise)
plt.plot(time, signal_pure)
plt.xlabel("time (s)")
plt.ylabel("signal (arb.u.)")
plt.show()

# plt.semilogy(f[1:], np.sqrt(psd[1:]))
# plt.xlabel("frequency (Hz)")
# plt.ylabel("psd (arb.u./SQRT(Hz))")
# #plt.axvline(13, ls="dashed", color="g")
# plt.axhline(rho, ls="dashed", color="r")
# plt.show()
