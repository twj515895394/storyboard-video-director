# Video Prompt Builder

Use for Seedance, generic AI video models, or model-specific video prompt generation. Do not treat Seedance 2.0 as requiring one rigid format. Use adaptive prompt dimensions and organize them clearly.

## Core dimensions

1. Format: duration, shot count, rhythm, clip strategy.
2. Subjects: characters/products/objects and reference asset binding.
3. Scene: environment, geography, route, spatial logic.
4. Action Logic: cause-effect chain and visible triggers.
5. Shot Sequence: ordered shots with camera language.
6. Camera Language: shot size, angle, movement, lens feel.
7. Audio Design: SFX/dialogue/voiceover/BGM as needed.
8. Mood: emotional movement.
9. Color Logic: palette and lighting transition.
10. Style: medium, realism level, texture, rendering language.
11. Constraints: identity, physics, continuity, and what not to show.

## Duration and shot density planner

- User specifies duration and shot count: obey unless infeasible.
- User specifies duration only: recommend shot count by type.
- User gives only theme: suggest duration and density.

Guidelines:

- Action/mechanical/chase: high shot density, clear inserts.
- Emotion/atmosphere/documentary: lower density, longer holds.
- Product/demo/training: shots follow operation or information beats.
- Vlog/social: event beats and camera intimacy drive shot count.

## Video prompt output structure

Use adaptive headings. A strong default is:

```text
FORMAT:
SUBJECTS:
REFERENCE ASSET BINDING:
SCENE:
ACTION LOGIC:
SHOT SEQUENCE:
AUDIO DESIGN:
MOOD:
COLOR LOGIC:
STYLE:
CONSTRAINTS:
```

Remove headings that are irrelevant. Do not force dialogue, voiceover, BGM, or subtitles.

## Shot sequence requirements

Each shot should include:

- shot number;
- camera language;
- subject action;
- location/route state;
- cause/effect when relevant;
- continuity from previous shot when needed;
- audio cues if useful.

## Reference asset binding

If assets are referenced, explicitly define usage:

```text
Use @[image1] only as character identity reference.
Use @[image2] only as robot/product design reference.
Do not redesign the subjects.
Maintain identity consistency across all shots.
```

## Subtitle policy for V1

Subtitles, captions, and screen text are disabled by default. Add only when the user explicitly asks.

## Final output pattern

1. 中文视频方案说明.
2. 中文视频 Prompt.
3. English Video Prompt.
4. Optional model notes or feasibility notes.
