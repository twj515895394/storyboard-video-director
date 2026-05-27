# Action Causality and Continuity

Use this module whenever the prompt includes motion, interaction, physical effects, product usage, mechanical events, fight/chase scenes, or multi-clip generation.

## Action causality

Action causality answers: why does the result happen?

Strength levels:

- Strong: action, mechanical, combat, chase, product demo. Results must be triggered by visible actions.
- Medium: drama, vlog, emotional story. Behavior and emotion must progress logically.
- Weak: mood film, MV, abstract visuals. Transitions can be driven by rhythm, music, or visual metaphor.

Strong causality pattern:

```text
visible setup → tool/contact/action → immediate mechanical/physical response → result/payoff
```

Bad pattern:

```text
The robot falls apart.
```

Good pattern:

```text
The red screwdriver engages the visible shoulder bolt, the character twists it loose, the bolt pops free, and only then the shoulder plate separates.
```

## Action continuity

Action continuity answers: how does the next shot connect?

Track:

- subject position;
- movement direction;
- body state;
- held props;
- damage/changed object state;
- camera direction;
- scene geography;
- emotional state.

Continuity prompt language:

```text
Continue from the previous shot: [subject] is still [position/state], moving [direction], holding [prop]. The next shot begins with [connected action].
```

## State persistence checklist

Before final output, verify:

- The same character/product/robot appears in all relevant shots.
- Props do not disappear unless explained.
- Injuries/damage/outfit changes persist.
- The camera does not invert geography unintentionally.
- Results only occur after visible causes.
- Multi-clip ending states become next clip opening states.
