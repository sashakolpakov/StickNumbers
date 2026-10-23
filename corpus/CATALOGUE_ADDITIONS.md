# Proposed corpus catalogue additions

Append the following section to the corpus `CONTENTS.md`; preserve existing
external contributions and internal collection totals.

```markdown
## External contribution: stick-knot counting

**Manuscript authors:** Alexander Kolpakov and Igor Rivin.

This external model-assisted contribution is proposed for mathematical review
and listed separately from the internal-model collection totals.

| Manuscript | Result and supporting materials |
|---|---|
| [Discriminant Varieties for Stick Knots and Links](preprints/Discriminant-Varieties-for-Stick-Knots-and-Links-October-23-2026/knot_fewnomials.pdf) | To the authors' knowledge, the first explicit determination of the sharp logarithmic growth order by stick budget, with lower exponent 2/3 and upper exponent 3. [Source, citation and build](preprints/Discriminant-Varieties-for-Stick-Knots-and-Links-October-23-2026/README.md). |

[Standalone Lean certificate](lean/StickKnots/README.md) checks the principal
internal deductions from explicit external mathematical inputs, including
the optimized floor/log deficit. The [manuscript map](lean/StickKnots/MANUSCRIPT_MAP.md)
documents the exact boundary. The package has its own Lean 4.32.0 pins.

A [retrospective development summary](reasoning_traces/stick-knot-counting.pdf)
is accompanied by a [source and coverage statement](reasoning_traces/stick-knot-counting.md).
It is not an original conversation transcript.
```

Suggested README addition, outside the internal collection description:

```markdown
An external model-assisted contribution on stick-knot counting is available
in the [contributed manuscript catalogue](CONTENTS.md#external-contribution-stick-knot-counting),
with its manuscript, standalone conditional Lean certificate and retrospective
development summary.
```

Suggested addition to `lean/README.md` (paths relative to `lean/`):

```markdown
The external [stick-knot counting package](StickKnots/README.md) is a standalone
Lean 4.32.0 project checking internal deductions from cited mathematical inputs.
It is built separately from the parent library and has no Comparator target.
```
