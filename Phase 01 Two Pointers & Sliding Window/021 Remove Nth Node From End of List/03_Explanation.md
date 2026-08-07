# Problem Summary

Given the head of a linked list, remove the $n^{\text{th}}$ node from the end in a **single pass**. Using a `dummy` node pointing to `head` and two pointers (`fast` and `slow`) separated by $n + 1$ steps, advancing both pointers together until `fast` hits `nullptr` positions `slow` right before the target node. We bypass the target node in $\mathcal{O}(L)$ single-pass time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to find or remove the $N^{\text{th}}$ element **from the end** of a singly linked list in a single pass.
- Fixed gap fast/slow pointer technique applies.

---

## Important Clues

1. **"Nth node from the end"**: Signals Fast & Slow pointer gap of $N$.
2. **"Single pass follow-up"**: Excludes computing length $L$ in pass 1 and traversing in pass 2.

---

## Example

### Input
`head = [1, 2, 3, 4, 5]`, `n = 2`

### Visual Step-by-Step Progression

```text
dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> null
  S           F   (gap of n + 1 = 3 nodes)

Move both until F reaches null:
dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> null
                   S               F (F is null!)

Bypass target: slow->next = slow->next->next (removes 4)
Result: [1, 2, 3, 5]
```

---

## Alternative Solutions

### Two Pass (Length $L$)
1. Pass 1: Compute length $L$.
2. Pass 2: Traverse to node at position $L - n - 1$.
3. Update `curr->next = curr->next->next`.
- **Time Complexity**: $\mathcal{O}(L)$ (2 passes).
- **Space Complexity**: $\mathcal{O}(1)$.

---

## Edge Cases

1. **Remove Head Node ($n = L$)**: Handled seamlessly by dummy node.
2. **Single Element List ($head = [1], n = 1$)**: Returns `[]`.
3. **Remove Last Element ($n = 1$)**: `slow` stops right before tail node.

---

## Interview Tips

- **Always Use a Dummy Node**: Emphasize *"Using a dummy node before head handles deleting the head node without adding special-case `if` branches."*
- **Explain Gap Rationale**: Clearly state *"Advancing `fast` by $n + 1$ steps ensures `slow` stops at the node PRECEDING the target node."*

---

## Similar Problems

1. [LeetCode #61: Rotate List](https://leetcode.com/problems/rotate-list/)
2. [LeetCode #2095: Delete the Middle Node of a Linked List](https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/)
3. [LeetCode #876: Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)

---

## Revision Notes

- Problem: Remove $n^{\text{th}}$ node from end of linked list in 1 pass.
- Strategy: Fast & Slow pointers separated by gap of $n + 1$.
- `ListNode dummy(0); dummy.next = head`.
- Advance `fast` $n + 1$ steps from `dummy`.
- Move `fast` and `slow` together until `fast == nullptr`.
- `slow->next = slow->next->next`.
- Return `dummy.next`.
- Optimal Complexity: Time $\mathcal{O}(L)$ (1 pass), Space $\mathcal{O}(1)$.
