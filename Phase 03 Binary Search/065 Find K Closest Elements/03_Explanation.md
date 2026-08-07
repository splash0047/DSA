# Problem Summary

Given a sorted integer array `arr`, `k`, and `x`, return the `k` closest integers to `x` in sorted order. The optimal approach uses **Binary Search for Window Starting Index**. Since `arr` is pre-sorted, the $k$ closest elements form a contiguous subarray of length $k$. Searching range $[0, N - K]$, we compare `x - arr[mid]` vs `arr[mid + k] - x`. If `x - arr[mid] > arr[mid + k] - x`, we move right (`low = mid + 1`); otherwise `high = mid`. This finds the window in $\mathcal{O}(\log(N - K) + K)$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to find a **contiguous subarray window of fixed size $K$** centered around target $X$ in a pre-sorted array.
- Binary Search on Window Starting Index pattern.

---

## Important Clues

1. **"Sorted integer array"**: Contiguous $K$-element window property.
2. **"k closest integers to x"**: Fixed size window of length $k$.

---

## Example

### Input
`arr = [1, 2, 3, 4, 5]`, `k = 4`, `x = 3`

### Visual Step-by-Step Progression

```text
Possible 4-element contiguous windows:
Window A: [1, 2, 3, 4] (start=0, end=3, arr[0]=1, arr[4]=5)
          Distances from x=3: |1-3|=2, |5-3|=2 -> Tie breaker favors left!

Optimal Window: [1, 2, 3, 4]
```

---

## Alternative Solutions

### Two-Pointer Shrinking Window (O(N) Time, O(1) Space)
- `low = 0`, `high = N - 1`. While `high - low + 1 > k`, shrink the boundary pointer with larger distance $|arr[idx] - x|$.
- **Time Complexity**: $\mathcal{O}(N - K) = \mathcal{O}(N)$.
- **Space Complexity**: $\mathcal{O}(1)$.

---

## Edge Cases

1. **`x` Smaller Than All Elements**: `arr = [1, 2, 3, 4, 5]`, `x = -1` -> Window starts at index `0` $\rightarrow$ `[1, 2, 3, 4]`.
2. **`x` Larger Than All Elements**: `arr = [1, 2, 3, 4, 5]`, `x = 10` -> Window starts at index `N - K` $\rightarrow$ `[2, 3, 4, 5]`.
3. **`k == N`**: Immediately returns entire array `arr`.

---

## Interview Tips

- **Explain Why Distance Comparison Doesn't Need `abs()`**: State *"We write `x - arr[mid] > arr[mid + k] - x` instead of `abs()`. Because `arr[mid] <= arr[mid + k]`, when `x` is between `arr[mid]` and `arr[mid + k]`, both `x - arr[mid]` and `arr[mid + k] - x` are non-negative, naturally preserving tie-breaking rules!"*

---

## Similar Problems

1. [LeetCode #374: Guess Number Higher or Lower](https://leetcode.com/problems/guess-number-higher-or-lower/)
2. [LeetCode #4: Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)

---

## Revision Notes

- Problem: Find $k$ closest elements to $x$ in sorted array `arr`.
- Pattern: Binary Search for Window Start Index.
- `low = 0`, `high = N - k`.
- `while (low < high)`:
  - `mid = low + (high - low) / 2`.
  - `if (x - arr[mid] > arr[mid + k] - x) low = mid + 1`.
  - `else high = mid`.
- Return subarray from `low` to `low + k`.
- Optimal Complexity: Time $\mathcal{O}(\log(N - K) + K)$, Space $\mathcal{O}(1)$.
