#!/usr/bin/env python3
"""Create a case-card scaffold from a raw prompt/example file."""
from __future__ import annotations

import argparse
import datetime as dt
import re
from pathlib import Path


def slugify(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value or "case"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--raw", required=True, help="Path to raw prompt/example text")
    parser.add_argument("--name", required=True, help="Case name")
    parser.add_argument("--family", default="unclassified", help="Template family")
    parser.add_argument("--mode", choices=["storyboard_image", "video_prompt", "complete_package", "video"], default="video_prompt")
    parser.add_argument("--out-dir", default="assets/case-cards")
    args = parser.parse_args()

    raw_path = Path(args.raw)
    if not raw_path.exists():
        raise FileNotFoundError(raw_path)
    raw_text = raw_path.read_text(encoding="utf-8")
    date = dt.date.today().strftime("%Y%m%d")
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{date}-{slugify(args.name)}.md"

    mode = "video_prompt" if args.mode == "video" else args.mode
    excerpt = raw_text[:4000]
    card = f"""# {args.name}

```yaml
case_name: "{args.name}"
mode: {mode}
template_family: "{args.family}"
source_type: prompt
use_cases: []
layout_structure: "TODO"
shot_or_panel_count: "TODO"
beat_structure: []
visual_style: "TODO"
camera_language: "TODO"
audio_design: "TODO"
action_causality: "TODO"
reference_asset_strategy: "TODO"
technical_bar_or_format: "TODO"
reusable_modules: []
non_reusable_parts: []
variant_ideas: []
quality_notes: []
```

## Raw excerpt

```text
{excerpt}
```

## Deconstruction notes

- Structure:
- Why it works:
- Reusable prompt modules:
- Risks / non-reusable details:
- Recommended template updates:
"""
    out_path.write_text(card, encoding="utf-8")
    print(out_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
