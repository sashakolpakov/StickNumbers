# Corpus handoff

This candidate follows the external-contribution layout inspected in the
arithmetic-trace-rigidity contribution to `openai/math`: one dated preprint,
one standalone pinned Lean package, and one retrospective development summary
under `reasoning_traces/`. All preparation stays in this repository.

The [mathematical audit](MATHEMATICAL_AUDIT.md) reviews the written arguments
and priority claim. The [manuscript map](../formal/MANUSCRIPT_MAP.md) records
the formal boundary. The [contribution audit](CONTRIBUTION_AUDIT.md) explains
the export and its limitations.

From the repository root, prepare and verify the complete candidate:

```sh
python3 scripts/prepare_corpus.py
```

This runs the Lean build and source/axiom audit, finite Python audit, both PDF
builds, and isolated clean PDF rebuilds. It exports only the selected source
files and documents into `corpus/_build/math/`, then checks its hashes and
relative links. It preserves the toolchain and exact dependency manifest;
it does not export dependency caches, Git history, session records or build
logs. Python 3, Lean/Lake, Latexmk and `pypdf` are required.

The output contains:

```text
preprints/Discriminant-Varieties-for-Stick-Knots-and-Links-October-23-2026/
lean/StickKnots/
reasoning_traces/stick-knot-counting.{md,tex,pdf,latexmkrc}
```

Recheck a prepared tree without rebuilding:

```sh
python3 scripts/check_corpus.py corpus/_build/math
```

When continuing in the corpus checkout, copy these three **new** paths into
the checkout, inspect [CATALOGUE_ADDITIONS.md](CATALOGUE_ADDITIONS.md), and
apply its additions to the existing README, contents and Lean index. Use
[PR_BODY.md](PR_BODY.md) for the proposed contribution description. Keep the
existing collection totals and the separate arithmetic-trace contribution.
The source files are copied verbatim except for documented path adaptation
in the standalone package README.

The handoff is ready for review, not a claim of upstream acceptance. No
changes to another checkout, branch publication or PR creation are performed
here. A fresh archive under `corpus/_build/sticknumbers-contribution.tar.gz`
contains the same three contributed paths for convenient transfer.
