Formal verification
===================

The pinned Lean 4/mathlib project gives a complete **conditional** certificate
of the principal knot-counting deductions. Deep cited theorems are supplied as
typed statements about the actual polygon objects and supplied braid and knot
interfaces; Lean checks
the constructions and all downstream finite and asymptotic reasoning.

`Read the declaration-level report <FORMAL_VERIFICATION.md>`__.

Certified conclusions
---------------------

Lean defines the actual polygon configuration space, cubic and quartic wall
polynomials, and genuine paths and path components. On supplied braid and knot
interfaces, it defines the bounded-stick subtype, explicit four-permutation
lower family, Garside words and endpoint fibers, purification, orientation
fibers, and prime-satellite target. It proves:

* the explicit unsliced real-algebraic upper bound;
* the finite lower bound
  :math:`((k!)^4)^q\leq 2(4k)!\,|\mathcal K_{s_{k,q}}|`;
* :math:`\log|\mathcal K_N|=\Theta(N\log N)`; and
* for every :math:`c<2/3`, eventually
  :math:`cN\log N\leq\log|\mathcal K_N|`;
* for every :math:`c>3`, eventually
  :math:`\log|\mathcal K_N|\leq cN\log N`; and
* the explicit lower deficit
  :math:`(2/3)N\log N-(2/3)N\log\log N-O(N)`.

The final item is proved with a sufficiently large fixed word length and does
not assume the optimized floor/log asymptotics. The sharper displayed
refinement is proved in ``ManuscriptArithmetic.lean``, which discharges the
floor/log arithmetic interface and composes it with the finite certificate.

External boundary
-----------------

Generic support and ambient-isotopy invariance, Barone--Basu, the classical
Artin-braid/Garside facts, Malyutin--Stupakov, Huh--Oh, and orientation reversal
remain cited inputs. Thus the long-word deduction is certified from a Garside
interface, but Garside theory itself is not claimed to be formalized.

The project contains no ``sorry``, ``admit``, ``native_decide``, or
project-specific ``axiom``. Root ``#print axioms`` audits report only the
standard foundations ``propext``, ``Classical.choice``, and ``Quot.sound``.
