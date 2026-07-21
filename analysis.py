"""
Held-out validation of a contralateral ERD asymmetry.
EEGBCI motor imagery (runs 4, 8, 12), subjects 61-109.

Primary test: in C3, right-hand imagery (T2) shows stronger alpha ERD
than left-hand imagery (T1), i.e. mean(T2) - mean(T1) < 0.

NOTE: parameters here differ from the committed pre-registration
(wavelet not PSD, 8-20 Hz, 1-3s window). See results.md, "Deviation".
"""

import numpy as np
import mne
from mne.datasets import eegbci
from scipy.stats import ttest_1samp


def wavelet_erd(epochs_cond, channel, freqs, n_cycles):
    """Per-epoch ERD (%) for one channel, averaged over the
    1-3s window and 8-20 Hz band, baseline-corrected to (-1, 0)."""
    tfr = epochs_cond.compute_tfr(method='morlet', freqs=freqs,
                                  n_cycles=n_cycles, return_itc=False,
                                  average=False)
    tfr.apply_baseline(baseline=(-1, 0), mode='percent')
    tfr = tfr.pick([channel]).crop(tmin=1.0, tmax=3.0, fmin=8, fmax=20)
    return tfr.data.mean(axis=(1, 2, 3))   # one value per epoch


c3_diff = []
c4_diff = []
freqs = np.arange(8, 31, 1)
n_cycles = freqs / 2

for subject in range(61, 110):
    try:
        files = eegbci.load_data(subjects=subject, runs=[4, 8, 12])
        raw = mne.concatenate_raws(
            [mne.io.read_raw_edf(f, preload=True) for f in files])

        eegbci.standardize(raw)
        raw.set_montage(mne.channels.make_standard_montage('standard_1005'))
        raw.filter(l_freq=1.0, h_freq=None)
        raw = mne.preprocessing.compute_current_source_density(raw)

        events, event_id = mne.events_from_annotations(raw)
        epochs = mne.Epochs(raw, events, event_id=event_id,
                            tmin=-1.0, tmax=4.0, baseline=(-1, 0),
                            preload=True)

        t2c3 = wavelet_erd(epochs['T2'], 'C3', freqs, n_cycles)
        t1c3 = wavelet_erd(epochs['T1'], 'C3', freqs, n_cycles)
        t1c4 = wavelet_erd(epochs['T1'], 'C4', freqs, n_cycles)
        t2c4 = wavelet_erd(epochs['T2'], 'C4', freqs, n_cycles)

        c3_diff.append(np.mean(t2c3) - np.mean(t1c3))
        c4_diff.append(np.mean(t1c4) - np.mean(t2c4))
        print(f"Subject {subject}: c3={c3_diff[-1]:.2f}, c4={c4_diff[-1]:.2f}")

    except Exception as e:
        print(f"Subject {subject} skipped: {e}")


# --- Primary test: C3 ---
t3, p3 = ttest_1samp(c3_diff, 0, alternative='less')
d = np.mean(c3_diff) / np.std(c3_diff, ddof=1)
print(f"\nC3 (primary): p = {p3:.4f}, d = {d:.4f}")

# --- Secondary: C4 (exploratory, no prediction) ---
t4, p4 = ttest_1samp(c4_diff, 0, alternative='less')
print(f"C4 (secondary): p = {p4:.4f}")

# --- Sign distribution ---
c3 = np.array(c3_diff)
print(f"n = {len(c3)}, "
      f"negative = {int(np.sum(c3 < 0))}, "
      f"positive = {int(np.sum(c3 > 0))}")
