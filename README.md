# Contralateral ERD: A Pre-Registered Validation

Testing whether a contralateral ERD asymmetry, found through exploratory
analysis of EEGBCI motor imagery data, holds up on held-out subjects
under a pre-registered plan.

**Result: the exploratory finding did not replicate.** And that is the point.

## Background

Contralateral organization is a textbook fact: right-hand movement activates
the left motor cortex (C3), left-hand movement the right (C4). I set out to
see this asymmetry in real EEG data (PhysioNet EEGBCI, motor imagery runs).

Across exploratory analyses of 60 subjects, a directional tendency appeared
in C3, but only reached significance (p = 0.0085) after a **post-hoc pooling**
decision — one I made *after* seeing that a replication attempt had failed.
That is not a confirmed finding; it is a candidate hypothesis.

So I pre-registered a test.

## What this repo contains

- **`preregistration.md`** — the analysis plan, committed *before* touching
  the held-out data (subjects 61–109). Fixed hypothesis, parameters,
  threshold, and decision rule.
- **`analysis.py`** — the analysis code.
- **`results.md`** — the outcome, reported exactly as the plan required.

## The test

- **Data:** EEGBCI (PhysioNet), subjects 61–109 (never analyzed before)
- **Hypothesis:** in C3, right-hand imagery (T2) produces stronger alpha ERD
  than left-hand imagery (T1) → `mean(T2) − mean(T1) < 0`
- **Test:** one-sided one-sample t-test, alpha = 0.05, single primary test
- **Decision rule:** p < 0.05 → confirmed; p ≥ 0.05 → not confirmed

## Result

| Phase | n | p | Cohen's d |
|-------|---|--------|-----------|
| Exploratory (post-hoc pooled) | 60 | 0.0085 | -0.35 |
| Held-out (pre-registered) | 49 | 0.165 | -0.14 |

Not confirmed. The effect shrank, lost significance, and the sign
distribution in held-out data was nearly balanced (25/24). The exploratory
result was most likely an artifact of post-hoc pooling.

## Why publish a negative result

The value here isn't a discovery. It's the workflow: separating exploration
from confirmation, committing to a plan before seeing the data, and reporting
what the data says rather than what I hoped it would say.

## A note on honesty

The committed pre-registration contained a parameter mismatch with the actual
code (PSD vs wavelet, and different band/window). Rather than editing the
committed plan, I documented the deviation openly in `results.md`. See the
"Deviation from Pre-Registration" section there.

## Related writing

I documented this process (in Turkish) on Substack: [https://substack.com/@mralasahin/note/p-207274574?utm_source=notes-share-action&r=8aezfj]

## Data

PhysioNet EEG Motor Movement/Imagery Dataset (eegmmidb):
https://physionet.org/content/eegmmidb/
