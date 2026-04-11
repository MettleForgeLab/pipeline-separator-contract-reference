#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(prog="lens-separator-reference")
    parser.add_argument("--in", dest="input_dir", required=True)
    parser.add_argument("--out-dir", dest="out_dir", required=True)

    args = parser.parse_args()

    input_dir = Path(args.input_dir).resolve()
    out_dir = Path(args.out_dir).resolve()

    documents_path = input_dir / "documents.ndjson"
    text_artifacts_path = input_dir / "text_artifacts.ndjson"

    if not documents_path.exists():
        raise SystemExit(f"Missing input: {documents_path}")

    if not text_artifacts_path.exists():
        raise SystemExit(f"Missing input: {text_artifacts_path}")

    out_dir.mkdir(parents=True, exist_ok=True)

    output_path = out_dir / "triage.ndjson"

    with output_path.open("w", encoding="utf-8") as f:
        # minimal valid output
        json.dump({"status": "ok"}, f)
        f.write("\n")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())