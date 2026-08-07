# Problem Summary

Given an elevation map `height`, compute how much rain water can be trapped. The optimal approach uses a **Monotonic Decreasing Stack** storing indices:
1. When `height[i] > height[st.top()]`, pop `mid = st.top()`.
2. If `st.empty()`, break (spills left).
3. Record `left = st.top()`, `bounded_h = min(height[left], height[i]) - height[mid]`, `width = i - left - 1`.
4. Accumulate `water += bounded_h * width`.
This evaluates trapped water layer-by-layer in $\mathcal{O}(N)$ time and $\mathcal{O}(N)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to compute **trapped fluid / bounded container capacity** in a 1D terrain map.
- Monotonic Decreasing Stack Basin Fill pattern.

---

## Important Clues

1. **"Compute how much water it can trap after raining"**: Classic Trapping Water problem.
2. **"Linear O(N) time requirement"**: Monotonic Stack or Two Pointers.

---

## Example

### Input
`height = [0, 1, 0, 2, 1, 0, 1, 3]`

### Visual Step-by-Step Progression

```text
Elevation map:
      3
  2   |
1 |~| | (Water trapped in basin between heights 1 and 2 = 1 unit)
  |~|~| (Water trapped in lower basin = 5 units)
0 1 0 2 1 0 1 3

Total Trapped Water: 6 units
```

---

## Alternative Solutions

### Two Pointers Technique (O(N) Time, O(1) Space)
- Maintain `left = 0`, `right = N - 1`, `left_max = 0`, `right_max = 0`. Move pointer pointing to smaller boundary inward, accumulating `water += left_max - height[left]`.
- **Time Complexity**: $\mathcal{O}(N)$.
- **Space Complexity**: $\mathcal{O}(1)$.

---

## Edge Cases

1. **Monotonically Increasing / Decreasing**: `[1, 2, 3, 4]` or `[4, 3, 2, 1]` -> Traps `0` water.
2. **V-Shaped Elevation**: `[3, 0, 3]` -> Traps $3 \times 1 = 3$ units of water.
3. **Array Length $< 3$**: Cannot trap any water -> Returns `0`.

---

## Interview Tips

- **Compare Stack vs Two Pointers Approach**: State *"The Monotonic Stack calculates trapped water HORIZONTALLY layer-by-layer, whereas the Two Pointers approach calculates trapped water VERTICALLY column-by-column. Both operate in $\mathcal{O}(N)$ time, with Two Pointers optimizing auxiliary space to $\mathcal{O}(1)$."*

---

## Similar Problems

1. [LeetCode #11: Container With Most Water](https://leetcode.com/problems/container-with-most-water/)
2. [LeetCode #84: Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)
3. [LeetCode #407: Trapping Rain Water II](https://leetcode.com/problems/trapping-rain-water-ii/)

---

## Revision Notes

- Problem: Trapping Rain Water in elevation map.
- Pattern: Monotonic Decreasing Stack (`stack<int> st` of indices).
- Loop `i` from `0` to `N - 1`:
  - `while (!st.empty() && height[i] > height[st.top()])`:
    - `mid = st.top(); st.pop();`
    - `if (st.empty()) break;`
    - `left = st.top();`
    - `water += (min(height[left], height[i]) - height[mid]) * (i - left - 1);`
  - `st.push(i);`
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(N)$ (or $\mathcal{O}(1)$ with Two Pointers).
