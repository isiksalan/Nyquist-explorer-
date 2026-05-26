Nyquist Sampling Explorer
An interactive Python tool for visualizing the Nyquist sampling theorem, aliasing, and ideal sinc reconstruction.
This project shows how a continuous sine wave is sampled at different sampling frequencies. A slider allows the user to change the sampling rate and immediately see whether the signal is undersampled, sampled exactly at the Nyquist rate, or sampled above the Nyquist rate.
Features
Interactive sampling frequency slider
Visualization of the original analog sine wave
Discrete sample points shown on the signal
Ideal sinc reconstruction from the samples
Automatic status display:
`ALIASING` when sampling below Nyquist
`AT Nyquist` when sampling exactly at the Nyquist rate
`OK` when sampling above Nyquist
Background
According to the Nyquist-Shannon sampling theorem, a bandlimited signal can be perfectly reconstructed from its samples if the sampling frequency is greater than twice the highest frequency component of the signal.
For a sine wave with frequency:
```text
f_signal = 5 Hz
```
the Nyquist rate is:
```text
2 × f_signal = 10 Hz
```
Sampling below this rate causes aliasing, meaning the reconstructed signal no longer correctly represents the original signal.
Requirements
Install the required Python packages:
```bash
pip install numpy matplotlib
```
How to Run
Run the Python script:
```bash
python nyquist_explorer.py
```
An interactive plot will open. Move the slider to change the sampling frequency.
Code Overview
The script uses:
`numpy` for signal generation and numerical operations
`matplotlib` for plotting
`matplotlib.widgets.Slider` for interactive control
Main functions:
```python
sample(fs)
```
Generates sample times and sample values for a given sampling frequency.
```python
reconstruct(t_s, x_s, t_query)
```
Performs ideal sinc reconstruction using the Whittaker-Shannon interpolation formula.
Example
The default signal is a 5 Hz sine wave with phase:
```python
phi = np.pi / 2
```
The initial sampling frequency is set exactly at the Nyquist rate:
```python
fs_init = 2 * f_sig
```
You can modify `f_sig`, `T`, or `phi` in the script to explore different cases.
Educational Purpose
This project is intended as a simple educational visualization for understanding:
Sampling
Nyquist rate
Aliasing
Sinc interpolation
Signal reconstruction
Suggested Repository Description
Interactive Python visualization of the Nyquist sampling theorem, aliasing, and ideal sinc reconstruction using Matplotlib sliders.
License
This project is open source. You may add a license such as MIT if you want others to freely use and modify it.
