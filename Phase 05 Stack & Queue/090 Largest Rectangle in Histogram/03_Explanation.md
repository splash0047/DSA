# Problem Summary

Given an array `heights` representing a histogram where each bar has width `1`, return the area of the largest rectangle in the histogram. The optimal approach uses a **Monotonic Increasing Stack** storing indices. For each bar `i` (up to `i = N` with virtual height `0`), while `heights[i] < heights[st.top()]`, pop `h = heights[st.top()]`. The current index `i` is the right smaller boundary, and the new `st.top()` is the left smaller boundary, giving `width = st.empty() ? i : (i - st.top() - 1)`. This calculates maximum area in $\mathcal{O}(N)$ time and $\mathcal{O}(N)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to find the **largest rectangle / area bounded by contiguous heights**.
- Monotonic Increasing Stack Boundary Resolution pattern.

---

## Important Clues

1. **"Largest rectangle in histogram"**: Classic Monotonic Stack problem.
2. **"Linear O(N) time requirement"**: Simultaneous Previous Smaller & Next Smaller boundary resolution.

---

## Example

### Input
`heights = [2, 1, 5, 6, 2, 3]`

### Visual Step-by-Step Progression

```text
Histogram bars:
      6
    5 |
    | |   3
2   | | 2 |
| 1 | | | |
0 1 2 3 4 5

At i = 4 (bar height 2):
- Pop bar 3 (height 6): width = 4-2-1 = 1 -> area = 6*1 = 6
- Pop bar 2 (height 5): width = 4-1-1 = 2 -> area = 5*2 = 10 (MAX!)

Largest Rectangle Area: 10
```

---

## Alternative Solutions

### Previous & Next Smaller Arrays (O(N) Time, O(N) Space)
- Precompute `prev_smaller[N]` and `next_smaller[N]` arrays using two separate monotonic stack passes, then evaluate `area[i] = heights[i] * (next_smaller[i] - prev_smaller[i] - 1)`.
- **Time Complexity**: $\mathcal{O}(N)$.
- **Space Complexity**: $\mathcal{O}(N)$.

---

## Edge Cases

1. **Monotonically Increasing Heights**: `[1, 2, 3, 4]` -> Flushed at virtual index `i = N`.
2. **All Identical Heights**: `[5, 5, 5, 5]` -> Returns $5 \times 4 = 20$.
3. **Single Element Histogram**: `[7]` -> Returns `7`.

---

## Interview Tips

- **Explain Why `w = st.empty() ? i : (i - st.top() - 1)` Works**: State *"If `st.empty()` is true after popping height `h`, it means height `h` is the smallest element seen so far from index `0` up to `i - 1`. Therefore, its valid rectangle width spans the ENTIRE distance `i` from index `0` to `i - 1`."*

---

## Similar Problems

1. [LeetCode #85: Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/)
2. [LeetCode #42: Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)
3. [LeetCode #901: Online Stock Span](https://leetcode.com/problems/online-stock-span/)

---

## Revision Notes

- Problem: Maximum rectangle area in histogram.
- Pattern: Monotonic Increasing Stack (`stack<int> st` of indices).
- Loop `i` from `0` to `N` (virtual height `0` at `i = N`):
  - `while (!st.empty() && curr_h < heights[st.top()])`:
    - `h = heights[st.top()]; st.pop();`
    - `w = st.empty() ? i : (i - st.top() - 1);`
    - `max_area = max(max_area, h * w);`
  - `st.push(i);`
- Return `max_area`.
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(N)$.
