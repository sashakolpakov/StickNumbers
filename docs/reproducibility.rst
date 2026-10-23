Reproducibility
===============

`Read the complete reproducibility guide <REPRODUCIBILITY.md>`__.

The three principal checks are:

.. code-block:: console

   $ cd manuscript
   $ latexmk -r .latexmkrc -pdf -interaction=nonstopmode -halt-on-error knot_fewnomials.tex

.. code-block:: console

   $ python3 scripts/repro/fewnomial_bound_audit.py \
       --check-doubly-alternating 50 100 500 2000 10000

.. code-block:: console

   $ cd formal
   $ lake exe cache get
   $ make verify

The Python audit uses only the standard library. The Lean and LaTeX dependency
versions are controlled by the files in their respective project directories.
