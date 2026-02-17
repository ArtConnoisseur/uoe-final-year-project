import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import mne
import os 

matplotlib.use("TkAgg")

def plot_single_signal_channel(signals, signal_headers, channel):
    channel = 0
    signal = signals[channel]
    fs = signal_headers[channel]['sample_frequency']
    duration = len(signal) / fs
    time = np.linspace(0, duration, len(signal))

    plt.figure(figsize=(12, 4))
    plt.plot(time, signal)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title(signal_headers[channel]['label'])
    plt.grid(True)
    plt.show()

def plot_all_signals(signals, signal_headers):
    n_channels = len(signals)
    fig, axes = plt.subplots(n_channels, 1, figsize=(12, 3*n_channels))

    for i in range(n_channels):
        signal = signals[i]
        fs = signal_headers[i]['sample_frequency']
        time = np.linspace(0, len(signal)/fs, len(signal))

        ax = axes[i] if n_channels > 1 else axes
        ax.plot(time, signal)
        ax.set_ylabel('Amplitude')
        ax.set_title(signal_headers[i]['label'])
        ax.grid(True)

    axes[-1].set_xlabel('Time (s)')
    plt.tight_layout()
    plt.show()

def plot_signal_with_annotations(signals, signal_headers, channel, header):
    signal = signals[channel]
    signal_header = signal_headers[channel]
    annotations = header["annotations"]

    fs = signal_header['sample_frequency']
    duration = len(signal) / fs
    time = np.linspace(0, duration, len(signal))
    plt.figure(figsize=(12, 4))

    colour_map = {
        "T0": "blue",
        "T1": "red",
        "T2": "yellow"
    }

    plotted_labels = set()

    for start_time, a_duration, label in annotations:
        start_idx = int(start_time * fs)
        end_idx = int((start_time + a_duration) * fs)

        plt.plot(
            time[start_idx: end_idx],
            signal[start_idx: end_idx],
            color=colour_map[label],
            label=label if not label in plotted_labels else None
        )

        plotted_labels.add(label)

    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.title(signal_headers[channel]['label'])
    plt.grid(True)
    plt.show()


# This now uses mne python 

main_path = "./eeg-data/reannotated/S001/S001R03_raw.fif"
raw = mne.io.read_raw_fif(main_path)

raw.plot(block=True, scalings="auto", clipping=None)
