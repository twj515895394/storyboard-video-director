#!/usr/bin/env python3
"""Validate the storyboard-video-director Skill package.

Checks the required SKILL.md frontmatter, expected directories, schemas, and core references.
This script uses only the Python standard library.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REQUIRED_DIRS = ["references", "assets", "assets/templates", "assets/examples", "assets/case-cards", "scripts", "schemas"]
REQUIRED_FILES = [
    "SKILL.md",
    "references/00-router.md",
    "references/01-grill-me-workflow.md",
    "references/02-brief-shot-map-schema.md",
    "references/03-storyboard-image-prompt-builder.md",
    "references/04-video-prompt-builder.md",
    "references/09-quality-checklist.md",
    "schemas/shot-map.schema.json",
    "schemas/case-card.schema.json",
]


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md must start with YAML frontmatter delimited by ---")
    end = text.find("\n---", 4)
    if end == -1:
        raise ValueError("SKILL.md frontmatter closing delimiter not found")
    raw = text[4:end].strip()
    data: dict[str, str] = {}
    for line in raw.splitlines():
        if not line.strip() or line.strip().startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"Invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    errors: list[str] = []
    warnings: list[str] = []

    skill_path = root / "SKILL.md"
    if not skill_path.exists():
        errors.append("Missing SKILL.md")
    else:
        text = skill_path.read_text(encoding="utf-8")
        try:
            fm = parse_frontmatter(text)
            if fm.get("name") != "storyboard-video-director":
                warnings.append("frontmatter name is not storyboard-video-director")
            if not fm.get("name"):
                errors.append("frontmatter.name is required")
            if not fm.get("description"):
                errors.append("frontmatter.description is required")
            elif len(fm["description"]) < 60:
                warnings.append("description may be too short for reliable triggering")
        except ValueError as exc:
            errors.append(str(exc))

    for d in REQUIRED_DIRS:
        if not (root / d).is_dir():
            errors.append(f"Missing directory: {d}")

    for f in REQUIRED_FILES:
        if not (root / f).is_file():
            errors.append(f"Missing file: {f}")

    for schema in ["schemas/shot-map.schema.json", "schemas/case-card.schema.json"]:
        path = root / schema
        if path.exists():
            try:
                json.loads(path.read_text(encoding="utf-8"))
            except json.JSONDecodeError as exc:
                errors.append(f"Invalid JSON in {schema}: {exc}")

    if skill_path.exists():
        content = skill_path.read_text(encoding="utf-8")
        refs = re.findall(r"`(references/[^`]+\.md)`", content)
        for ref in refs:
            if not (root / ref).exists():
                errors.append(f"SKILL.md references missing file: {ref}")

    for warning in warnings:
        print(f"WARN: {warning}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("OK: storyboard-video-director skill package looks valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
