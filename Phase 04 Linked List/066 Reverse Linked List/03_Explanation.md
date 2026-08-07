# Problem Summary

Given the `head` of a singly linked list, reverse the list pointers in-place and return the new head. The optimal approach uses **3-Pointer Iterative Reversal** (`prev`, `curr`, `next_node`). At each node, store `next_node = curr->next`, redirect `curr->next = prev`, and advance pointers `prev = curr` and `curr = next_node`. This reverses the list in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to **reverse a linked list** or a portion of it (e.g. subsegment $[L, R]$, $K$-group reversal, palindrome check).
- 3-Pointer Link Reversal pattern (`prev`, `curr`, `next`).

---

## Important Clues

1. **"Reverse the list"**: Link orientation flip.
2. **"O(1) space follow-up"**: Mandatory iterative pointer manipulation.

---

## Example

### Input
`head = [1 -> 2 -> 3 -> 4 -> 5]`

### Visual Step-by-Step Progression

```text
Initial:  nullptr    1  ->  2  ->  3  ->  4  ->  5  ->  nullptr
            P        C      N

Step 1:   nullptr <- 1      2  ->  3  ->  4  ->  5  ->  nullptr
                     P      C      N

Step 2:   nullptr <- 1  <-  2      3  ->  4  ->  5  ->  nullptr
                            P      C      N

Final:    nullptr <- 1  <-  2  <-  3  <-  4  <-  5  (New Head = 5)
                                                 P
```

---

## Alternative Solutions

### Recursive Reversal (O(N) Time, O(N) Stack Space)
- Recursively call `reverseList(head->next)`. Set `head->next->next = head` and `head->next = nullptr`.
- **Time Complexity**: $\mathcal{O}(N)$.
- **Space Complexity**: $\mathcal{O}(N)$ recursion stack space.

---

## Edge Cases

1. **Empty List**: `head = nullptr` -> Returns `nullptr`.
2. **Single Node List**: `head = [1]` -> Returns `[1]`.
3. **Two Nodes**: `[1 -> 2]` -> Returns `[2 -> 1]`.

---

## Interview Tips

- **Mention Both Iterative & Recursive Approaches**: State *"The iterative 3-pointer solution is preferred because it achieves $\mathcal{O}(1)$ auxiliary space, whereas the recursive solution uses $\mathcal{O}(N)$ implicit call stack memory."*

---

## Similar Problems

1. [LeetCode #92: Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/)
2. [LeetCode #25: Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/)
3. [LeetCode #234: Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)

---

## Revision Notes

- Problem: Reverse singly linked list pointers in $\mathcal{O}(N)$ time, $\mathcal{O}(1)$ space.
- Pattern: 3 Pointers (`prev = nullptr`, `curr = head`).
- `while (curr != nullptr)`:
  - `next_node = curr->next`.
  - `curr->next = prev`.
  - `prev = curr`.
  - `curr = next_node`.
- Return `prev`.
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(1)$.
