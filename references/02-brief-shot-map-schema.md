# Brief and Shot Map Schema

Use one shared source of truth for both storyboard image prompts and video prompts.

## Layer 1: Project Brief

```yaml
project_brief:
  title: ""
  user_goal: ""
  output_mode: design | image_prompt | video_prompt | complete_package | case_ingestion
  primary_medium: storyboard_image | video | both
  target_model: gpt-image2 | seedance | generic_video | unspecified
  audience: ""
  use_case: short_film | ad | vlog | training | product_demo | mood_film | other
  aspect_ratio: "9:16 | 16:9 | 1:1 | 4:5 | custom"
  orientation: vertical | horizontal | square | custom
  target_platform: douyin | xiaohongshu | youtube | presentation | generic | unspecified
  aspect_ratio_policy: required_for_video
  timeline_policy: required_for_direct_video | ask_for_storyboard_based_video | optional | disabled
  language_policy:
    explanation: zh
    storyboard_labels: zh
    final_prompts: zh_en
```

## Video aspect ratio rule

Aspect ratio is required for video prompt generation.

- Direct video prompt generation: include aspect ratio in `project_brief` and final prompt.
- Complete package with video prompt: include aspect ratio in the video section.
- Storyboard image to video prompt: ask whether to inherit the storyboard aspect ratio or choose a new video ratio.
- If user does not specify and asks for immediate generation, choose a context-aware default and state it explicitly.

Recommended default question:

```text
这个视频主要用于哪里？A 竖屏 9:16（抖音/小红书/Seedance常用，默认推荐） B 横屏 16:9（电影感/YouTube/PPT） C 方形 1:1 D 自定义比例。
我的推荐：短视频平台优先 9:16；电影感环境展示优先 16:9。
```

## Layer 2: Story / Visual Brief

```yaml
story_visual_brief:
  logline: ""
  subjects:
    - id: subject_1
      role: protagonist | product | robot | environment | symbolic_object
      description: ""
      consistency_priority: high | medium | low
      reference_asset: "@[image1]"
      reference_usage: identity | product_design | scene | style | layout
  scene_world: ""
  story_arc: ""
  emotional_progression: []
  visual_motifs: []
  color_logic: ""
  style_language: ""
  constraints: []
```

## Layer 3: Sequence / Beat Layer

Use this layer when the project has more than 4 shots/panels or clear dramatic phases.

```yaml
beats:
  - id: beat_1
    name: "建立 / setup"
    function: "establish subject, space, and tension"
    start_state: ""
    end_state: ""
    shots: [1, 2, 3]
```

## Layer 4: Timeline / Beat Map

Use this layer for video prompt generation.

Rules:

- Direct video prompt generation without a storyboard image: timeline is required.
- Complete package including video prompt: timeline is required in the video section.
- Video prompt from an existing storyboard image: ask the user whether to add timeline unless they already specify it.
- If the user declines timeline for storyboard-based conversion, preserve panel order and continuity without explicit timestamps.

```yaml
timeline_beat_map:
  required: true
  source: direct_video_prompt | storyboard_image_conversion | complete_package
  total_duration: "8s"
  beat_style: one_take_internal_beats | edited_shot_timeline | multi_clip_timeline
  beats:
    - time: "0.0-1.0s"
      visual_action: ""
      camera_motion: ""
      scene_route_state: ""
      continuity: ""
      audio_cue: ""
```

## Layer 5: Shot Map

```yaml
shot_map:
  - shot: 1
    beat: beat_1
    time: "0-2s"
    panel_title: ""
    story_function: setup | action | transition | reveal | payoff
    frame_description: ""
    camera:
      shot_size: extreme_wide | wide | medium | close_up | macro
      angle: eye_level | low_angle | high_angle | overhead | worm_eye
      movement: locked | push_in | pullback | tracking | handheld | whip_pan
      lens_feel: "24mm / 35mm / macro / telephoto feel"
    action:
      subject_action: ""
      cause: ""
      effect: ""
      continuity_from_previous: ""
    audio:
      dialogue: ""
      voiceover: ""
      sfx: ""
      bgm: ""
      silence_or_pause: ""
    design_notes:
      props: []
      text_labels: []
      generation_constraints: []
```

## Extensions

### Storyboard image extension

```yaml
storyboard_image_extension:
  layout: wide_storyboard_sheet
  reference_strip: adaptive
  technical_bar: adaptive
  panel_count: 4-16
  image_text_density: minimal
```

### Video prompt extension

```yaml
video_prompt_extension:
  duration: ""
  aspect_ratio: "9:16 | 16:9 | 1:1 | 4:5 | custom"
  orientation: vertical | horizontal | square | custom
  target_platform: ""
  aspect_ratio_required: true
  shot_strategy: one_take | multi_shot | montage | loop | clip_series
  timeline_required: true
  timeline_question_required: false
  shot_count: ""
  shot_density: low | medium | high
  multi_clip: false
  continuity_strength: low | medium | high
  audio_priority: sfx | bgm | dialogue | ambient | none
  subtitle_policy: disabled_by_default
```
