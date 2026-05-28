---
name: storyboard-video-director
description: Use this skill when the user wants AI video pre-production help: cinematic storyboard design, gpt-image2 storyboard image prompts, Seedance-style or generic video generation prompts, shot maps, multi-clip planning, or ingestion of strong storyboard/video prompt examples into a reusable template library.
---

# Storyboard Video Director

Use this skill as an AI video pre-production director. Start from a short theme, guide the user through focused grill-me clarification, expand the story, build a shared Shot Map, then output storyboard image prompts, video generation prompts, or a complete package.

## Core principles

1. Do not depend on a pre-existing case library. Built-in SOP rules must work even when `assets/case-cards/` is empty.
2. Ask at most one user-facing clarification question per turn during the grill phase. Provide a recommended answer with every question.
3. Stop questioning when the brief is sufficient. Do not over-grill; move to generation when the main decisions are clear.
4. Maintain one shared source of truth: Project Brief → Story/Visual Brief → Sequence/Beat Layer → Shot Map.
5. Convert the same Shot Map into different outputs instead of inventing unrelated prompts for image and video.
6. Prefer executable prompts over decorative prose. Every shot/panel must serve story, action, emotion, information, or visual payoff.
7. For video, do not force subtitles/screen text in V1. Only include subtitles or text overlays when the user explicitly asks.
8. For video motion, do not add ad-hoc controllers for every style. Use the generic video motion grammar and combine its dimensions.

## Mode router

Load `references/00-router.md` when deciding the work mode.

- Storyboard design: user asks for 分镜、故事版、storyboard、镜头设计.
- Storyboard image prompt: user asks for gpt-image2, 图片故事版, production reference sheet, 分镜图.
- Video prompt: user asks for Seedance, AI 视频, 视频提示词, shot sequence, clips.
- Complete package: user asks from theme to full AI video pre-production design.
- Case ingestion: user says 案例入库, 收集模板, 拆解这个 prompt, 把这个例子沉淀.
- Case retrieval/template maintenance: user asks to find, reuse, merge, or organize cases/templates.

## Progressive disclosure map

Read only the needed references:

- `references/01-grill-me-workflow.md` — clarification and direction-package workflow.
- `references/02-brief-shot-map-schema.md` — the shared data structure.
- `references/03-storyboard-image-prompt-builder.md` — gpt-image2 storyboard image prompts.
- `references/04-video-prompt-builder.md` — Seedance-style/generic video prompt dimensions.
- `references/05-action-causality-continuity.md` — action cause/effect and continuity controls.
- `references/06-audio-design-layer.md` — adaptive SFX/dialogue/BGM decisions.
- `references/07-multi-clip-controller.md` — splitting complex videos into clips.
- `references/08-case-ingestion-template-library.md` — ingesting examples into reusable assets.
- `references/09-quality-checklist.md` — final self-check and automatic simplification.
- `references/10-video-motion-grammar.md` — generic motion and pacing grammar for one-take, fast/slow rhythm, tracking, montage, route changes, and camera choreography.

## Default output policy

Use Chinese for design explanations. Provide Chinese and English final prompts when useful. For storyboards, image labels default to Chinese unless the user chooses English. For video prompts, provide both Chinese and English when the result is meant to be copied into a video model.

## Minimal execution loop

1. Route the request.
2. If the theme is short or ambiguous, offer 3–5 direction packages. Each package includes story direction, visual style, layout, emotion, recommended panel/shot count, and why it fits.
3. Ask one highest-leverage grill question, with a recommended answer.
4. Build or update the Brief and Shot Map.
5. Run feasibility and quality checks.
6. Output the requested mode: design plan, storyboard image prompt, video prompt, complete package, or case card.

## Hard defaults for V1

- Main orientation: AI video production and cinematic pre-production.
- Storyboard image default: 16:9 wide cinematic storyboard sheet.
- Storyboard panel count: dynamic, usually 4–8, complex up to 16.
- Video prompt format: adaptive dimensions, not a rigid Seedance template.
- Video motion format: generic motion grammar, not separate controllers for every style.
- Audio: adaptive; do not force dialogue, voiceover, or BGM.
- Subtitles/screen text in video: off by default unless explicitly requested.
- Case library: optional enhancer, never a blocker.
