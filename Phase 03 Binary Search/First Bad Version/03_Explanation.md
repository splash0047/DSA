# First Bad Version - Deep Explanation

## Monotonicity & `left + (right - left) / 2`
Using `mid = left + (right - left) / 2` prevents 32-bit integer overflow when $n = 2^{31} - 1$.
The predicate `isBadVersion` is monotonically non-decreasing, ensuring binary search correctness.
