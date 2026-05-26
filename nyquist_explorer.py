# -*- coding: utf-8 -*-
"""
Created on Wed May 20 16:57:50 2026

@author: isiks100
"""

# %% Nyquist explorer
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# --- signal parameters ---
f_sig = 5.0          # Hz, frequency of the "analog" sine
T = 1.0              # seconds, total duration to display
fs_cont = 2000       # "continuous" reference sampling (just for the smooth curve)

# dense time vector representing the true analog signal
t_cont = np.linspace(0, T, int(fs_cont * T), endpoint=False)

phi = np.pi/2   # try np.pi/2 to see peaks captured exactly
x_cont = np.sin(2 * np.pi * f_sig * t_cont + phi)

# --- figure layout ---
fig, ax = plt.subplots(figsize=(10, 5))
plt.subplots_adjust(bottom=0.25)   # leave room for the slider

# the true analog signal (smooth)
(line_cont,) = ax.plot(t_cont, x_cont, lw=1.2, alpha=0.6, label=f'analog: {f_sig} Hz')

# initial sampling rate: exactly Nyquist (2*f_sig)
fs_init = 2 * f_sig

def sample(fs):
    """Return sample times and sample values at sampling rate fs."""
    n = int(fs * T)
    t_s = np.arange(n) / fs
    x_s = np.sin(2 * np.pi * f_sig * t_s + phi)
    return t_s, x_s

def reconstruct(t_s, x_s, t_query):
    """Ideal sinc (Whittaker-Shannon) reconstruction from samples."""
    fs = 1 / (t_s[1] - t_s[0])
    # broadcast: (len(t_query), len(t_s))
    T_mat = t_query[:, None] - t_s[None, :]
    return np.sum(x_s[None, :] * np.sinc(fs * T_mat), axis=1)

t_s, x_s = sample(fs_init)
x_recon = reconstruct(t_s, x_s, t_cont)

(stem_line,) = ax.plot(t_s, x_s, 'o', ms=7, color='C3', label='samples')
(recon_line,) = ax.plot(t_cont, x_recon, '--', lw=1.5, color='C2',
                        label='sinc reconstruction')

ax.set_xlabel('time [s]')
ax.set_ylabel('amplitude')
ax.set_title(f'fs = {fs_init:.2f} Hz   (Nyquist rate = {2*f_sig:.2f} Hz)')
ax.set_ylim(-1.6, 1.6)
ax.grid(True, alpha=0.3)
ax.legend(loc='upper right')

# --- slider ---
ax_slider = plt.axes([0.15, 0.08, 0.7, 0.04])
slider = Slider(ax_slider, 'fs [Hz]', valmin=1.0, valmax=10*f_sig,
                valinit=fs_init, valstep=0.1)

def update(val):
    fs = slider.val
    t_s, x_s = sample(fs)
    x_recon = reconstruct(t_s, x_s, t_cont)
    stem_line.set_data(t_s, x_s)
    recon_line.set_data(t_cont, x_recon)
    ratio = fs / (2 * f_sig)
    status = 'ALIASING' if fs < 2*f_sig else ('AT Nyquist' if np.isclose(fs, 2*f_sig) else 'OK')
    ax.set_title(f'fs = {fs:.2f} Hz   ({ratio:.2f}× Nyquist)   →  {status}')
    fig.canvas.draw_idle()

slider.on_changed(update)

plt.show(block=True)