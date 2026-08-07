# Problem Summary

Given the `head` of a singly linked list $L_0 \rightarrow L_1 \rightarrow \dots \rightarrow L_n$, reorder it in-place to $L_0 \rightarrow L_n \rightarrow L_1 \rightarrow L_{n-1} \rightarrow \dots$. The optimal approach combines three modular steps:
1. **Find Midpoint** using Fast & Slow pointers (`slow`, `fast`).
2. **Reverse Second Half** starting from `slow->next` and disconnect `slow->next = nullptr`.
3. **Interleave Merge** the first half and reversed second half alternately in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to **reorder or interleave** nodes from opposite ends of a linked list.
- 3-Phase Linked List Pattern: Find Mid + Reverse Half + Merge.

---

## Important Clues

1. **"Reorder list to L0 -> Ln -> L1 -> Ln-1"**: Interleaved head/tail merge pattern.
2. **"Do not modify values"**: In-place pointer manipulation constraint.

---

## Example

### Input
`head = [1 -> 2 -> 3 -> 4 -> 5]`

### Visual Step-by-Step Progression

```text
Step 1 (Find Mid & Split):
First Half:   [ 1  ->  2  ->  3 ] -> nullptr
Second Half:  [ 4  ->  5 ] -> nullptr

Step 2 (Reverse Second Half):
Reversed:     [ 5  ->  4 ] -> nullptr

Step 3 (Interleave Merge):
Stitch 1 -> 5 -> 2 -> 4 -> 3

Result: [1 -> 5 -> 2 -> 4 -> 3]
```

---

## Alternative Solutions

### Vector Pointer Storage (O(N) Time, O(N) Space)
- Store node pointers in `vector<ListNode*>`. Use `left` and `right` pointers to interleave.
- **Time Complexity**: $\mathcal{O}(N)$.
- **Space Complexity**: $\mathcal{O}(N)$.

---

## Edge Cases

1. **Length 1 or 2**: `head = [1]` or `[1 -> 2]` -> No reordering needed, returns immediately.
2. **Even Length List**: `head = [1 -> 2 -> 3 -> 4]` -> Reorders cleanly to `[1 -> 4 -> 2 -> 3]`.
3. **Odd Length List**: Middle node remains as the tail of the first half.

---

## Interview Tips

- **Highlight Modular 3-Step Strategy**: State *"Reordering a linked list in $\mathcal{O}(1)$ space breaks down into three classic sub-problems: finding the midpoint using Fast/Slow pointers, reversing the second half, and zip-merging the two sub-lists."*

---

## Similar Problems

1. [LeetCode #234: Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)
2. [LeetCode #206: Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)
3. [LeetCode #21: Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)

---

## Revision Notes

- Problem: Reorder linked list to $L_0 \rightarrow L_n \rightarrow L_1 \rightarrow L_{n-1} \dots$ in $\mathcal{O}(1)$ space.
- Strategy: 3-Step Modular Algorithm:
  1. Midpoint: `fast` & `slow` pointers.
  2. Reverse: `prev = nullptr`, reverse `slow->next`, set `slow->next = nullptr`.
  3. Interleave: `while (second)` stitch `first->next = second; second->next = tmp1;`.
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(1)$.
