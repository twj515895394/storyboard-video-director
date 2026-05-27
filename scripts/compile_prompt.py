#!/usr/bin/env python3
"""Compile a lightweight storyboard/video prompt from a Shot Map JSON.

This is a deterministic helper, not a replacement for the Skill's creative reasoning.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def shot_line(shot: dict[str, Any], idx: int) -> str:
    camera = shot.get("camera", {}) or {}
    action = shot.get("action", {}) or {}
    audio = shot.get("audio", {}) or {}
    parts = [
        f"SHOT {shot.get('shot', idx)}",
        shot.get("time", ""),
        shot.get("panel_title", ""),
        shot.get("frame_description", ""),
        f"Camera: {camera.get('shot_size', '')}, {camera.get('angle', '')}, {camera.get('movement', '')}, {camera.get('lens_feel', '')}".strip(),
        f"Action/Cause/Effect: {action.get('subject_action', '')}; {action.get('cause', '')}; {action.get('effect', '')}".strip(),
    ]
    if any(audio.values()):
        parts.append("Audio: " + ", ".join(f"{k}={v}" for k, v in audio.items() if v))
    return " / ".join(p for p in parts if p)


def build_video(data: dict[str, Any], lang: str) -> str:
    pb = data.get("project_brief", {})
    sv = data.get("story_visual_brief", {})
    shots = data.get("shot_map", [])
    header = "视频生成 Prompt" if lang == "zh" else "Video Generation Prompt"
    lines = [f"# {header}", "", f"FORMAT: {pb.get('title', 'Untitled')} / {len(shots)} shots", ""]
    lines += ["SUBJECTS / STYLE:", sv.get("logline", ""), sv.get("style_language", ""), ""]
    lines += ["SCENE:", sv.get("scene_world", ""), ""]
    lines += ["SHOT SEQUENCE:"]
    lines.extend(shot_line(s, i + 1) for i, s in enumerate(shots))
    lines += ["", "COLOR LOGIC:", sv.get("color_logic", ""), "", "CONSTRAINTS:", "Maintain subject consistency, action causality, and shot continuity. Do not add subtitles unless requested."]
    return "\n".join(lines)


def build_storyboard(data: dict[str, Any], lang: str) -> str:
    pb = data.get("project_brief", {})
    sv = data.get("story_visual_brief", {})
    shots = data.get("shot_map", [])
    header = "gpt-image2 故事版图片 Prompt" if lang == "zh" else "gpt-image2 Storyboard Image Prompt"
    lines = [f"# {header}", ""]
    lines.append(f"Create a {pb.get('aspect_ratio', '16:9')} wide cinematic storyboard sheet for: {pb.get('title', 'Untitled')}.")
    lines.append("Use a clean production storyboard layout with numbered panels, short Chinese labels by default, optional reference strip, and optional technical bar.")
    lines.append(f"Style: {sv.get('style_language', '')}. Color logic: {sv.get('color_logic', '')}.")
    lines.append("Maintain strict consistency across all panels.")
    lines.append("")
    lines.append("MAIN STORYBOARD PANELS:")
    for i, shot in enumerate(shots, 1):
        lines.append(shot_line(shot, i))
    lines.append("")
    lines.append("Avoid dense text, wrong panel order, inconsistent subject design, and cluttered layout.")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("json_path")
    parser.add_argument("--mode", choices=["storyboard", "video", "complete"], default="complete")
    parser.add_argument("--lang", choices=["zh", "en", "both"], default="both")
    args = parser.parse_args()

    data = json.loads(Path(args.json_path).read_text(encoding="utf-8"))
    langs = ["zh", "en"] if args.lang == "both" else [args.lang]
    chunks: list[str] = []
    for lang in langs:
        if args.mode in {"storyboard", "complete"}:
            chunks.append(build_storyboard(data, lang))
        if args.mode in {"video", "complete"}:
            chunks.append(build_video(data, lang))
    print("\n\n---\n\n".join(chunks))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
