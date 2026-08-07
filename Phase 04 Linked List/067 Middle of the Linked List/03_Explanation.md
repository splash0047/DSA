# Problem Summary

Given the `head` of a singly linked list, find and return its middle node (or second middle node if length is even). The optimal approach uses **Floyd's Fast & Slow Pointers**. Pointer `slow` moves 1 node at a time while `fast` moves 2 nodes at a time. When `fast` reaches the end (`fast == nullptr` or `fast->next == nullptr`), `slow` sits at the middle node in a single pass taking $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to find the **middle node / midpoint** of a linked list in a single pass (e.g. Merge Sort on Linked List, Palindrome check).
- Fast & Slow Pointer pattern.

---

## Important Clues

1. **"Return second middle node"**: Requires `fast != nullptr && fast->next != nullptr` loop termination.
2. **"Single pass"**: Fast/Slow pointer application.

---

## Example

### Input
`head = [1 -> 2 -> 3 -> 4 -> 5 -> 6]`

### Visual Step-by-Step Progression

```text
Start:  S/F
       [ 1  ->  2  ->  3  ->  4  ->  5  ->  6 ]

Step 1:         S       F
       [ 1  ->  2  ->  3  ->  4  ->  5  ->  6 ]

Step 2:                 S               F
       [ 1  ->  2  ->  3  ->  4  ->  5  ->  6 ]

Step 3:                         S                   F (nullptr)
       [ 1  ->  2  ->  3  ->  4  ->  5  ->  6 ]

Result: Node 4 (Second Middle Node)
```

---

## Alternative Solutions

### Two-Pass Length Counter (O(N) Time, O(1) Space)
- Pass 1 counts total nodes $N$. Pass 2 traverses $N/2$ steps to return middle node.
- **Time Complexity**: $\mathcal{O}(N)$ (1.5 N steps).
- **Space Complexity**: $\mathcal{O}(1)$.

---

## Edge Cases

1. **Single Node List**: `head = [1]` -> `slow` stays at `1`, returns `1`.
2. **Two Node List**: `head = [1 -> 2]` -> `slow` moves to `2`, returns `2` (second middle).
3. **Even Length List**: `head = [1 -> 2 -> 3 -> 4]` -> Returns `3`.

---

## Interview Tips

- **Explain First vs Second Middle Preference**: State *"In LeetCode #876, we use `while (fast && fast->next)` to return the second middle node for even lengths. For problems like Merge Sort on Linked List where we want the first middle node as the left partition tail, we use `while (fast->next && fast->next->next)` instead."*

---

## Similar Problems

1. [LeetCode #141: Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)
2. [LeetCode #234: Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)
3. [LeetCode #148: Sort List](https://leetcode.com/problems/sort-list/)

---

## Revision Notes

- Problem: Find middle node of linked list in 1 pass.
- Pattern: Fast & Slow Pointers (`slow = slow->next`, `fast = fast->next->next`).
- Loop: `while (fast != nullptr && fast->next != nullptr)`.
- Return `slow`.
- For Even lengths: Returns second middle node.
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(1)$.
