import mne 

# Reading the new file to test if the annotations hold 

print("Baseline:")
raw = mne.io.read_raw_fif(r"eeg-data/reannotated/S001/S001R01_raw.fif")
print(raw.annotations)
print(mne.events_from_annotations(raw))

print("\nLeft/Right:")
raw = mne.io.read_raw_fif(r"eeg-data/reannotated/S001/S001R03_raw.fif")
print(raw.annotations)
print(mne.events_from_annotations(raw))

print("\nFist/Feet:")
raw = mne.io.read_raw_fif(r"eeg-data/reannotated/S001/S001R05_raw.fif")
print(raw.annotations)
print(mne.events_from_annotations(raw))

