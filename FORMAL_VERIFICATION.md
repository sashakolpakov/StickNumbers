# Formal verification

The pinned Lean 4.32/mathlib project in [`formal/`](formal/) is a **complete
conditional certificate** of the manuscript's principal stick-knot counting
deductions. It is not an unconditional formalization of the cited literature.

“Conditional” has a precise meaning here: deep results enter as typed theorem
parameters about the actual polygon objects and supplied braid and knot
interfaces. Lean then checks
the constructions and every downstream deduction to the finite and asymptotic
bounds. The certificate does not replace the hard inputs with unrelated
natural-number variables.

## What Lean proves

| Layer | Certified content |
|---|---|
| Polygonal geometry | Actual `Fin N → ℝ³` configurations, cyclic edges, cubic nonincident-edge walls, quartic adjacent-edge walls, evaluation identities, degree bounds, and wall avoidance implying finite-edge embeddedness |
| Components and knot count | Genuine mathlib paths and path components; openness/local path connectedness; factorization of a path-invariant classifier; surjection onto `{K // stickNumber K ≤ N}`; the explicit unsliced upper bound |
| Permutation family | An explicit injection of four copies of `S_k` into the doubly down--up permutations on `4k` letters, including both descent conditions and `(k!)⁴ ≤ |G_{4k}|` |
| Factorial control | `(4k)! ≤ 2^(9k)(k!)⁴`, its logarithmic loss, and mathlib Stirling estimates |
| Long words | The actual word type `Fin q → G_{4k}`, endpoint fibers, factorial pigeonholing, inverse-endpoint purification, purity, injectivity by cancellation, and the `q+1` factor-length bound |
| Knot transfer | Actual maps and subtypes for the Malyutin--Stupakov image, arc index, orientation forgetting, prime satellites, stick number, and the factor-two orientation loss |
| End-to-end finite bounds | Injection of the lower family into the bounded-stick subtype of the supplied knot-type interface; finiteness of that subtype derived from the upper certificate, not assumed on the lower side |
| Headline asymptotics | `log |K_N| = Θ(N log N)`, proved with `q=2`, `k=floor(N/132)` and internal floor/Stirling/asymptotic estimates |
| Refined lower exponent | For every real `c < 2/3`, Lean chooses a sufficiently large fixed `q` and proves eventually `c N log N ≤ log |K_N|`; this certifies the one-sided meaning of `N^((2/3+o(1))N)` |

The exact optimized finite choice

```text
q_N = floor(log N),
k_N = floor((2N+15)/(12(q_N+9)))
```

is also implemented, including its stick budget and factorial-free Stirling
envelope. The optional sharper
`-(2/3)N log log N + O(N)` evaluation is represented by the typed
`OptimizedDeficitArithmetic` interface; Lean verifies its composition with the
actual lower certificate. Neither the headline order nor the `2/3` lower
exponent depends on that interface.

## External theorem boundary

The following mathematics is cited rather than re-proved:

- generic support for bounded-stick knot types, PL stability, and ambient
  isotopy extension, packaged as a surjective path-invariant classifier on the
  actual wall-free polygon space;
- the uniform Barone--Basu component theorem for finite families of real
  polynomials of degree at most four;
- interpretation of the abstract braid carrier as the classical Artin braid
  group and the relevant Elrifai--Morton Garside normal-form, cancellation, and
  length statements;
- the Malyutin--Stupakov injection and arc-index estimate;
- Huh--Oh's stick/arc inequality; and
- the structural interpretation of forgetting knot orientation.

Thus the long Garside-word argument is Lean-certified from a typed Garside
interface; Garside theory itself is not claimed to be formalized. Likewise,
Lean reasons with the bounded-stick subtype of the supplied knot-type interface
but does not construct the ambient-isotopy quotient defining classical knot
types. The auxiliary link
construction in the manuscript is outside the current formal target.

## Build and audit

```sh
cd formal
lake exe cache get
lake build StickKnots

rg -n '(^|[[:space:]])(sorry|admit)([[:space:]]|$)|^[[:space:]]*axiom[[:space:]]|native_decide' \
  --glob '*.lean' .
```

The source scan is empty. The root module imports the complete publication
target and runs `#print axioms` on its principal declarations. The reported
dependencies are only the standard Lean/mathlib foundations `propext`,
`Classical.choice`, and `Quot.sound`. External mathematical inputs are theorem
parameters, so this audit verifies the conditional deductions rather than
pretending to prove those inputs.

For the declaration-level inventory, see [`formal/README.md`](formal/README.md).
