# Video Motion Grammar

This module defines a general motion-and-pacing grammar for video prompts. Do not create a new controller file for every style such as one-take, slow-burn, chase, handheld, drone, product demo, or fast montage. Treat those as combinations of motion grammar parameters.

## Core idea

A video prompt should be built from reusable motion dimensions:

```text
Shot Strategy
+ Pace Profile
+ Camera Relationship
+ Route / Scene Progression
+ Subject Motion
+ Transition Logic
+ Visual Rhythm
+ Audio Rhythm
+ Continuity Constraints
```

Specific forms such as 一镜到底, fast-paced, slow-paced, handheld tracking, drone reveal, product macro, or city chase are presets made from these dimensions, not separate controllers.

## 1. Shot Strategy

Choose one:

| Strategy | Meaning | Prompt behavior |
|---|---|---|
| one_take | One uninterrupted shot | Use internal time beats, no cuts |
| multi_shot | Edited sequence | Use shot list |
| montage | Rapid associative cuts | Use visual rhythm and transitions |
| loop | Seamless repeated action | Define start/end match |
| clip_series | Multiple generated clips | Use Multi-Clip Controller |

For `one_take`, do not output `SHOT 1 / SHOT 2` as edited cuts. Use `CONTINUOUS BEATS`.

## 2. Pace Profile

Choose or infer:

| Pace | Description | Controls |
|---|---|---|
| slow_burn | Calm, observational, lingering | longer holds, subtle camera drift |
| medium_flow | Natural cinematic pace | balanced motion and readable action |
| fast_kinetic | High-energy motion | speed changes, close tracking, foreground wipes |
| staccato | Rapid precise beats | inserts, hard timing, crisp SFX |
| crescendo | Gradual acceleration | slow start, fast end, rising audio/visual intensity |

Important: one-take can be fast. It should create rhythm through route changes, camera height changes, speed ramps, foreground occlusion, subject turns, and background transitions.

## 3. Camera Relationship

Define camera relation to subject:

- front tracking;
- side tracking;
- side-rear tracking;
- over-shoulder;
- low follow;
- top-down follow;
- orbit;
- push-in / pullback;
- handheld / gimbal / FPV / drone.

Always include camera height, distance, and stability:

```text
low side-rear tracking camera, knee-to-waist height, close enough to feel speed while keeping full body and skateboard readable, handheld-gimbal hybrid, energetic but controlled
```

## 4. Route / Scene Progression

For movement videos, define a readable route:

```text
start zone → texture zone → obstacle/turn/occlusion → reveal zone → exit/payoff
```

One scene can contain multiple visual zones. This solves the user's concern that one-take should still feel like different scenes or changing environments.

Examples:

- alley entrance → laundry zone → e-bike cluster → graffiti corner → bright market exit;
- living room → hallway → kitchen → balcony reveal;
- product table → hand interaction → macro detail → final hero angle.

## 5. Subject Motion

Specify how the subject moves:

- enters frame;
- accelerates;
- turns;
- ducks / jumps / slides / carves;
- interacts with props;
- exits or lands in final pose.

For action, tie movement to visible physical cause.

## 6. Transition Logic

For multi-shot: use cuts, match cuts, whip pans, inserts, or hard cuts.

For one-take: transitions must happen inside the continuous shot:

- foreground wipe;
- passing behind object;
- camera dip/rise;
- turn around a corner;
- lighting change;
- moving from one visual zone to another.

## 7. Audio Rhythm

Match sound to motion:

- wheel rattle / footsteps / breath / fabric movement;
- city ambience changing by zone;
- SFX accents on turns, impacts, pushes;
- optional BGM only if useful.

Do not force dialogue, voiceover, BGM, subtitles, or screen text.

## 8. Output assembly rule

When a Visual Brief and Shot Map / Beat Map have been generated, the final copyable prompt must include the same information. Do not summarize it away.

Mandatory final prompt fields:

- format: duration, aspect ratio, shot strategy, pace;
- subject: identity, clothing, prop, continuity lock;
- scene and route: visual zones and movement path;
- camera choreography: height, distance, relation, motion, stability;
- action beats: timed internal beats or shot list;
- audio design: only useful sounds;
- style/light/color;
- negative constraints.

## Preset examples

### Fast one-take tracking

```text
shot_strategy: one_take
pace_profile: fast_kinetic
camera_relationship: low side-rear tracking
route: entrance → texture zone → foreground wipe → turn → bright exit
transition_logic: in-camera transitions only
```

### Slow observational one-take

```text
shot_strategy: one_take
pace_profile: slow_burn
camera_relationship: gentle handheld push-in
route: static space with micro-actions
transition_logic: lighting and subject movement
```

### Fast edited action

```text
shot_strategy: multi_shot
pace_profile: staccato
camera_relationship: alternating wide / macro inserts
action_logic: visible cause-effect chain
transition_logic: hard cuts and inserts
```

### Product demo

```text
shot_strategy: multi_shot or one_take
pace_profile: medium_flow
route: product hero → hand operation → functional proof → result
transition_logic: match movement or macro inserts
```
