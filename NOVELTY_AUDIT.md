# Novelty audit for the stick-knot counting result

Audit date: 2026-08-02.

## Result being audited

For

$$
\mathcal K_N=\{K:\mathrm{stick}(K)\le N\},
$$

the manuscript proves

$$
N^{(2/3+o(1))N}\le |\mathcal K_N|\le N^{3N+o(N)}.
$$

Consequently

$$
\log |\mathcal K_N|=\Theta(N\log N).
$$

The defensible novelty claim is now precise:

- The direct self-intersection-discriminant argument gives the new upper
  bound $N^{3N+o(N)}$ using only $O(N^2)$ cubic and quartic walls in $3N$
  coordinates.
- Gros--Ramirez Alfonsin's November 2025 strong-geometry reconstruction
  theorem already implies a factorial-scale upper bound after standard
  sign-pattern counting. The full wedge table gives $N^{33N+o(N)}$; extracting
  only the signs used in their proof gives $N^{6N+o(N)}$. Their paper does not
  print these counting corollaries, but they are mathematically implicit and
  must be credited.
- The manuscript therefore improves the strongest readily extracted prior
  upper exponent from $6$ to $3$; it must not claim that no $N^{O(N)}$ upper
  bound was previously implicit.
- The Garside/Malyutin--Stupakov construction gives the new explicit lower
  exponent $2/3$, already among prime satellite knots. Earlier printed
  arc-index results already implied a smaller positive factorial exponent.
- The bounds determine an asymptotic growth order, not an asymptotic
  equivalent and not a limit for $\log|\mathcal K_N|/(N\log N)$.

## Closest prior results checked

| Source | What it gives | Relation to the manuscript |
|---|---|---|
| Freedman--He--Wang, *Möbius energy of knots and unknots* (1994), <https://doi.org/10.2307/2946626> | Exponential growth in crossing number. With the $O(N^2)$ crossing bound for an $N$-stick polygon, this gives the coarse baseline $\exp(O(N^2))$. | A classical general upper bound exists. |
| Calvo, *Geometric knot spaces and polygonal isotopy* (2001), <https://arxiv.org/abs/math/9904037> | Models labeled $N$-gons in $\mathbb R^{3N}$ and describes nonincident-edge intersection loci as cubic semialgebraic pieces; components of the embedding locus are geometric knot types. | Direct geometric precursor. The new upper theorem quantitatively counts a deliberately enlarged low-degree wall complement; the discriminant encoding itself is not new. |
| Randell--Simon--Tokle, *Möbius transformations of polygons and partitions of 3-space* (2008), <https://arxiv.org/abs/math/0602466> | Theorem 7 proves an exponential lower bound by polygon length. | Direct prior counting result, but below the factorial scale. |
| Millett, *Physical knot theory* (2010 manuscript), <https://web.math.ucsb.edu/~millett/Preprints/MillettTriesteLectures.pdf> | Problem 5.2 asks how many knot types occur among equilateral $N$-gons and reports no useful edge-number estimate at that time. | Historical evidence only; the model is equilateral. |
| Malyutin--Stupakov, *On the number of knots with a given arc index* (2022), <https://www.pdmi.ras.ru/preprint/2022/22-07.html> | Theorem 1 gives at least $\lfloor(k+4)/11\rfloor!$ oriented prime knots of arc index at most $k$. Proposition 1 injects $PB_n$ into oriented prime satellite knots with arc index at most $n\max\{11,s+8\}-4$ for an $s$-factor input. | The printed theorem plus Huh--Oh already gives $N^{(2/33+o(1))N}$ stick-bounded knots. The new variable-length extraction raises the exponent to $2/3$. |
| Elrifai--Morton, *Algorithms for positive braids* (1994), <https://doi.org/10.1093/qmath/45.4.479> | Starting/finishing sets and uniqueness of left canonical form for positive braids. | External Garside input ensuring that the selected long words are distinct. |
| Huh--Oh, *An upper bound on stick numbers of knots* (2011), <https://doi.org/10.1142/S0218216511008966> | $\mathrm{stick}(K)\le \tfrac32(\alpha(K)-1)$ for nontrivial knots. | Converts the arc-index construction into a stick-number lower bound. |
| Gros--Ramirez Alfonsin, *Strong geometry: knots*, v3 (2025), <https://arxiv.org/abs/2504.00197v3> | Theorem 1 says isomorphic affine strong geometries of generic point configurations yield isotopic polygonal knots; the following corollary says the wedge matroid alone suffices. | This already turns finite sign data into a knot classifier. The full $N^{12}$-slot degree-$9$ table yields $N^{33N+o(N)}$ by standard sign counting. The $O(N^3)$ degree-at-most-$6$ queries actually used in their proof yield $N^{6N+o(N)}$. These are derived consequences, not printed bounds. |
| Cantarella--Rechnitzer--Schumacher--Shonkwiler, *New upper bounds for stick numbers* (2025), <https://arxiv.org/abs/2508.18263> | Computational upper bounds for individual stick numbers. | Does not count all types realizable with $N$ sticks. |
| Pollack--Roy, *On the number of cells defined by a set of polynomials* (1993) | Dimension-sensitive cell bounds retaining the essential $(sd/m)^m$ dependence. | Shows that the real-algebraic technology predates this manuscript. |
| Barone--Basu, *Refined bounds on the number of connected components of sign conditions on a variety* (2012), <https://arxiv.org/abs/1104.0636> | Explicit component bounds for realizable sign conditions. | External theorem used on the actual cubic/quartic wall family. |

## Derivation of the strong-geometry comparison

For clarity, this is why the 2025 reconstruction paper changes the novelty
claim.

Homogenize each vertex to $v_i=(1,p_i)\in\mathbb R^4$. Its full wedge ground
set contains a normal to every ordered triple of the $v_i$, hence at most
$N^3$ normals. The rank-four wedge chirotope has at most $N^{12}$ sign slots.
Unit normalization can be removed without changing a sign. In the resulting
cofactor normal, one coordinate has degree $3$ and the other three have degree
at most $2$, so every four-normal determinant has degree at most $9$. With
$3N$ real variables, standard fixed-degree sign-pattern counting gives

$$
\left(C\frac{N^{12}}{N}\right)^{3N}
=N^{33N+o(N)}.
$$

The proof of their knot theorem uses much less data: $O(N^2)$ affine signs for
crossings, over/under information, and crossing signs, plus $O(N^3)$ witness
signs ordering crossings along projected edges. The witness determinants have
degree at most $6$. Counting just these sign queries gives

$$
\left(C\frac{N^3}{N}\right)^{3N}
=N^{6N+o(N)}.
$$

Their reconstruction theorem turns equality of these labeled data into equal
knot type. Generic perturbation within the open PL embedding locus covers all
stick-bounded knot types. This is a sign-pattern count, not a chamber count.
The new discriminant argument obtains $N^{3N+o(N)}$ by counting components of
a smaller $O(N^2)$ wall complement.

## Lower-bound audit

The new lower proof no longer needs RSK or alternating-permutation
asymptotics. For $n=4k$, four arbitrary permutations of $k$ letters give an
explicit injective family of doubly down--up permutations of size $(k!)^4$.
Lean checks the construction, both descent conditions, injectivity, and

$$
(4k)!\le 2^{9k}(k!)^4.
$$

Elrifai--Morton normal-form uniqueness makes every $q$-letter word distinct;
endpoint pigeonholing costs $(4k)!$; Malyutin--Stupakov and Huh--Oh transfer
the family to stick-bounded prime satellite knots; forgetting orientation
costs at most $2$. Optimizing $q\sim\log N$ gives the $2/3$ exponent. Focused
searches found no prior use of this explicit family and variable-length
Garside optimization in the stick-number counting problem.

## Formal-verification status

The Lean development is a complete conditional certificate of the principal
stick-knot deductions, not an unconditional formal proof of the external
literature or the auxiliary link construction. It uses actual polygon
configurations, multivariate wall polynomials, paths and connected components,
permutation words and endpoint fibers, plus supplied braid and knot interfaces
and their pure-braid and bounded-stick subtypes. From
typed semantic, Barone--Basu, Garside, Malyutin--Stupakov, and Huh--Oh
interfaces it derives the final finite inequalities. No free numerical
“number of chambers/braids/knots” is assumed. It then proves the headline
`Theta(N log N)` law and, by a fixed-word argument, the eventual lower bound
with every coefficient `c < 2/3`. The optimized finite parameters are also
checked; only the optional explicit `-(2/3)N log log N + O(N)` evaluation is
left behind a typed elementary-arithmetic interface. See `formal/README.md`
for the exact boundary.

## Defensible announcement wording

Use:

> We prove the explicit window
> $N^{(2/3+o(1))N}\le |\mathcal K_N|\le N^{3N+o(N)}$ for knot types realizable
> with at most $N$ sticks. A recent strong-geometry reconstruction theorem
> already implies the factorial upper scale; the signs used in its proof give
> $N^{6N+o(N)}$. Our direct cubic/quartic discriminant count sharpens that to
> $N^{3N+o(N)}$, while an explicit Garside construction gives the $2/3$ lower
> exponent.

Do not claim that no $N^{O(N)}$ upper bound was previously implicit. Do not
claim the first superexponential lower bound. Do not describe Calvo's
discriminant or the general sign-condition theorem as new. The strongest story
is the direct topology-to-algebraic-chambers bridge, the substantially sharper
upper exponent, the explicit lower construction, and the kernel-checked
conditional proof graph.
