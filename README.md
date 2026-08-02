# StickNumbers

This repository accompanies the manuscript **“Discriminant Varieties for
Stick Knots and Links”** by Alexander Kolpakov and Igor Rivin.  The paper gives
quantitative upper and lower bounds for the number of knot types realizable by
polygonal knots with at most $N$ sticks.

The manuscript is the source of truth:

- [TeX source](manuscript/knot_fewnomials.tex)
- [compiled PDF](manuscript/knot_fewnomials.pdf)

The principal knot-counting result is the asymptotic growth law

$$
\log \lvert\mathcal K_N\rvert=\Theta(N\log N),
\qquad
\lvert\mathcal K_N\rvert=N^{\Theta(N)}.
$$

A quantitative refinement gives

$$
N^{(2/3+o(1))N}
\leq \lvert\mathcal K_N\rvert
\leq N^{3N+o(N)}.
$$

Here $\mathcal K_N$ is the set of knot types with stick number at most
$N$.  This is an asymptotic growth theorem: it pins down the factorial scale
$N^{\Theta(N)}$, equivalently the order $N\log N$ of the logarithm.  A
finer asymptotic equivalent remains open.

The central result is the direct real-algebraic upper bound. The generic route
through crossing-number enumeration gives only $\exp(O(N^2))$. A 2025
strong-geometry reconstruction theorem already implies the factorial scale;
counting the signs actually used in its proof gives $N^{6N+o(N)}$. Counting
the connected chambers of the cubic/quartic self-intersection discriminant
sharpens this to $N^{3N+o(N)}$. An explicit Garside construction supplies the
$N^{(2/3+o(1))N}$ lower bound, already among prime satellite knots.

## What is included

- `manuscript/`: the authoritative TeX source and compiled paper.
- `formal/`: a pinned Lean 4/mathlib project giving a complete conditional
  certificate of the principal finite and asymptotic knot-counting deductions.
- `scripts/repro/fewnomial_bound_audit.py`: a standard-library-only numerical
  audit of the upper-bound entropy saving, the lower-bound budget, and small
  doubly alternating permutation counts.
- `announcements/`: copy-ready LinkedIn and X launch posts centered on the
  topology-to-chamber-counting breakthrough.
- `docs/`: Sphinx documentation which points back to the manuscript for all
  theorem statements and proofs.
- `NOVELTY_AUDIT.md`: a qualified literature audit for the counting result.

The exact formalization boundary is recorded in
[FORMAL_VERIFICATION.md](FORMAL_VERIFICATION.md). Lean works with the actual
polygonal wall space, multivariate wall polynomials, path components,
permutation words, endpoint fibers, and the bounded-stick subtype of a supplied
knot-type interface. From typed
ambient-isotopy, Barone--Basu, Garside, Malyutin--Stupakov, and Huh--Oh inputs,
it proves the finite bounds, the headline $\Theta(N\log N)$ law, and the
one-sided $2/3$ lower exponent. Those cited inputs are not claimed to have been
formalized; the complete downstream proof graph is kernel checked.

## Quick verification

Compile the manuscript:

```sh
cd manuscript
latexmk -pdf -interaction=nonstopmode -halt-on-error knot_fewnomials.tex
```

Run the finite arithmetic audit:

```sh
python3 scripts/repro/fewnomial_bound_audit.py \
  --check-doubly-alternating 50 100 500 2000 10000
```

Build the Lean development:

```sh
cd formal
lake exe cache get
lake build
```

See [REPRODUCIBILITY.md](REPRODUCIBILITY.md) for complete instructions.

## Documentation

The Sphinx site is built from `docs/`; its paper page serves the exact TeX and
PDF from `manuscript/` rather than maintaining a second copy.  Locally:

```sh
python3 -m pip install -r docs/requirements.txt
sphinx-build -W --keep-going -b html docs docs/_build/html
```

The published site is intended for
<https://sashakolpakov.github.io/StickNumbers/>.

## Attribution

The authors used OpenAI's GPT-5.6-sol to help strengthen the results, improve
the exposition, and generate and audit the accompanying Python and Lean 4
code.  See [ACKNOWLEDGMENTS.md](ACKNOWLEDGMENTS.md) for the full statement.
