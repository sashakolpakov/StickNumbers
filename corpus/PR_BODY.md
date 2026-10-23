This proposes *Discriminant Varieties for Stick Knots and Links*, by
Alexander Kolpakov and Igor Rivin, as an external model-assisted contribution
for mathematical review. For knot types realizable with at most `N` sticks,
it gives, to the authors' knowledge, the first explicit determination of
the logarithmic growth order. It proves the window
`N^((2/3+o(1))N) ≤ |K_N| ≤ N^(3N+o(N))`, hence sharp logarithmic growth order
`log |K_N| = Θ(N log N)`.

The proof directly counts cubic/quartic discriminant chambers and uses the
Garside/arc-index construction for the lower bound. It is independent of
strong-geometry reconstruction. The manuscript briefly notes that related
reconstruction work could, in principle, supply another counting approach;
the audit retains that separate retrospective derivation. This candidate is
the audited repository revision,
dated 23 October 2026, rather than an unchanged copy of arXiv v1.

The contribution includes one manuscript and its build source, a standalone
pinned Lean project, a two-page retrospective development summary and its
source/coverage statement, mathematical and contribution audits, exact source
hashes and a repeatable artifact checker. The summary does not reconstruct
original model turns or authenticate an unavailable conversation export.
The manuscript's existing model-assistance acknowledgment is preserved.

Lean checks the principal internal finite and asymptotic deductions from
explicit external geometry, real-algebraic, braid and knot-theoretic inputs.
The new arithmetic module discharges the optimized floor/log deficit and
derives every eventual upper coefficient above 3. This remains a conditional
certificate, not a formalization of the classical ambient-isotopy quotient
or the cited external theorems. The auxiliary link construction is reviewed
in the written audit and lies outside Lean's target.

The package retains Lean 4.32.0 and its exact mathlib manifest, independently
of the parent library. It has no parent Comparator target and is indexed
separately from internal-model totals and unconditional formalization entries.
Authorship is retained; no new license grant is asserted where the source
project supplies none.

Validation is recorded in the exported release manifest: complete Lean build,
12-source scan and 17 compiled declaration/axiom checks; numerical finite
audit; manuscript and summary builds; two isolated clean rebuilds of each
PDF; relative-link, artifact-hash and bounded metadata checks.

Source: [sashakolpakov/StickNumbers](https://github.com/sashakolpakov/StickNumbers),
starting revision `ee6d8f8c5cb3c4ef9f154e1173a7d05ffe9452b6` plus the
inventoried candidate changes. The release manifest records their exact hashes.
