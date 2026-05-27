# Multi-Clip Controller

Use when a video is too complex for one generation prompt.

## When to split

Consider splitting when any of these apply:

- longer than 15–20 seconds;
- more than 8–12 shots;
- more than 2 main subjects;
- multiple major scene changes;
- complex action causality chain;
- high risk of identity drift;
- user wants a longer short film, ad, or sequence.

## Output structure

For multi-clip output, use:

1. Global Brief
2. Clip Map
3. Per-Clip Prompt
4. Stitching Notes

## Global Brief

Must include:

- subject identity and reference assets;
- world/scene rules;
- style and color logic;
- audio rules;
- action causality rules;
- continuity constraints;
- negative constraints.

## Clip Map

For each clip:

```yaml
clip: 1
duration: "8s"
function: "setup and first conflict"
start_state: ""
end_state: ""
shot_density: medium
continuity_into_next: ""
```

## Per-Clip Prompt

Each clip must be independently copyable while preserving global rules. Repeat the minimum global identity and style constraints inside each clip prompt.

## Stitching Notes

State how clips connect:

- last frame of clip 1 should match first frame of clip 2;
- subject position and direction;
- prop/damage/outfit state;
- sound tail or hard cut;
- color/lighting continuity;
- camera direction continuity.
