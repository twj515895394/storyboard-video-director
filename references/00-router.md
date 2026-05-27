# Router

Use this router before reading deeper references.

## Modes

### 1. Storyboard design mode
Trigger when the user asks for 分镜设计, 故事版, storyboard, 镜头方案, or a visual story plan without asking for final model prompts.

Output: creative summary, sequence/beat design, structured panel/shot table, and next-step options.

### 2. Storyboard image prompt mode
Trigger when the user wants a single storyboard sheet, production reference sheet, gpt-image2 prompt, wide storyboard image, image storyboard, or story infographic.

Read: `03-storyboard-image-prompt-builder.md`.

### 3. Video prompt mode
Trigger when the user asks for Seedance, AI 视频提示词, video prompt, shot sequence, multi-shot video, or a model-ready video generation prompt.

Read: `04-video-prompt-builder.md`, then `05-action-causality-continuity.md` and `06-audio-design-layer.md` as needed.

### 4. Complete package mode
Trigger when the user asks for a complete AI video pre-production plan, from theme to storyboard and video prompt.

Output: design plan + Shot Map + storyboard image prompt + video prompt. Use the same Shot Map for all outputs.

### 5. Case ingestion mode
Trigger when the user says 案例入库, 拆解这个案例, 把这个 prompt 沉淀, 收集模板, or provides an example for future reuse.

Read: `08-case-ingestion-template-library.md`.

### 6. Template maintenance/retrieval mode
Trigger when the user asks to find, merge, compare, clean, organize, or build template families from stored cases.

Read: `08-case-ingestion-template-library.md` and `assets/templates/template-families.md`.

## Routing fallbacks

- If user input is only a short theme, enter storyboard/video ideation flow and present 3–5 direction packages.
- If user explicitly asks for a file/package/update to repository, prioritize artifact creation over further grilling.
- If a request could be image or video, ask one question only when the output medium changes the result substantially. Otherwise output a complete package.
