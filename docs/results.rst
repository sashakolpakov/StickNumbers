Main results
============

Let :math:`\mathcal K_N` be the set of knot types with stick number at most
:math:`N`. The paper proves

.. math::

   N^{(2/3+o(1))N}
   \leq |\mathcal K_N|
   \leq N^{3N+o(N)}.

Consequently

.. math::

   \log |\mathcal K_N|=\Theta(N\log N),
   \qquad |\mathcal K_N|=N^{\Theta(N)}.

This determines the order of growth of the logarithm, not an asymptotic
equivalent or a limit for the normalized logarithm. The lower construction
already produces prime satellite knots.

Proof architecture
------------------

An :math:`N`-vertex polygon is represented in :math:`3N` real coordinates.
Its knot type can change only across a family of cubic and quartic
self-intersection walls. A dimension-sensitive real-algebraic component bound,
with the binomial denominator retained, gives the direct upper estimate
:math:`N^{3N+o(N)}`.

The generic crossing-diagram route gives the coarser baseline
:math:`\exp(O(N^2))`. To our knowledge, the present upper and lower bounds
give the first explicit determination of the sharp logarithmic growth order
in the stick budget. The proof is independent of strong-geometry
reconstruction results.

For the lower bound, an explicit family of doubly down--up permutations feeds
long Garside words, endpoint purification, the Malyutin--Stupakov injection,
and Huh--Oh's arc-to-stick inequality. The resulting one-sided coefficient is
:math:`2/3`.

The `paper <paper.html>`__ contains the complete proofs and citations. The
`formal-verification page <formal_verification.html>`__ records the exact
machine-checked boundary.
