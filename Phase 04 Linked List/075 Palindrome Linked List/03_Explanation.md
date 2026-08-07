# Problem Summary

Given the `head` of a singly linked list, determine if it is a palindrome. The optimal approach uses **Find Mid + Reverse Second Half + Compare**:
1. Find midpoint using Fast & Slow pointers (`slow`, `fast`).
2. Reverse second half starting from `slow`.
3. Compare node values from `head` and reversed second half.
4. Restore second half to preserve original structure.
This evaluates the palindrome in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to verify if a **singly linked list is a palindrome** in $\mathcal{O}(1)$ auxiliary space.
- 3-Phase Linked List Pattern: Find Mid + Reverse Half + Compare.

---

## Important Clues

1. **"Return true if palindrome"**: Symmetrical sequence check.
2. **"O(1) space follow-up"**: Mandatory in-place second half reversal.

---

## Example

### Input
`head = [1 -> 2 -> 2 -> 1]`

### Visual Step-by-Step Progression

```text
Step 1 (Find Mid):
[1  ->  2  ->  2  ->  1]
               ^ (slow stops at index 2)

Step 2 (Reverse Second Half):
First Half:   [ 1  ->  2 ]
Reversed 2nd: [ 1  ->  2 ]

Step 3 (Compare Node Values):
Compare 1 == 1 AND 2 == 2 (MATCH!)

Result: true
```

---

## Alternative Solutions

### Vector Copy & Two Pointers (O(N) Time, O(N) Space)
- Copy values into `std::vector<int>`. Check palindrome using `left` and `right` indices.
- **Time Complexity**: $\mathcal{O}(N)$.
- **Space Complexity**: $\mathcal{O}(N)$.

---

## Edge Cases

1. **Single Node List**: `head = [1]` -> Returns `true`.
2. **Two Node Palindrome**: `head = [1 -> 1]` -> Returns `true`.
3. **Odd Length Palindrome**: `head = [1 -> 2 -> 1]` -> Returns `true`.

---

## Interview Tips

- **Mention List Structure Restoration**: State *"Restoring the linked list back to its original structure after reversing the second half is an essential production software engineering practice, ensuring zero side-effects for callers."*

---

## Similar Problems

1. [LeetCode #206: Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)
2. [LeetCode #143: Reorder List](https://leetcode.com/problems/reorder-list/)
3. [LeetCode #9: Palindrome Number](https://leetcode.com/problems/palindrome-number/)

---

## Revision Notes

- Problem: Check if singly linked list is palindrome in $\mathcal{O}(1)$ space.
- Strategy: 4-Step Algorithm:
  1. Mid: Fast & Slow pointers (`slow`, `fast`).
  2. Reverse: Reverse from `slow`.
  3. Compare: Walk `first = head` and `second = reversed_head`.
  4. Restore: Re-reverse second half.
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(1)$.
