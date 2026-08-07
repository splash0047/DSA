# Problem Summary

Given `nums1` (subset of `nums2`), find the Next Greater Element in `nums2` for each value in `nums1`. The optimal approach uses a **Monotonic Decreasing Stack + Hash Map**:
1. Iterate through `nums2`. Maintain a stack of unresolved numbers.
2. When `num > st.top()`, pop `st.top()` and record `next_greater[st.top()] = num`.
3. Set `next_greater[val] = -1` for remaining stack values.
4. Query `next_greater[x]` for each `x` in `nums1` in $\mathcal{O}(1)$ time.
This completes in $\mathcal{O}(N_1 + N_2)$ time and $\mathcal{O}(N_2)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to find **Next Greater Element for a subset of queries** from a pre-defined array.
- Monotonic Stack + Hash Map Lookup pattern.

---

## Important Clues

1. **"Next greater element in nums2 for elements in nums1"**: NGE pattern.
2. **"O(N1 + N2) follow-up time constraint"**: Monotonic stack precomputation.

---

## Example

### Input
`nums1 = [4, 1, 2]`, `nums2 = [1, 3, 4, 2]`

### Visual Step-by-Step Progression

```text
Precompute NGE for nums2 = [1, 3, 4, 2]:
1 < 3 -> NGE[1] = 3
3 < 4 -> NGE[3] = 4
4 (no greater) -> NGE[4] = -1
2 (no greater) -> NGE[2] = -1

Query map for nums1 = [4, 1, 2]:
NGE[4] = -1
NGE[1] = 3
NGE[2] = -1

Result: [-1, 3, -1]
```

---

## Alternative Solutions

### Nested Linear Search (Brute Force)
- For each `x` in `nums1`, find `x` in `nums2` and scan right for first greater element.
- **Time Complexity**: $\mathcal{O}(N_1 \times N_2)$.
- **Space Complexity**: $\mathcal{O}(1)$.

---

## Edge Cases

1. **Strictly Decreasing `nums2`**: `nums2 = [4, 3, 2, 1]` -> All queries return `-1`.
2. **Strictly Increasing `nums2`**: `nums2 = [1, 2, 3, 4]` -> Each element's NGE is its immediate right neighbor.
3. **Single Element Arrays**: Handled smoothly.

---

## Interview Tips

- **Explain Why Hash Map Precomputation Optimizes Subset Queries**: State *"Because `nums1` is a subset of `nums2`, precomputing Next Greater Elements for all numbers in `nums2` ONCE using a Monotonic Stack ($\mathcal{O}(N_2)$ time) allows us to answer all $N_1$ queries in $\mathcal{O}(1)$ time per query, avoiding redundant scans."*

---

## Similar Problems

1. [LeetCode #503: Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/)
2. [LeetCode #739: Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)
3. [LeetCode #556: Next Greater Element III](https://leetcode.com/problems/next-greater-element-iii/)

---

## Revision Notes

- Problem: Next Greater Element for `nums1` in `nums2`.
- Pattern: Monotonic Stack + `unordered_map<int, int> next_greater`.
- Traverse `num` in `nums2`:
  - `while (!st.empty() && num > st.top()) next_greater[st.top()] = num, st.pop()`.
  - `st.push(num)`.
- Leftover `st` elements set to `-1`.
- Query map for `nums1` elements.
- Optimal Complexity: Time $\mathcal{O}(N_1 + N_2)$, Space $\mathcal{O}(N_2)$.
