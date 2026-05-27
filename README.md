# storyboard-video-director

**AI 故事版与视频分镜导演 Skill**

A Claude/Agent Skill for AI video pre-production. It helps turn a short theme into cinematic storyboard design, gpt-image2 storyboard image prompts, Seedance-style or generic video prompts, multi-clip plans, and reusable case/template assets.

## What this Skill does

- Guides users through focused grill-me clarification.
- Generates creative direction packages before narrowing the idea.
- Builds a shared Project Brief, Story/Visual Brief, Sequence/Beat Layer, and Shot Map.
- Converts the same Shot Map into:
  - storyboard design plans,
  - gpt-image2 storyboard image prompts,
  - Seedance-style/generic video prompts,
  - multi-clip prompt packages.
- Supports case ingestion so strong prompts/examples can become reusable template assets.

## Standard Skill structure

The repository root is the Skill folder. `SKILL.md` is the required entry file with YAML frontmatter. Detailed rules are progressively loaded from `references/`. Reusable templates and examples live in `assets/`. Utility scripts live in `scripts/`.

## Quick validation

```bash
python scripts/validate_skill.py .
```

## Package

```bash
python scripts/package_skill.py . --out storyboard-video-director.zip
```

## Case ingestion scaffold

```bash
python scripts/scaffold_case.py --raw assets/examples/seedance-sabotage-example.md --name "sabotage action" --family "action-mechanical" --mode video
```

## Compile from a Shot Map JSON

```bash
python scripts/compile_prompt.py assets/examples/sample-shot-map.json --mode complete --lang both
```

## V1 note

The case library is optional. The SOP must still produce high-quality output when no custom cases are available.
