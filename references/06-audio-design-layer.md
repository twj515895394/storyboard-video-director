# Audio Design Layer

Audio Design is a default inspection dimension, not a mandatory block that must be filled in every prompt.

## Adaptive rules

- Action/mechanical/sports: prioritize SFX, rhythm, impacts, servo/metal/footstep detail.
- Emotional/mood/ad film: prioritize BGM, ambience, silence, breathing room.
- Vlog/social/roleplay: include dialogue, voiceover, caption rhythm only if useful.
- Product demo/training: include operation sounds, UI feedback, short narration only if needed.
- Silent visual film: explicitly say minimal sound, ambient only, or no dialogue.

## Do not force

Do not force:

- dialogue;
- voiceover;
- BGM;
- subtitles;
- sound effects for quiet scenes.

## Audio block pattern

Use only the rows that matter:

```text
AUDIO DESIGN:
- Dialogue: none / short line / natural exchange.
- Voiceover: none / concise narration.
- SFX: [specific sound events per action].
- BGM: [mood, tempo, instrument feel], optional.
- Rhythm: [staccato / slow-burn / rising / impact pauses].
- Audio transitions: [whip, hard cut, reverb tail, silence].
```

## SFX precision

For physical action, bind sound to visible cause:

- screw bites → metal click;
- bolt drops → bounce on concrete;
- robot buckles → servo strain + concrete impact;
- dust settles → soft granular falloff.

## BGM caution

If SFX is the primary information carrier, BGM should be subtle or omitted.
