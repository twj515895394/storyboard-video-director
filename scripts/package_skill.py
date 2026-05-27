#!/usr/bin/env python3
"""Package the Skill directory into a zip archive."""
from __future__ import annotations

import argparse
import subprocess
import sys
import zipfile
from pathlib import Path

EXCLUDES = {".git", "__pycache__", ".DS_Store"}


def should_skip(path: Path) -> bool:
    return any(part in EXCLUDES for part in path.parts) or path.suffix == ".pyc" or path.suffix == ".zip"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    parser.add_argument("--out", default="storyboard-video-director.zip")
    parser.add_argument("--skip-validate", action="store_true")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    if not args.skip_validate:
        result = subprocess.run([sys.executable, str(root / "scripts" / "validate_skill.py"), str(root)])
        if result.returncode != 0:
            return result.returncode

    out = Path(args.out).resolve()
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
        for file in root.rglob("*"):
            if file.is_file() and not should_skip(file.relative_to(root)):
                zf.write(file, file.relative_to(root))
    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
