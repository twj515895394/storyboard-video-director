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
5. Shot Strategy: one-take, multi-shot, montage, loop, clip-series.
6. Camera Language: shot size, angle, movement, lens feel.
7. Motion Grammar: pace profile, subject route, camera relationship, transition logic.
8. Timeline / Beat Map: timed action beats used to assemble the final prompt.
9. Audio Design: SFX/dialogue/voiceover/BGM as needed.
10. Mood: emotional movement.
11. Color Logic: palette and lighting transition.
12. Style: medium, realism level, texture, rendering language.
13. Constraints: identity, physics, continuity, and what not to show.

## Timeline policy

Timeline is a required planning layer for direct video prompt generation.

### Case A: user directly asks for a video prompt

If the user asks directly for 视频 Prompt / Seedance Prompt / AI 视频提示词 and there is no storyboard image as the source, always output a visible timeline section before the final prompt.

Use one of these names:

```text
时间轴设计
Time Beat Map
Timeline / Beat Map
Continuous Action Beats
Shot Timeline
```

The final copyable prompt must also include the timeline information, not just the planning section.

Minimum timeline fields:

```text
time range → visual/action beat → camera/motion behavior → scene/route state → audio cue when useful
```

### Case B: user asks to generate video prompt based on storyboard image

If the user provides or references a storyboard image / storyboard sheet / 分镜图 and asks to convert it into a video prompt, ask whether to add a timeline before finalizing unless the user already specified it.

Recommended question:

```text
要不要在视频 Prompt 里加入明确时间轴？A 加入，按每个分镜/动作拆成时间段（推荐） B 不加入，只保留连续视频描述 C 你指定时间分配。
我的推荐：如果要投喂 Seedance / AI 视频模型，建议加入时间轴，这样镜头节奏和动作更稳。
```

If the user says yes, convert storyboard panels into timed beats. If the user says no, still preserve panel order and continuity, but do not force explicit timestamps.

### Case C: complete package

If output includes both storyboard design and video prompt, include a timeline in the video section by default, because the Shot Map already contains timing information.

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

## Motion grammar rule

Always use `references/10-video-motion-grammar.md` when the prompt involves movement, pacing, tracking, one-take, fast/slow rhythm, route changes, scene transitions, chase, sports, dance, product operation, or camera choreography.

Do not create separate controllers for every named style. Treat one-take, slow-burn, fast kinetic, handheld, drone reveal, tracking, product demo, and montage as combinations of motion grammar parameters:

```text
Shot Strategy + Pace Profile + Camera Relationship + Route / Scene Progression + Subject Motion + Transition Logic + Audio Rhythm + Continuity Constraints
```

## One-take handling inside motion grammar

If the user says 一镜到底, one take, continuous shot, long take, tracking shot, 跟拍, or no cut:

- Use `shot_strategy: one_take`.
- Use internal timed beats, not an edited multi-shot list.
- Make pace explicit: slow_burn, medium_flow, fast_kinetic, staccato, or crescendo.
- One-take can be fast-paced. Build speed through subject acceleration, route changes, foreground wipes, camera height changes, turns, background zone changes, and audio rhythm.
- The final prompt must say: one continuous shot, no cuts, no montage, no jump cuts.

## Video prompt output structure

Use adaptive headings. A strong default is:

```text
FORMAT:
SUBJECTS:
REFERENCE ASSET BINDING:
SCENE & ROUTE:
CAMERA / MOTION GRAMMAR:
TIMELINE / BEAT MAP:
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
SUBJECT:
SCENE & ROUTE:
CAMERA / MOTION GRAMMAR:
CONTINUOUS ACTION BEATS / TIME BEAT MAP:
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
- camera / motion grammar;
- timed action beats or explicit timeline when required;
- lighting and color logic;
- audio priorities;
- negative constraints.

If any of these exist in the Visual Brief, Shot Map, Timeline / Beat Map, or storyboard analysis but not in the final prompt, revise the prompt before output.

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
2. 时间轴设计 / Timeline Beat Map, required for direct video prompt generation.
3. 中文视频 Prompt, copyable.
4. English Video Prompt, copyable when useful.
5. Optional model notes or feasibility notes.

If the user asks for direct generation and the brief is sufficient, keep the design explanation short and prioritize the timeline plus final copyable prompt.
