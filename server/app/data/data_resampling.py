import mne 

path = "./eeg-data/processed/S001/S001R03_epo.fif"
raw = mne.read_epochs(path)
print(raw.info)