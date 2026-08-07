# Problem Summary

Given an unsorted array `arr[]` and an integer `k`, find the $k^{th}$ smallest element in the array. The optimal approach uses a **Max-Heap of size $k$**:
- Maintain a max-priority queue of size at most $k$.
- Iterate through `arr`, pushing each element into the heap.
- If heap size exceeds $k$, pop the top (largest) element.
- The root of the max-heap at the end is the $k^{th}$ smallest element.
This achieves $\mathcal{O}(N \log k)$ time and $\mathcal{O}(k)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to find the **$K^{th}$ smallest element** in an array/matrix/stream.
- Fixed-size heap pattern: Max-Heap for $K^{th}$ smallest, Min-Heap for $K^{th}$ largest.

---

## Important Clues

1. **"K-th smallest element"**: Use Max-Heap of size $k$.
2. **"Distinct elements / unsorted array"**: Priority queue streaming approach.

---

## Example

### Input
`arr = [7, 10, 4, 3, 20, 15]`, `k = 3`

### Visual Step-by-Step Progression

```text
Processing items: 7, 10, 4, 3, 20, 15

Max-Heap of size 3:
- Add 7:  [7]
- Add 10: [10, 7]
- Add 4:  [10, 7, 4]
- Add 3:  [10, 7, 4, 3] -> Pop 10 -> [7, 4, 3]
- Add 20: [20, 7, 4, 3] -> Pop 20 -> [7, 4, 3]
- Add 15: [15, 7, 4, 3] -> Pop 15 -> [7, 4, 3]

Root of Max-Heap = 7 (3rd smallest element!)
```

---

## Alternative Solutions

### 1. Full Sorting ($\mathcal{O}(N \log N)$ Time, $\mathcal{O}(1)$ Space)
- Sort array and return `arr[k - 1]`.

### 2. QuickSelect ($\mathcal{O}(N)$ Avg Time, $\mathcal{O}(1)$ Space)
- Partition array around pivot until pivot ends up at index `k - 1`.

---

## Edge Cases

1. **$k = 1$**: Minimum element in array.
2. **$k = N$**: Maximum element in array.
3. **Array already sorted**: Handled seamlessly by max-heap.

---

## Interview Tips

- **Dual Heap Memory Trick**:
  - **$K^{th}$ Largest** $\rightarrow$ **MIN-heap** of size $k$.
  - **$K^{th}$ Smallest** $\rightarrow$ **MAX-heap** of size $k$.
- Explain why the opposite heap type is used: "We want to discard elements that are too large, so we use a Max-Heap to easily pop the maximum."

---

## Similar Problems

1. [LeetCode #215: Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)
2. [LeetCode #378: Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/)
3. [LeetCode #973: K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/)

---

## Revision Notes

- Problem: Find $k^{th}$ smallest element in an array.
- Pattern: Max-Heap of size $k$.
- Key Logic: `maxHeap.push(num); if (maxHeap.size() > k) maxHeap.pop();`
- Result: `return maxHeap.top();`
- Optimal Complexity: Time $\mathcal{O}(N \log k)$, Space $\mathcal{O}(k)$.
