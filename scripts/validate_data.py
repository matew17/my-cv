#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import re
import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DATE_RE = re.compile(r"^(\d{4})-(\d{2})$")


def load(name):
    return yaml.safe_load((DATA / name).read_text(encoding="utf-8"))


def month_index(value):
    if value in (None, "present"):
        return None
    text = str(value)
    match = DATE_RE.match(text)
    if not match:
        return None
    year, month = map(int, match.groups())
    if not 1 <= month <= 12:
        return None
    return year * 12 + month


def check_date_range(start, end, label, warnings):
    if start is None:
        warnings.append(f"MISSING START DATE: {label}")
        return
    if end is None:
        warnings.append(f"MISSING END DATE: {label}")
        return
    start_idx = month_index(start)
    end_idx = month_index(end)
    if str(start) != "present" and start_idx is None:
        warnings.append(f"INVALID START DATE: {label}: {start!r}")
    if str(end) != "present" and end_idx is None:
        warnings.append(f"INVALID END DATE: {label}: {end!r}")
    if start_idx is not None and end_idx is not None and start_idx > end_idx:
        warnings.append(f"REVERSED DATE RANGE: {label}: {start} > {end}")


def main():
    experience = load("experience.yaml")
    metrics = load("verified-metrics.yaml")
    warnings = []

    for employer in experience:
        company = employer.get("company", "Unknown employer")
        check_date_range(
            employer.get("employment_start"),
            employer.get("employment_end"),
            company,
            warnings,
        )
        for engagement in employer.get("engagements", []) or []:
            label = " / ".join(
                x for x in [engagement.get("client"), engagement.get("project")] if x
            )
            if engagement.get("start_status") == "unconfirmed":
                warnings.append(
                    f"UNCONFIRMED DATE: {label} start date. "
                    f"Raw user value: {engagement.get('user_supplied_start_raw')!r}."
                )
            check_date_range(engagement.get("start"), engagement.get("end"), label, warnings)

    def walk(obj, path=""):
        if isinstance(obj, dict):
            if "verified" in obj and obj["verified"] is not True:
                warnings.append(f"UNVERIFIED METRIC: {path}")
            for k, v in obj.items():
                walk(v, f"{path}.{k}" if path else k)
        elif isinstance(obj, list):
            for i, v in enumerate(obj):
                walk(v, f"{path}[{i}]")

    walk(metrics)

    if warnings:
        print("Data validation completed with warnings:")
        for warning in warnings:
            print(f"- {warning}")
        raise SystemExit(1)

    print("Data validation passed with no warnings.")


if __name__ == "__main__":
    main()
