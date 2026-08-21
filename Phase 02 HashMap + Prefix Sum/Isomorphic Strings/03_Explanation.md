# Isomorphic Strings - Deep Explanation

## Core Concept: Bijection (1-to-1 and Onto)
A valid isomorphism requires:
1. Every character in $S$ maps to exactly one character in $T$.
2. No two distinct characters in $S$ map to the same character in $T$.
Using the last-seen index array automatically verifies both directions of the bijection in $\mathcal{O}(1)$ space!
