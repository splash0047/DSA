# Problem Summary

Given an array of `k` sorted linked lists, merge all of them into a single sorted linked list. The optimal approach uses a **Min-Heap (Priority Queue)** of size at most $K$. Initialized with the head nodes of all non-empty lists, we repeatedly pop the minimum node `min_node`, attach it to `tail->next`, and push `min_node->next` into the heap. This completes the $K$-way merge in $\mathcal{O}(N \log K)$ time and $\mathcal{O}(K)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to **merge $K$ sorted streams / lists / arrays** into a single sorted stream.
- Min-Heap $K$-Way Merge pattern.

---

## Important Clues

1. **"Merge k sorted linked-lists"**: $K$-way merge.
2. **"Optimal runtime O(N log K)"**: Min-Heap or Divide & Conquer requirement.

---

## Example

### Input
`lists = [[1->4->5], [1->3->4], [2->6]]`

### Visual Step-by-Step Progression

```text
Min-Heap (Size 3):
Top: Node 1 (L1) -> Attach to merged list -> Push Node 4 (L1)
Top: Node 1 (L2) -> Attach to merged list -> Push Node 3 (L2)
Top: Node 2 (L3) -> Attach to merged list -> Push Node 6 (L3)
Top: Node 3 (L2) -> Attach to merged list -> Push Node 4 (L2)
...

Merged List: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6
```

---

## Alternative Solutions

### Divide and Conquer Pairwise Merging (O(N log K) Time, O(log K) Space)
- Pairwise merge adjacent lists (`lists[0]` with `lists[1]`, `lists[2]` with `lists[3]`, etc.) repeatedly in $\log K$ passes.
- **Time Complexity**: $\mathcal{O}(N \log K)$.
- **Space Complexity**: $\mathcal{O}(\log K)$ recursion stack (or $\mathcal{O}(1)$ iterative).

---

## Edge Cases

1. **Empty Input**: `lists = []` -> Returns `nullptr`.
2. **All Lists Empty**: `lists = [[], [], []]` -> Returns `nullptr`.
3. **Single List**: `lists = [[1, 2, 3]]` -> Returns `[1, 2, 3]`.

---

## Interview Tips

- **Compare Min-Heap vs Divide & Conquer**: State *"Both Min-Heap and Divide & Conquer approaches achieve the optimal $\mathcal{O}(N \log K)$ time. Min-Heap is ideal for online streaming inputs where lists arrive dynamically, while Divide & Conquer achieves $\mathcal{O}(1)$ auxiliary space when implemented iteratively."*

---

## Similar Problems

1. [LeetCode #21: Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)
2. [LeetCode #378: Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/)
3. [LeetCode #264: Ugly Number II](https://leetcode.com/problems/ugly-number-ii/)

---

## Revision Notes

- Problem: Merge $k$ sorted linked lists.
- Pattern: Min-Heap (`std::priority_queue<ListNode*, vector<ListNode*>, Compare>`).
- Custom Comparator: `struct Compare { bool operator()(a, b) { return a->val > b->val; } };`.
- Push initial non-null heads.
- `while (!pq.empty())`:
  - `min_node = pq.top(); pq.pop();`
  - `tail->next = min_node; tail = tail->next;`
  - `if (min_node->next) pq.push(min_node->next);`
- Optimal Complexity: Time $\mathcal{O}(N \log K)$, Space $\mathcal{O}(K)$.
