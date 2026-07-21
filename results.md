# Results — Held-Out Validation

## Deviation from Pre-Registration

The committed pre-registration described a PSD-based analysis with an 8–13 Hz
band and a 0.5–2.5s window. The code actually run — used identically across
all exploratory phases and this held-out test — differs:

- **Method:** wavelet (Morlet), not PSD
- **Frequency band (ERD measurement):** 8–20 Hz
- **Time window:** 1.0–3.0s
- **Baseline:** −1 to 0s, percent change

This is a documentation error: the pre-registration text did not match the
code. Because the same wavelet pipeline was used for both the exploratory and
held-out phases, the held-out test remains a valid comparison. But the plan
did not accurately capture the parameters in advance. I report this rather
than silently editing the committed plan — the point of pre-registration is
that the record stays honest.

## Primary Result (C3)

- **p = 0.165** (one-sided one-sample t-test, `alternative='less'`)
- **Cohen's d = -0.14**
- Threshold: alpha = 0.05
- **Outcome: NOT CONFIRMED.**

Per the pre-registered decision rule: the exploratory finding did not
replicate on independent data. The initial p = 0.0085 was likely a
statistical mirage born from post-hoc pooling.

## Effect Size Comparison

| Phase | n | p | Cohen's d |
|-------|---|--------|-----------|
| Exploratory (post-hoc pooled) | 60 | 0.0085 | -0.35 |
| Held-out (pre-registered) | 49 | 0.165 | -0.14 |

The effect size dropped by ~60%. The exploratory d was likely inflated
(winner's curse): an effect estimated from a result that survived a
significance filter is systematically overestimated.

## Sign Distribution (C3)

- Negative difference (expected direction): **25 / 49**
- Positive: **24 / 49**

In the exploratory set the split was 42/18 — a clear lean. In the held-out
set it is essentially a coin flip (25/24). The directional tendency that
motivated this test almost entirely disappears in independent data.

## Secondary — C4 (exploratory, no prediction)

- **p = 0.194**
- No claim was pre-registered for C4. Consistent with its silence across all
  exploratory phases (p = 0.108, 0.678, 0.143).

## Excluded Subjects

- None. All 49 subjects (61–109) loaded and processed successfully.

## Post-hoc Note (transparency, NOT evidence)

Out of curiosity, I also ran the analysis on all 109 subjects (exploratory +
held-out pooled): p = 0.014, d = -0.21. **This number is not interpretable as
evidence.** It mixes the exploratory set with the held-out set, destroying the
independence that made the validation meaningful. The low p-value reflects the
large n (109), not a strong effect — d = -0.21 remains small.

## Conclusion

The pre-registered validation did not confirm the exploratory finding. In the
held-out data the effect was small (d = -0.14), non-significant (p = 0.165),
and the sign distribution was nearly balanced (25/24). The value of this
repository is not a finding; it is the demonstration of testing one's own
claim honestly — including reporting a deviation — and accepting the result.
