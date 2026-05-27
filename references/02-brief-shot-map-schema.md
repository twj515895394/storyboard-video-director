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
  aspect_ratio: "16:9"
  language_policy:
    explanation: zh
    storyboard_labels: zh
    final_prompts: zh_en
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

## Layer 4: Shot Map

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
  shot_count: ""
  shot_density: low | medium | high
  multi_clip: false
  continuity_strength: low | medium | high
  audio_priority: sfx | bgm | dialogue | ambient | none
  subtitle_policy: disabled_by_default
```
