# Problem Summary

Merge $k$ sorted linked-lists into one sorted linked-list and return it. The optimal approach uses a **Min-Heap (K-Way Merge)**:
- Push non-null head nodes of all $k$ lists into a Min-Heap.
- While heap is not empty:
  - Extract the node with minimum value `curr`.
  - Append `curr` to the merged list.
  - If `curr->next != nullptr`, push `curr->next` into the Min-Heap.
This merges all nodes in $\mathcal{O}(N \log k)$ time and $\mathcal{O}(k)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to **merge $K$ sorted streams / lists / arrays**.
- K-Way Merge with Min-Heap pattern.

---

## Important Clues

1. **"Merge k sorted linked lists"**: K-Way merge using Min-Heap.
2. **"Each list is individually sorted"**: Head node of each list holds smallest unmerged element of that list.

---

## Example

### Input
`lists = [[1->4->5], [1->3->4], [2->6]]`

### Visual Step-by-Step Progression

```text
Heap (Size k=3 Min-Heap):
Initial: [1(L1), 1(L2), 2(L3)]

Step 1: Pop 1(L1) -> Linked: 1 -> Push 4(L1) -> Heap: [1(L2), 2(L3), 4(L1)]
Step 2: Pop 1(L2) -> Linked: 1->1 -> Push 3(L2) -> Heap: [2(L3), 3(L2), 4(L1)]
Step 3: Pop 2(L3) -> Linked: 1->1->2 -> Push 6(L3) -> Heap: [3(L2), 4(L1), 6(L3)]
...

Result: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6
```

---

## Alternative Solutions

### 1. Divide and Conquer Merge Sort ($\mathcal{O}(N \log k)$ Time, $\mathcal{O}(\log k)$ Space)
- Pairwise merge lists using standard 2-list merge helper recursively.

### 2. Extract All & Sort ($\mathcal{O}(N \log N)$ Time, $\mathcal{O}(N)$ Space)
- Dump all values into array, sort, and construct new list.

---

## Edge Cases

1. **Empty input**: `lists = []` $\implies$ returns `nullptr`.
2. **Lists with empty sublists**: `lists = [[], [1->2], []]` $\implies$ null checks prevent crashing.
3. **Single list**: `lists = [[1->2->3]]` $\implies$ returns same list.

---

## Interview Tips

- **Explain In-Place Re-linking**: State *"Instead of allocating new node instances, we re-link the existing `ListNode*` pointers directly in $\mathcal{O}(k)$ space."*
- Compare with **Divide-and-Conquer**: "Both Min-Heap and Divide-and-Conquer achieve optimal $\mathcal{O}(N \log k)$ time."

---

## Similar Problems

1. [LeetCode #21: Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)
2. [LeetCode #378: Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/)
3. [LeetCode #632: Smallest Range Covering Elements from K Lists](https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/)

---

## Revision Notes

- Problem: Merge $k$ sorted linked lists into one.
- Pattern: Min-Heap of size $k$ holding list head pointers.
- Key Loop: `curr = minHeap.top(); minHeap.pop(); tail->next = curr; if (curr->next) minHeap.push(curr->next);`
- Optimal Complexity: Time $\mathcal{O}(N \log k)$, Space $\mathcal{O}(k)$.
