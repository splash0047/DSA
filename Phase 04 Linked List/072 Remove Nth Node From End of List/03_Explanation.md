# Problem Summary

Given the `head` of a linked list and `n`, remove the $n^{\text{th}}$ node from the end in a single pass. The optimal approach uses **Two-Pointer Fixed Gap (Fast & Slow)** with a `dummy` node. We advance `fast` pointer $n + 1$ steps ahead of `slow`. Sliding both pointers forward until `fast == nullptr` positions `slow` at the node immediately before the target, allowing deletion in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to find or remove the **$N^{\text{th}}$ node from the end** of a linked list in a single pass.
- Fast & Slow Pointer with Fixed Gap ($N+1$) pattern.

---

## Important Clues

1. **"N-th node from end"**: Fixed gap two-pointer pattern.
2. **"Single pass follow-up"**: Simultaneous traversal using gap $N+1$.

---

## Example

### Input
`head = [1 -> 2 -> 3 -> 4 -> 5]`, `n = 2`

### Visual Step-by-Step Progression

```text
Dummy -> [ 1  ->  2  ->  3  ->  4  ->  5 ]
   S               F  (Gap of n+1 = 3 steps)

Slide both until F reaches nullptr:
Dummy -> [ 1  ->  2  ->  3  ->  4  ->  5 ] -> nullptr
                         S               F

Delete S->next (Node 4): 3->next = 5

Result: [1 -> 2 -> 3 -> 5]
```

---

## Alternative Solutions

### Two-Pass Length Counter (O(N) Time, O(1) Space)
- Pass 1 counts total length $SZ$. Pass 2 traverses $SZ - n - 1$ steps to delete node.
- **Time Complexity**: $\mathcal{O}(N)$ (Two passes).
- **Space Complexity**: $\mathcal{O}(1)$.

---

## Edge Cases

1. **Delete Head Node ($n == SZ$)**: `dummy` node ensures `slow` stays at `dummy` and `dummy.next` updates smoothly.
2. **Single Element List ($n = 1, SZ = 1$)**: Returns `nullptr`.
3. **Delete Tail Node ($n = 1$)**: Removes last element.

---

## Interview Tips

- **Explain Dummy Node Sentinel Utility**: State *"Using `ListNode dummy(0, head)` handles deleting the head node seamlessly without needing separate conditional `if (n == length)` checks."*

---

## Similar Problems

1. [LeetCode #876: Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)
2. [LeetCode #61: Rotate List](https://leetcode.com/problems/rotate-list/)
3. [LeetCode #143: Reorder List](https://leetcode.com/problems/reorder-list/)

---

## Revision Notes

- Problem: Remove $n^{\text{th}}$ node from end of linked list in 1 pass.
- Pattern: Fast & Slow Pointers + Dummy Node (`ListNode dummy(0, head)`).
- Advance `fast` pointer $n + 1$ steps from `dummy`.
- `while (fast != nullptr)`: `slow = slow->next`, `fast = fast->next`.
- Delete: `slow->next = slow->next->next`.
- Return `dummy.next`.
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(1)$.
