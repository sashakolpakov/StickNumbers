# Reproducibility

The authoritative paper sources are
`manuscript/knot_fewnomials.tex` and its compiled counterpart
`manuscript/knot_fewnomials.pdf`. Run all commands below from the repository
root unless a command changes directory explicitly.

## Manuscript

The paper uses a standard LaTeX installation with `latexmk`, `amsmath`,
`amsthm`, `hyperref`, and TikZ.

```sh
cd manuscript
latexmk -r .latexmkrc -pdf -interaction=nonstopmode -halt-on-error knot_fewnomials.tex
```

The build should resolve every citation and cross-reference without LaTeX or
package warnings. The PDF is a versioned research artifact; auxiliary LaTeX
files are ignored. The checked-in configuration fixes the build clock to
23 October 2026 UTC; the TeX date is explicit. This gives repeatable PDF bytes
with the same TeX installation, without asserting identity across TeX versions.

## Arithmetic audit

The audit script uses only the Python standard library:

```sh
python3 scripts/repro/fewnomial_bound_audit.py \
  --check-doubly-alternating 50 100 500 2000 10000
```

It performs three distinct checks:

1. compares the naive chamber estimate with the factorial-sensitive partial
   binomial estimate responsible for the linear base in $N$;
2. checks the finite stick-budget and Stirling-envelope arithmetic for the
   explicit quarter-family Garside construction; and
3. enumerates the small doubly down--up sets through $n=9$, checking
   $(k!)^4\leq\lvert G_{4k}\rvert$ whenever applicable.

This numerical script is an audit, not a substitute for any cited
real-algebraic, braid-theoretic, or knot-theoretic input.

A fast syntax check is:

```sh
python3 -m py_compile scripts/repro/fewnomial_bound_audit.py
```

## Lean verification

The pinned Lean 4/mathlib project is in `formal/`:

```sh
cd formal
lake exe cache get
make verify
```

The first command downloads mathlib's compiled cache when available; it is an
optimization, not part of the proof. The second builds the complete project,
scans project sources excluding comments, and compiles every declaration in
the root axiom audit. Lean's `#print axioms` output may mention
the standard foundations used by mathlib—`propext`, `Classical.choice`, and
`Quot.sound`—but no project-specific axiom. See
[FORMAL_VERIFICATION.md](FORMAL_VERIFICATION.md) for the checked statements and
the deliberate proof boundary.  A successful build verifies the core lemmas
and conditional proof graph; it does not turn the external ambient-isotopy,
Barone--Basu, Garside, or knot-theoretic inputs into Lean proofs.

## Corpus handoff

See [corpus/README.md](corpus/README.md). The preparation script creates a
standalone manuscript/Lean/development-summary tree and verifies its file
hashes and relative links. It does not modify another checkout or publish it.

## Sphinx documentation

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r docs/requirements.txt
sphinx-build -W --keep-going -b html docs docs/_build/html
```

The Sphinx configuration reads the paper title and authors directly from the
TeX source. It also copies the authoritative TeX and PDF into the generated
site, so the documentation does not maintain a shadow manuscript.
