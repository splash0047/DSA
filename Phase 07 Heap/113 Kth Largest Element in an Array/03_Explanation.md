# Problem Summary

Given an integer array `nums` and an integer `k`, return the $k^{th}$ largest element in the array. The optimal approach uses a **Min-Heap of size $k$**:
- Maintain a min-priority queue of size at most $k$.
- Iterate through `nums`, pushing each element into the heap.
- If heap size exceeds $k$, pop the top element.
- The root of the min-heap at the end is the $k^{th}$ largest element.
This achieves $\mathcal{O}(N \log k)$ time complexity and $\mathcal{O}(k)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to find the **$K^{th}$ largest / smallest** element in an unsorted collection.
- You need the **Top K** elements from a large stream/array.
- Min-Heap / Max-Heap pattern or QuickSelect algorithm.

---

## Important Clues

1. **"K-th largest element"**: Top K pattern $\implies$ Use Min-Heap of size $k$.
2. **"Solve without sorting"**: Standard $\mathcal{O}(N \log N)$ sort is forbidden; use Heap $\mathcal{O}(N \log k)$ or QuickSelect $\mathcal{O}(N)$.

---

## Example

### Input
`nums = [3, 2, 1, 5, 6, 4]`, `k = 2`

### Visual Step-by-Step Progression

```text
Iterate elements: 3, 2, 1, 5, 6, 4

Heap (Size 2 Min-Heap):
- Add 3: [3]
- Add 2: [2, 3]
- Add 1: [1, 2, 3] -> Pop 1 -> [2, 3]
- Add 5: [2, 3, 5] -> Pop 2 -> [3, 5]
- Add 6: [3, 5, 6] -> Pop 3 -> [5, 6]
- Add 4: [4, 5, 6] -> Pop 4 -> [5, 6]

Top of Min-Heap = 5 (2nd largest element!)
```

---

## Alternative Solutions

### 1. Full Sorting ($\mathcal{O}(N \log N)$ Time, $\mathcal{O}(1)$ Space)
- Sort `nums` and return `nums[n - k]`.

### 2. Max-Heap of Size $N$ ($\mathcal{O}(N + k \log N)$ Time, $\mathcal{O}(N)$ Space)
- Build max-heap from all elements, then call `pop()` $k - 1$ times.

### 3. QuickSelect ($\mathcal{O}(N)$ Avg Time, $\mathcal{O}(1)$ Space)
- Divide-and-conquer partition strategy.

---

## Edge Cases

1. **$k = 1$**: Return maximum element (`std::max_element`).
2. **$k = N$**: Return minimum element (`std::min_element`).
3. **Duplicate Elements**: e.g., `nums = [2, 2, 2], k = 2` -> Correctly returns `2`.
4. **Negative Numbers**: Handled naturally by comparisons.

---

## Interview Tips

- **Explain Min-Heap vs Max-Heap Choice**: State *"For $K^{th}$ LARGEST, use a MIN-heap of size $k$ so the smallest element among the top $k$ is easily evicted, leaving the $k^{th}$ largest at the top."*
- Mention **QuickSelect** for bonus points if the interviewer asks for $\mathcal{O}(N)$ average time complexity without extra space.

---

## Similar Problems

1. [LeetCode #347: Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)
2. [LeetCode #973: K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/)
3. [LeetCode #703: Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/)
4. [LeetCode #692: Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/)
5. [LeetCode #378: Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/)

---

## Revision Notes

- Problem: Find $k^{th}$ largest element in an unsorted array.
- Pattern: Min-Heap of size $k$.
- Key Logic: `minHeap.push(num); if (minHeap.size() > k) minHeap.pop();`
- Result: `return minHeap.top();`
- Optimal Complexity: Time $\mathcal{O}(N \log k)$, Space $\mathcal{O}(k)$.
