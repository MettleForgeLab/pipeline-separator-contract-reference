# DataDiddler Lens — Separator (Reference)

**Status:** Reference implementation
**Version:** 0.1.0
**Scope:** Minimal contract-aligned separator lens
**Layer Position:** Lens (reference stage implementation)

This repository implements the **reference separator lens** for DataDiddler.

It is the first concrete lens that plugs into the `datadiddler-kernel` and proves that the lens contract works end-to-end.

It is intentionally minimal.

---

## Purpose

This lens demonstrates how a DataDiddler lens:

* accepts kernel-defined inputs
* produces contract-aligned outputs
* runs as a standalone, inspectable stage

It exists to **prove the interface**, not to provide advanced behavior.

---

## Inputs

This lens expects the following input files:

* `documents.ndjson`
* `text_artifacts.ndjson`

These are provided by the kernel at runtime.

---

## Outputs

This lens produces:

* `triage.ndjson`

The output file must exist and be well-formed for the stage to be considered successful.

---

## Guarantees

This repository guarantees:

* a valid lens structure (template-conformant)
* correct CLI execution behavior
* input file handling
* output file creation
* exit code `0` on success

The implementation:

* reads expected input files
* writes a valid `triage.ndjson`
* does not introduce domain-specific logic

---

## Non-guarantees

This repository does **not** guarantee:

* semantic correctness
* domain intelligence
* schema completeness beyond minimal validity
* downstream compatibility beyond contract shape

This is a **reference lens**, not a production implementation.

---

## Quick run

From the repo root:

```bash
python -m lens_separator_reference.lens --in examples/sample_in --out-dir examples/sample_out
```

Expected result:

```
examples/sample_out/triage.ndjson
```

---

## Contract test

Run:

```bash
pytest
```

These tests verify:

* package import works
* required structure exists
* output file is produced

---

## What this is not

This repository is not:

* the kernel
* a schema authority
* a domain lens
* a policy layer
* a renderer or consumer

It implements a **single stage** within a larger execution graph and exists to validate the contract between kernel and lens.
