# Grill-Me Workflow

The user may provide only a short theme. The skill must expand it without becoming a questionnaire.

## Rule

Ask only one user-facing question per turn during clarification, and always include a recommended answer.

## Adaptive depth

- Clear brief: ask 0–2 questions, then generate.
- Normal brief: ask 3–5 questions across intent, story, style, output.
- Very vague or high-stakes creative project: ask until the main dependencies are resolved, but stop once enough detail exists.

## Direction packages

When the user gives a short theme, first generate 3–5 direction packages. Each package should contain:

1. Direction name.
2. Story route.
3. Visual style.
4. Layout or video rhythm.
5. Emotional tone.
6. Recommended panel/shot count.
7. Suitable use case.
8. Why this direction fits.

Do not treat direction packages as final. They are creative handles for selection, mixing, or rejection.

## Question priority

Choose the next question by the highest unlocked dependency:

1. Output target: storyboard image, video prompt, or complete package.
2. Use case: AI short film, ad, vlog, product demo, training, mood film.
3. Core subject: character/product/space/concept.
4. Story engine: conflict, transformation, process, reveal, demonstration.
5. Visual style: realistic, cinematic, anime hybrid, documentary, commercial, painterly 3D, etc.
6. Duration/panel count if video or storyboard density matters.
7. Reference assets and consistency requirements.

## When to stop grilling

Stop and generate when these are clear enough:

- Intended output.
- Core subject and scene.
- Story direction or beat logic.
- Visual style.
- Approximate duration or panel/shot density when needed.
- Any strict constraints.

Small gaps should be resolved with sensible defaults instead of extra questions.
