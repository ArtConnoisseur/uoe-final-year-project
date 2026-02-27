# =============================================

# This file is part of Rudraksh Srivastava's
# Final Year Project at the University
# of Edinburgh.

# This file is essentially used to maintain the
# code for the preprocessing of the EEG data

# =============================================

import os

import mne
from mne.preprocessing import ICA


class EEGPreprocessing:
    def __init__(self):
        self.base_data_path = r"eeg-data/reannotated/"
        self.save_data_path = r"eeg-data/processed/"
        self.raw = None
        self.ica = None
        self._is_loaded = False

    def _load_file(self, patient, trial):
        complete_path = (
            rf"{self.base_data_path}/S{patient:03}/S{patient:03}R{trial:02}_raw.fif"
        )
        raw = mne.io.read_raw_fif(complete_path)
        raw.rename_channels(lambda ch: ch.rstrip("."))
        montage = mne.channels.make_standard_montage("standard_1005")
        raw.set_montage(montage, match_case=False, match_alias=True)
        self.raw = raw
        self._is_loaded = True
        return raw

    def _apply_notch_and_bandpass(self):
        raw = self.raw.load_data()

        raw_notch = raw.copy().notch_filter(
            freqs=[60], method="spectrum_fit", filter_length="5s"
        )

        raw_bandpass = raw_notch.copy().filter(l_freq=0.1, h_freq=40)

        self.raw = raw_bandpass  # keep self.raw in sync for downstream methods
        return raw_bandpass

    def _fit_ica(self, n_components, random_seed=87):
        raw = self.raw.copy()
        raw = raw.load_data()

        # ICA requires a 1Hz high-pass to perform reliably
        raw = raw.filter(l_freq=1, h_freq=None)

        ica = ICA(
            n_components=n_components,
            max_iter="auto",
            random_state=random_seed,
        )
        ica.fit(raw)

        explained_var_ratio = ica.get_explained_variance_ratio(raw)
        self.ica = ica
        return ica, explained_var_ratio

    def _exclude_ica_components(self, components):
        if self.ica is None:
            raise RuntimeError("ICA has not been fitted yet. Call _fit_ica() first.")

        # excluding top components ensures heartbeat and eye blinks are removed
        self.ica.exclude = components

    def _apply_ica(self):
        if self.ica is None:
            raise RuntimeError("ICA has not been fitted yet. Call _fit_ica() first.")

        raw = self.raw.copy()
        self.ica.apply(raw)
        return raw

    def _create_epochs(self, raw):
        events, event_id = mne.events_from_annotations(raw)

        epochs = mne.Epochs(
            raw,
            events=events,
            event_id=event_id,
            tmin=-0.5,
            tmax=4.0,
            baseline=(
                None,
                0,
            ),  # baseline correction from start of epoch to stimulus onset
            preload=True,
        )

        return epochs

    def save_processed(self, raw, patient, trial):
        save_dir = os.path.join(self.save_data_path, f"S{patient:03}")
        os.makedirs(save_dir, exist_ok=True)

        save_path = os.path.join(save_dir, f"S{patient:03}R{trial:02}_epo.fif")
        raw.save(save_path, overwrite=True)

    def reset(self):
        self.raw = None
        self.ica = None  # fixed: was missing, stale ICA would persist across files
        self._is_loaded = False

    def run_pipeline(
        self, patient, trial, n_components, exclude_components, random_seed=87
    ):
        if self._is_loaded:
            raise RuntimeError(
                "A file is already loaded. Call reset() before processing a new file."
            )

        self._load_file(patient, trial)
        self._apply_notch_and_bandpass()
        self._fit_ica(n_components=n_components, random_seed=random_seed)
        self._exclude_ica_components(exclude_components)
        raw_clean = self._apply_ica()
        epochs = self._create_epochs(raw_clean)
        return epochs

    def process_batch(
        self, file_list, n_components, exclude_components, random_seed=42
    ):
        """
        file_list: list of (patient, trial) tuples
        e.g. [(1, 12), (1, 13), (2, 4)]
        """
        for patient, trial in file_list:
            self.reset()
            print(f"Processing S{patient:03} R{trial:02}...")

            raw_clean = self.run_pipeline(
                patient=patient,
                trial=trial,
                n_components=n_components,
                exclude_components=exclude_components,
                random_seed=random_seed,
            )

            self.save_processed(raw_clean, patient, trial)
            print(f"Saved S{patient:03} R{trial:02} to {self.save_data_path}")


if __name__ == "__main__":
    eeg_processor = EEGPreprocessing()
    full_file_list = [
        (patient, trial) for patient in range(1, 110) for trial in range(3, 15)
    ]
    eeg_processor.process_batch(full_file_list, 15, [0, 1, 2, 3], 42)
