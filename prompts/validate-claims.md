Validate the candidate resume against `data/` and `data/verified-metrics.yaml`.

For every factual statement in the candidate resume:
1. Identify the source fact in `data/`.
2. Flag any unsupported technology, title, responsibility, date, metric, scale claim, or outcome.
3. Flag stronger causal wording than the source supports.
4. Flag any metric not present in `verified-metrics.yaml` with `verified: true`.
5. Validate that engagement dates are consistent with `data/experience.yaml` and chronologically valid.

Return a concise validation report and suggested factual corrections. Do not silently fix claims.
