# Problem Summary

Design a data structure that supports adding numbers from a data stream and returning the median of all elements seen so far in real time. The optimal approach uses **Two Heaps (Max-Heap + Min-Heap Balancing)**:
- `maxHeap` stores the lower half of numbers (top is max of lower half).
- `minHeap` stores the upper half of numbers (top is min of upper half).
- Keep `maxHeap.size() == minHeap.size()` or `maxHeap.size() == minHeap.size() + 1`.
- `addNum` runs in $\mathcal{O}(\log N)$ time, and `findMedian` runs in $\mathcal{O}(1)$ time.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need **continuous median tracking** in a dynamic data stream.
- You need to partition data into lower and upper halves dynamically.
- Two Heaps balancing pattern.

---

## Important Clues

1. **"Find median from data stream"**: Canonical two heap problem.
2. **"Dynamic additions with fast median queries"**: $\mathcal{O}(\log N)$ add, $\mathcal{O}(1)$ query requirement.

---

## Example

### Input
`add(1)`, `add(2)`, `findMedian()`, `add(3)`, `findMedian()`

### Visual Step-by-Step Progression

```text
Lower Half (Max-Heap)  |  Upper Half (Min-Heap)
-----------------------|-----------------------
Add 1:  [1]            |  []          -> Median = 1.0
Add 2:  [1]            |  [2]         -> Median = (1+2)/2 = 1.5
Add 3:  [2, 1]         |  [3]         -> Median = 2.0 (maxHeap top)
```

---

## Alternative Solutions

### 1. Vector Insertion Sort ($\mathcal{O}(N)$ Add, $\mathcal{O}(1)$ Median, $\mathcal{O}(N)$ Space)
- Maintain sorted vector with `std::lower_bound` and `vector::insert`.

### 2. Self-Balancing BST (`std::multiset` with Iterator) ($\mathcal{O}(\log N)$ Add, $\mathcal{O}(1)$ Median)
- Maintain pointer iterator to median element.

---

## Edge Cases

1. **Even number of elements**: Median is average of `maxHeap.top()` and `minHeap.top()`.
2. **Odd number of elements**: Median is `maxHeap.top()`.
3. **Duplicate values**: Handled correctly by priority queues.

---

## Interview Tips

- **Explain Heap Invariant**: State *"We divide elements into lower half (Max-Heap) and upper half (Min-Heap). Maintaining `maxHeap.top() <= minHeap.top()` and size difference $\le 1$ allows us to extract the median in $\mathcal{O}(1)$ time."*

---

## Similar Problems

1. [LeetCode #480: Sliding Window Median](https://leetcode.com/problems/sliding-window-median/)
2. [LeetCode #1825: Finding MK Average](https://leetcode.com/problems/finding-mk-average/)
3. [LeetCode #703: Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/)

---

## Revision Notes

- Problem: Dynamic median tracking from stream.
- Pattern: Two Heaps (`maxHeap` for lower half, `minHeap` for upper half).
- Invariants: `maxHeap.top() <= minHeap.top()`, `maxHeap.size() == minHeap.size() (+1)`.
- `addNum`: $\mathcal{O}(\log N)$. `findMedian`: $\mathcal{O}(1)$.
- Optimal Complexity: Time $\mathcal{O}(\log N)$ per add, Space $\mathcal{O}(N)$.
