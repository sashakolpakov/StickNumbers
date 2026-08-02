# LinkedIn announcement

🪢 WE TURNED STICK KNOTS INTO A REAL-ALGEBRAIC COUNTING PROBLEM.

How many genuinely different knots can be built from at most $N$ straight
sticks?

The answer lives on the factorial scale:

**N^((2/3 + o(1))N) ≤ K(N) ≤ N^(3N + o(N)).**

The mechanism is the fun part. An $N$-stick polygon is a point in a
$3N$-dimensional configuration space. Its knot type can change only when two
sticks collide—and those collision walls are sparse cubic and quartic
polynomials.

So the problem becomes:

**knot topology → determinant walls → algebraic chambers → counting**

The classical crossing-diagram route gives only $\exp(O(N^2))$. A recent
strong-geometry reconstruction theorem already implies the factorial scale;
the signs used in that proof give an upper bound $N^{6N+o(N)}$. The direct
discriminant count sharpens it to $N^{3N+o(N)}$. On the other side, an explicit
Garside-braid construction produces $N^{(2/3+o(1))N}$ prime satellite knots.

This is not a tiny coefficient massage. It is a direct bridge between knot
topology, real algebraic geometry, fewnomials, and permutation combinatorics.

The proof graph also has a Lean certificate: actual polygon spaces,
multivariate walls, path components, permutation words, endpoint fibers, and
the final deductions on supplied braid and knot interfaces are kernel checked.
The deep cited inputs—ambient
isotopy, Barone--Basu, Garside theory, Malyutin--Stupakov, and Huh--Oh—are
explicitly marked as external.

Joint work with Igor Rivin. Manuscript, Lean, reproducibility files, and the
novelty audit:

🪢 https://github.com/sashakolpakov/StickNumbers

#KnotTheory #AlgebraicGeometry #Fewnomials #Lean4 #FormalMethods
