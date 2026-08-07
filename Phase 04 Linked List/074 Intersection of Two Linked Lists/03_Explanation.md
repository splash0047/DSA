# Problem Summary

Given `headA` and `headB` of two singly linked lists, find and return the node where the two lists intersect, or `null` if no intersection exists. The optimal approach uses **Two Pointers Path Equivalence Switching** (`pA`, `pB`). When `pA` hits `nullptr`, redirect `pA = headB`; when `pB` hits `nullptr`, redirect `pB = headA`. Both pointers travel distance $(a + b + c)$, meeting at the intersection node (or `nullptr`) in $\mathcal{O}(M + N)$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to find the **intersection point / merge point** of two linked lists without modifying the list structure.
- Two Pointers Path Equivalence Switching pattern.

---

## Important Clues

1. **"Find node at which two lists intersect"**: Intersection point detection.
2. **"O(m + n) time and O(1) memory"**: Mandatory 2-pointer path length alignment.

---

## Example

### Input
`listA = [4 -> 1 -> 8 -> 4 -> 5]`, `listB = [5 -> 6 -> 1 -> 8 -> 4 -> 5]`

### Visual Step-by-Step Progression

```text
List A: 4 -> 1 -\ 
                 8 -> 4 -> 5
List B: 5 -> 6 -> 1 -/

pA path: 4 -> 1 -> 8 -> 4 -> 5 -> [Switch to B] -> 5 -> 6 -> 1 -> 8
pB path: 5 -> 6 -> 1 -> 8 -> 4 -> 5 -> [Switch to A] -> 4 -> 1 -> 8

Both land on Node 8 simultaneously!
```

---

## Alternative Solutions

### Length Difference Alignment (O(M + N) Time, O(1) Space)
- Calculate lengths $LenA$ and $LenB$. Advance the pointer of the longer list by $|LenA - LenB|$ steps, then move both pointers 1 step at a time until they meet.
- **Time Complexity**: $\mathcal{O}(M + N)$.
- **Space Complexity**: $\mathcal{O}(1)$.

---

## Edge Cases

1. **No Intersection**: Both pointers complete $M + N$ steps and evaluate `pA == pB == nullptr` simultaneously.
2. **Identical Lists** (`headA == headB`): Loop terminates immediately at iteration 0, returning `headA`.
3. **One List Null**: Returns `nullptr`.

---

## Interview Tips

- **Explain Why Switch Happens on `pA == nullptr`**: State *"We redirect `pA` to `headB` when `pA == nullptr` (rather than `pA->next == nullptr`). This allows `pA` and `pB` to naturally hit `nullptr` together in non-intersecting cases, avoiding infinite loops."*

---

## Similar Problems

1. [LeetCode #142: Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)
2. [LeetCode #1650: Lowest Common Ancestor of a Binary Tree III](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/)

---

## Revision Notes

- Problem: Intersection node of two linked lists in $\mathcal{O}(1)$ space.
- Pattern: Two Pointers (`pA = headA`, `pB = headB`).
- `while (pA != pB)`:
  - `pA = (pA == nullptr) ? headB : pA->next`.
  - `pB = (pB == nullptr) ? headA : pB->next`.
- Return `pA`.
- Optimal Complexity: Time $\mathcal{O}(M + N)$, Space $\mathcal{O}(1)$.
