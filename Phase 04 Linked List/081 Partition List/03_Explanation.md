# Problem Summary

Given the `head` of a linked list and `x`, partition the list such that nodes $< x$ come before nodes $\ge x$, while **preserving relative node order**. The optimal approach uses **Two Dummy Sentinel Lists** (`less_dummy`, `greater_dummy`). As we traverse `head`, nodes are attached to the tail of `less_dummy` or `greater_dummy`. Setting `greater_tail->next = nullptr` prevents cycles, and stitching `less_tail->next = greater_dummy.next` partitions the list in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to **partition a linked list into two categories** while maintaining relative ordering (e.g. odd/even index split, positive/negative split).
- Two Dummy Sentinel Lists pattern.

---

## Important Clues

1. **"Partition such that nodes < x come before nodes >= x"**: Two-way split.
2. **"Preserve original relative order"**: Stable partitioning constraint.

---

## Example

### Input
`head = [1 -> 4 -> 3 -> 2 -> 5 -> 2]`, `x = 3`

### Visual Step-by-Step Progression

```text
Traverse and partition into 2 lists:
Less (< 3):    dummyL -> [1] -> [2] -> [2]
Greater (>= 3): dummyG -> [4] -> [3] -> [5] -> nullptr

Stitch together:
dummyL -> [1] -> [2] -> [2] -> [4] -> [3] -> [5] -> nullptr

Result: [1 -> 2 -> 2 -> 4 -> 3 -> 5]
```

---

## Alternative Solutions

### Vector Array Extraction (O(N) Time, O(N) Space)
- Separate values into `less_vals` and `greater_vals` vectors, then overwrite node values.
- **Time Complexity**: $\mathcal{O}(N)$.
- **Space Complexity**: $\mathcal{O}(N)$.

---

## Edge Cases

1. **All Nodes $< x$**: `greater_dummy.next == nullptr` $\implies$ `less_tail` attaches `nullptr`.
2. **All Nodes $\ge x$**: `less_dummy.next == nullptr` $\implies$ Returns `greater_dummy.next`.
3. **Empty List**: Returns `nullptr`.

---

## Interview Tips

- **Explain Cycle Prevention**: State *"Setting `greater_tail->next = nullptr` before joining `less` and `greater` partitions is mandatory to prevent cyclic pointer loops when the original tail node belongs to the `less` partition."*

---

## Similar Problems

1. [LeetCode #328: Odd Even Linked List](https://leetcode.com/problems/odd-even-linked-list/)
2. [LeetCode #86: Partition List](https://leetcode.com/problems/partition-list/)
3. [LeetCode #21: Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)

---

## Revision Notes

- Problem: Partition linked list around value $x$ preserving relative order in $\mathcal{O}(1)$ space.
- Pattern: Two Dummy Sentinel Lists (`less_dummy`, `greater_dummy`).
- Traverse `head`:
  - `if (curr->val < x) less_tail->next = curr, less_tail = less_tail->next`.
  - `else greater_tail->next = curr, greater_tail = greater_tail->next`.
- `greater_tail->next = nullptr` (Prevent cycle!).
- `less_tail->next = greater_dummy.next` (Stitch partitions).
- Return `less_dummy.next`.
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(1)$.
