# What secret scanning evaluations measure — reproducibility materials

Authors: **Tripti Tiwari** and **Mohit Tiwari** (corresponding author).  
Target journal: *Computing* (Springer Nature).  
Article type: Critical methodological review. **This repository is supporting material, not evidence of publication or acceptance.**

## Public supporting evidence

The following files are directly browsable/downloadable in this repository:

| File | Purpose |
| --- | --- |
| `extraction_ledger.csv` | Structured extraction from 15 assessed full-text studies |
| `assessed_source_manifest.json` | Assessed sources and provenance |
| `claim_locations.json` | Source-level locations for review claims |
| `descriptive_appraisal.csv` | Methodological appraisal |
| `discovery_queries.csv` | Actual discovery query records |
| `Search_and_Selection.md` | Review design, selection limits, and retrieval exceptions |
| `reference_verification_ledger.json` | Bibliographic verification records |
| `tables.json` | Supporting table data |
| `counterexample_results.json` | Constructed arithmetic example outputs |
| `code/counterexamples.py` | Python 3 script for reproducing examples |

A single archival snapshot is available as [**Online Resource 1 (tar.xz)**](evidence/Online_Resource_1.tar.xz).

**Archive SHA-256:** `6631e9aae595a81ecee933380e27b607b362db3ef8a410c666b31585a68103d1`.

## Reproduction

Using Python 3 (standard library only), run:

```bash
python3 code/counterexamples.py
```

The script checks three **constructed** counterexamples and writes `counterexample_results.json`. These are analytical illustrations, **not** empirical secret-scanner performance measurements.

## Scope and research transparency

This is a bounded, purposive critical review, **not** a systematic review or comprehensive census. The material documents the 15 assessed full-text studies and retrieval/selection limitations; it does **not** redistribute copyrighted full texts. The supplementary materials are provided for transparency, not as a claim that all source findings have been independently replicated.

## Suggested research-data availability wording

"The structured evidence-extraction ledger, assessed-source manifest, source-level claim locations, descriptive appraisal, discovery and reference-verification records, supporting tables, and executable arithmetic counterexamples are publicly available at https://github.com/profmohit-edu/secret-scanning-evaluation-review. A matching supplementary snapshot is provided as Online Resource 1. The underlying third-party studies are available through their original publishers or repositories, subject to their access conditions."

## Citation

Tiwari, T. and Tiwari, M. *What secret scanning evaluations measure*. Manuscript prepared for submission to *Computing*. **Do not cite as accepted or published.**
