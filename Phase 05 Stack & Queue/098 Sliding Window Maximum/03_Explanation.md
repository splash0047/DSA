# Problem Summary

Given an array `nums` and a sliding window of size `k`, find the maximum element in each window as it slides from left to right. The optimal approach uses a **Monotonic Decreasing Deque (`std::deque<int> dq`)** storing indices:
1. Evict expired out-of-window indices from the front (`dq.front() == i - k`).
2. Maintain monotonic decreasing property by popping smaller elements from the back (`nums[i] >= nums[dq.back()]`).
3. Push index `i` to back.
4. When $i \ge k - 1$, record `ans.push_back(nums[dq.front()])`.
This computes sliding window maximums in $\mathcal{O}(N)$ time and $\mathcal{O}(K)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to find the **maximum or minimum in a sliding window of fixed size $K$**.
- Monotonic Decreasing Deque pattern.

---

## Important Clues

1. **"Sliding window of size k"**: Fixed-width moving window.
2. **"Find maximum in each window in O(N) time"**: Monotonic Deque application.

---

## Example

### Input
`nums = [1, 3, -1, -3, 5, 3, 6, 7]`, `k = 3`

### Visual Step-by-Step Progression

```text
Window 1: [1, 3, -1] -> Max = 3
Window 2: [3, -1, -3] -> Max = 3
Window 3: [-1, -3, 5] -> Max = 5
Window 4: [-3, 5, 3]  -> Max = 5
Window 5: [5, 3, 6]   -> Max = 6
Window 6: [3, 6, 7]   -> Max = 7

Result: [3, 3, 5, 5, 6, 7]
```

---

## Alternative Solutions

### Max-Heap Priority Queue (O(N log N) Time, O(N) Space)
- Maintain `std::priority_queue<pair<int, int>> pq` of `{value, index}`. Evict lazy elements when `pq.top().second <= i - k`.
- **Time Complexity**: $\mathcal{O}(N \log N)$.
- **Space Complexity**: $\mathcal{O}(N)$.

---

## Edge Cases

1. **Window Size $K = 1$**: Output is identical to input array `nums`.
2. **Window Size $K = N$**: Single window, output contains overall maximum element.
3. **Strictly Decreasing Array**: `[5, 4, 3, 2, 1]`, `k = 3` -> Output `[5, 4, 3]`.

---

## Interview Tips

- **Explain Why Deque Stores Indices**: State *"We store index `i` in the deque rather than value `nums[i]` because index information is mandatory to identify when a candidate maximum has expired and fallen out of the sliding window (`dq.front() <= i - k`)."*

---

## Similar Problems

1. [LeetCode #155: Min Stack](https://leetcode.com/problems/min-stack/)
2. [LeetCode #1425: Constrained Subsequence Sum](https://leetcode.com/problems/constrained-subsequence-sum/)
3. [LeetCode #1438: Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/)

---

## Revision Notes

- Problem: Maximum in sliding window of size $k$.
- Pattern: Monotonic Decreasing Deque (`std::deque<int> dq` of indices).
- Loop `i` from `0` to `N - 1`:
  - `if (!dq.empty() && dq.front() == i - k) dq.pop_front();`
  - `while (!dq.empty() && nums[i] >= nums[dq.back()]) dq.pop_back();`
  - `dq.push_back(i);`
  - `if (i >= k - 1) ans.push_back(nums[dq.front()]);`
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(K)$.
