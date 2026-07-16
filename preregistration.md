# Pre-Registered Analysis Plan
## Held-Out Validation of a Contralateral ERD Asymmetry (EEGBCI, Subjects 61–109)

## Background

In my previous analysis of 60 subjects, a post-hoc pooling procedure resulted in a significant p-value for the C3 channel (p = 0.0085). However, this was an exploratory finding: the decision to pool was made after seeing the initial results. This pre-registration tests that exact same hypothesis on a completely unused, held-out dataset using a strictly predefined procedure.

## Transparency Note

Subjects 1 to 60 from the EEGBCI dataset were analyzed in the previous exploratory phases. Subjects 61 to 109 have never been accessed, viewed, or analyzed.

## Primary Hypothesis

For the C3 channel, Right Fist Imagery (T2) creates a stronger Event-Related Desynchronization (ERD) than Left Fist Imagery (T1).

- **Event labels:** Verified from PhysioNet documentation for runs 4, 8, 12: T1 = left fist imagery, T2 = right fist imagery.
- **Mathematical prediction:** `Mean(T2_ERD) - Mean(T1_ERD) < 0`
- **Statistical test:** One-sided one-sample t-test (`alternative='less'`)
- **Significance threshold:** alpha = 0.05
- **Correction:** None. This is a single, isolated primary test.

## Secondary (Exploratory) Analysis

The C4 channel will be processed and reported using the exact same metrics. However, this is **not** a formal hypothesis test. In the first 60 subjects, C4 was silent at every stage (p = 0.108, 0.678, 0.143). Therefore, there is no formal prediction for C4, and no claim will be made from its result.

## Dataset

- **Dataset:** EEGBCI (PhysioNet, eegmmidb)
- **Subjects:** 61 through 109 (n = 49)
- **Runs:** 4, 8, 12 (motor imagery)
- **Sample size rationale:** Fixed at n = 49, i.e. all remaining unused subjects.

## Exclusion Criteria

Subjects will be excluded strictly for technical failures only (file loading errors, missing runs, corrupted data formats). No subject will be excluded based on signal quality, artifacts, or the final results. Any excluded subject will be explicitly documented and reported.

## Preprocessing Pipeline

Applied strictly in this order:

1. Standardize channel names (`mne.datasets.eegbci.standardize`)
2. Apply `standard_1005` montage
3. Highpass filter at 1.0 Hz (no lowpass)
4. Apply Current Source Density (CSD) transformation
5. Epoching: tmin = -1.0 s, tmax = 4.0 s
6. Baseline correction: (-1.0, 0.0) s
7. **Note:** Independent Component Analysis (ICA) will not be used.

## Analysis Pipeline

- **Method:** PSD-based Event-Related Desynchronization (ERD)
- **Frequency band:** Alpha (8–13 Hz)
- **Time windows:** Baseline = -1.0 to 0.0 s, Movement = 0.5 to 2.5 s
- **ERD formula:** `ERD (%) = (Movement_power - Baseline_power) / Baseline_power * 100`
- **Subject-level extraction:** `c3_diff = Mean(T2_ERD) - Mean(T1_ERD)`
- **Group-level test:** `scipy.stats.ttest_1samp(c3_diffs, 0, alternative='less')`

## Decision Rule

- **If p < 0.05:** The exploratory finding is confirmed on independent data.
- **If p >= 0.05:** The finding is not confirmed. The initial p = 0.0085 was likely a statistical mirage born from post-hoc pooling.

## Commitment

The results of this analysis will be published exactly as they are. There will be no parameter tweaking. There will be no additional post-hoc analyses to "save" the p-value. There will be no dynamic adding or removing of subjects. The code will be run once, and the output will be the final word.

## Also Reported (Descriptive)

To provide context beyond the p-value:

- Distribution of signs across subjects (how many showed a negative difference)
- Effect size (Cohen's d). For reference, the exploratory phase yielded d = -0.35 (small-to-moderate).
- The exact p-value and effect size for C4
- The IDs of any subjects dropped due to technical errors
