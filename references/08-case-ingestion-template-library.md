# Case Ingestion and Template Library

The case library is an enhancer, not a dependency. If no cases exist, use built-in SOP rules.

## Case ingestion trigger

Use this mode when the user says:

- 把这个案例入库;
- 拆解这个 prompt;
- 这个例子不错，沉淀一下;
- 收集成模板;
- 基于这个案例以后复用.

## Ingestion workflow

1. Preserve the raw example or a short source note.
2. Classify the case type.
3. Deconstruct the structure.
4. Extract reusable modules.
5. Identify non-reusable parts.
6. Assign or propose a template family.
7. Generate a case card in `assets/case-cards/`.
8. Decide whether to update `assets/templates/template-families.md`.

## Case card fields

```yaml
case_name: ""
mode: storyboard_image | video_prompt | complete_package
template_family: ""
source_type: prompt | image | link | mixed
use_cases: []
layout_structure: ""
shot_or_panel_count: ""
beat_structure: []
visual_style: ""
camera_language: ""
audio_design: ""
action_causality: ""
reference_asset_strategy: ""
technical_bar_or_format: ""
reusable_modules: []
non_reusable_parts: []
variant_ideas: []
quality_notes: []
```

## Template family update rule

Promote a case into a template family when it has a reusable structure that can apply to at least three future tasks.

Do not blindly copy examples. Extract structure, rhythm, and constraints.
