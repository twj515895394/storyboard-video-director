# Video Prompt Builder

Use for Seedance, generic AI video models, or model-specific video prompt generation. Do not treat Seedance 2.0 as requiring one rigid format. Use adaptive prompt dimensions and organize them clearly.

## Non-negotiable output standard

A video prompt must be an execution-grade motion direction, not a loose visual description.

If the user has already provided enough constraints, do not output only a Visual Brief + vague Shot Map. Move directly to a model-ready prompt.

A strong video prompt must specify:

- duration and shot strategy;
- aspect ratio / orientation / target platform when relevant;
- subject identity and visible styling;
- scene geography and movement route;
- camera position, height, distance, movement, and relationship to the subject;
- action beats with exact timing;
- continuity of body, prop, direction, and scene state;
- lighting/color/mood as behavior inside the shot, not just adjectives;
- audio priorities when useful;
- negative constraints to prevent common AI video failure modes.

## Core dimensions

1. Format: duration, aspect ratio, shot count, rhythm, clip strategy.
2. Subjects: characters/products/objects and reference asset binding.
3. Scene: environment, geography, route, spatial logic.
4. Action Logic: cause-effect chain and visible triggers.
5. Shot Sequence: ordered shots with camera language.
6. Camera Language: shot size, angle, movement, lens feel.
7. Motion Blocking: subject movement path, camera path, start/end position, speed changes.
8. Audio Design: SFX/dialogue/voiceover/BGM as needed.
9. Mood: emotional movement.
10. Color Logic: palette and lighting transition.
11. Style: medium, realism level, texture, rendering language.
12. Constraints: identity, physics, continuity, and what not to show.

## Duration and shot density planner

- User specifies duration and shot count: obey unless infeasible.
- User specifies duration only: recommend shot count by type.
- User gives only theme: suggest duration and density.

Guidelines:

- Action/mechanical/chase: high shot density, clear inserts.
- Emotion/atmosphere/documentary: lower density, longer holds.
- Product/demo/training: shots follow operation or information beats.
- Vlog/social: event beats and camera intimacy drive shot count.
- One-take/tracking: one continuous camera move with internal action beats, not multiple edited shots.

## Aspect ratio and orientation rule

For video prompt generation, aspect ratio is a first-class parameter.

If the user does not specify aspect ratio or platform, ask one concise grill question unless the user explicitly asked for immediate generation.

Recommended default question:

```text
这个视频主要用于哪里？A 竖屏 9:16（抖音/小红书/Seedance常用，默认推荐） B 横屏 16:9（电影感/YouTube/PPT） C 方形 1:1 D 你指定比例。
我的推荐：如果是滑板穿梭街巷的一镜到底短视频，优先 9:16；如果要电影感展示环境，选 16:9。
```

If immediate generation is required and aspect ratio is missing, choose a context-aware default and state it before the prompt.

## One-take detection rule

If the user says 一镜到底, one take, continuous shot, long take, tracking shot, 跟拍, or no cut, immediately load `references/10-one-take-video-controller.md`.

For one-take requests, do not output a multi-shot list unless the user asks for a storyboard. Use an internal time-beat map, then produce one continuous prompt.

Important: one-take does not mean slow or static. It can be fast-paced through speed changes, route changes, foreground occlusions, camera height changes, background transitions, and staged action beats inside one uninterrupted shot.

## Video prompt output structure

Use adaptive headings. A strong default is:

```text
FORMAT:
SUBJECTS:
REFERENCE ASSET BINDING:
SCENE & ROUTE:
CAMERA PLAN:
ACTION / MOTION BEATS:
AUDIO DESIGN:
MOOD:
COLOR LOGIC:
STYLE:
CONSTRAINTS:
FINAL COPYABLE PROMPT:
```

For one-take prompts, prefer:

```text
FORMAT:
ONE-TAKE CAMERA PLAN:
SUBJECT:
SCENE & ROUTE:
CONTINUOUS ACTION BEATS:
AUDIO DESIGN:
STYLE / LIGHTING / COLOR:
NEGATIVE CONSTRAINTS:
FINAL COPYABLE PROMPT:
```

Remove headings that are irrelevant. Do not force dialogue, voiceover, BGM, or subtitles.

## Shot sequence / beat requirements

Each shot or internal beat should include:

- shot/beat number;
- time range;
- camera language;
- subject action;
- location/route state;
- cause/effect when relevant;
- continuity from previous shot/beat when needed;
- audio cues if useful.

## Prompt assembly contract

The final copyable prompt must integrate the confirmed Visual Brief and Shot Map / Beat Map details. It must not discard them.

Before finalizing, check that the final prompt includes:

- subject description;
- clothing/props/reference assets;
- duration and aspect ratio/orientation;
- scene and route;
- camera plan;
- timed action beats;
- lighting and color logic;
- audio priorities;
- negative constraints.

If any of these exist in the Visual Brief or Shot Map but not in the final prompt, revise the prompt before output.

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

1. 中文视频方案说明, concise.
2. 中文视频 Prompt, copyable.
3. English Video Prompt, copyable when useful.
4. Optional model notes or feasibility notes.

If the user asks for direct generation and the brief is sufficient, keep the design explanation short and prioritize the final copyable prompt.
