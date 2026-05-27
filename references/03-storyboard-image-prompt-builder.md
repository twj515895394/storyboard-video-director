# Storyboard Image Prompt Builder

Use for gpt-image2 or similar image models when the output is a single storyboard sheet or production reference image.

## Default orientation

- Main default: 16:9 wide cinematic storyboard sheet.
- Panel count: dynamic; usually 4–8, complex up to 16.
- Text labels: Chinese by default; English if user chooses.
- Do not overload the image with long paragraphs.

## Structural modules

### 1. Overall sheet instruction

State the output as a polished storyboard sheet, production reference board, or hybrid visual proposal.

Example:

> Create a 16:9 wide cinematic storyboard and production reference sheet for [project]. Use [style]. Present the entire sequence in one clean, readable design.

### 2. Visual language

Include medium, realism level, lighting, color logic, texture, camera feel, and what to avoid.

### 3. Character / subject consistency

If a core subject exists, explicitly require identity consistency across all panels:

> Maintain strict consistency in character identity, facial features, body proportions, outfit progression, key props, and design language across every panel.

For products, robots, vehicles, or props, replace character identity with product/design identity.

### 4. Reference strip

Use adaptively.

- Film/video pre-production: include top reference strip.
- Simple social visuals: omit or simplify.
- Commercial pitch: use top strip + technical bar.

Reference strip may contain character, scene, lighting, style, props, lens/motion, and color references.

### 5. Main storyboard grid

For each panel include:

- panel number and short title;
- timecode or narrative beat;
- frame description;
- camera language;
- action/emotion;
- compact notes;
- key props/symbols.

### 6. Technical reference bar

Use adaptively:

- cinematic: aspect ratio, lens feel, camera movement, color, lighting, editing rhythm, audio mood;
- commercial: brand tone, product hero detail, motion style, sound mnemonic;
- simple image: keep technical info in prompt text only.

## Chinese label rule

Default image labels are Chinese. Keep them short:

- 第1镜 / 建立
- 冲突
- 转折
- 高潮
- 收束

Avoid dense paragraphs inside the image.

## Negative constraints

Add context-specific negative constraints:

- no crowded unreadable layout;
- no inconsistent character/product design;
- no random panel order;
- no long illegible text;
- no cheap template look;
- no style drift between panels.

For realistic storyboards, add: no anime unless requested, no excessive polish, no plastic skin, no fantasy effects unless required.

## Output pattern

When finalizing, provide:

1. 中文设计说明.
2. 中文 gpt-image2 Prompt.
3. English gpt-image2 Prompt.
