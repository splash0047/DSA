# Problem Summary

Given `head` of a singly linked list, determine if the list contains a cycle. The optimal approach uses **Floyd's Cycle Detection Algorithm (Tortoise and Hare)**. Moving `slow` by 1 step and `fast` by 2 steps guarantees that if a cycle exists, `fast` will eventually catch `slow` (`slow == fast`). If no cycle exists, `fast` hits `nullptr`. This detects cycles in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to detect a **cycle / loop** in a linked list or sequence (e.g. Happy Number, Find Duplicate Number).
- Fast & Slow Pointer (Floyd's Cycle Finding) pattern.

---

## Important Clues

1. **"Determine if linked list has a cycle"**: Cycle detection.
2. **"O(1) memory follow-up"**: Floyd's Tortoise & Hare algorithm.

---

## Example

### Input
`head = [3 -> 2 -> 0 -> -4]` (where `-4` connects back to `2`)

### Visual Step-by-Step Progression

```text
Start:  S/F
       [ 3  ->  2  ->  0  -> -4 ]
                ^-------------|

Step 1:         S       F
       [ 3  ->  2  ->  0  -> -4 ]
                ^-------------|

Step 2:                 S
       [ 3  ->  2  ->  0  -> -4 ]
                ^-------------|
                F

Step 3:                         S/F (MEET AT NODE -4!)
       [ 3  ->  2  ->  0  -> -4 ]
                ^-------------|

Result: true
```

---

## Alternative Solutions

### Hash Set Address Tracking (O(N) Time, O(N) Space)
- Store visited node pointers in `std::unordered_set<ListNode*>`. If pointer repeated $\implies$ cycle!
- **Time Complexity**: $\mathcal{O}(N)$.
- **Space Complexity**: $\mathcal{O}(N)$.

---

## Edge Cases

1. **Empty List**: `head = nullptr` -> Returns `false`.
2. **Single Node without Cycle**: `head = [1]` -> Returns `false`.
3. **Single Self-Loop Node**: `head = [1 -> 1]` -> Returns `true`.

---

## Interview Tips

- **Explain the Mathematical Proof of Convergence**: State *"Once both `slow` and `fast` enter a cycle of length $C$, the relative distance between `fast` and `slow` closes by 1 node per iteration ($2 - 1 = 1$). Since the gap shrinks by 1 node per step, `fast` MUST meet `slow` in at most $C$ steps."*

---

## Similar Problems

1. [LeetCode #142: Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)
2. [LeetCode #287: Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)
3. [LeetCode #202: Happy Number](https://leetcode.com/problems/happy-number/)

---

## Revision Notes

- Problem: Detect cycle in singly linked list in $\mathcal{O}(1)$ space.
- Pattern: Floyd's Cycle Finding (`slow` step 1, `fast` step 2).
- `while (fast != nullptr && fast->next != nullptr)`:
  - `slow = slow->next`.
  - `fast = fast->next->next`.
  - `if (slow == fast) return true`.
- Return `false`.
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(1)$.
