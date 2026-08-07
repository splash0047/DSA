# Problem Summary

Given two non-empty linked lists `l1` and `l2` representing non-negative integers stored in **reverse order**, add the numbers and return the sum as a linked list. The optimal approach uses **Single-Pass Digit Addition with Carry**. We traverse `l1` and `l2` together while `l1 != nullptr || l2 != nullptr || carry > 0`. At each digit position, compute `sum = val1 + val2 + carry`, set `carry = sum / 10`, and append `new ListNode(sum % 10)` in $\mathcal{O}(\max(N, M))$ time and $\mathcal{O}(\max(N, M))$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to perform **digit arithmetic / BigInt addition** represented as linked lists or arrays.
- Column Addition with Carry pattern.

---

## Important Clues

1. **"Digits stored in reverse order"**: Least significant digit at head $\implies$ Direct left-to-right addition.
2. **"Non-negative integers"**: No negative value checks required.

---

## Example

### Input
`l1 = [2 -> 4 -> 3]` (342)
`l2 = [5 -> 6 -> 4]` (465)

### Visual Step-by-Step Progression

```text
  2 -> 4 -> 3
+ 5 -> 6 -> 4
--------------
  7 -> 0 -> 8   (Carry 1 generated at second position: 4+6=10)

Result: [7 -> 0 -> 8] (807)
```

---

## Alternative Solutions

### Forward-Stored Addition (Add Two Numbers II - LeetCode #445)
- If digits are stored in **forward order** (Most Significant Digit at head), reverse both lists first (or use Stacks), perform digit addition, then reverse the result list.
- **Time Complexity**: $\mathcal{O}(N + M)$.
- **Space Complexity**: $\mathcal{O}(N + M)$.

---

## Edge Cases

1. **Lists of Different Lengths**: `l1 = [9, 9, 9]`, `l2 = [1]` -> Shorter list padded with `0`.
2. **Final Carry Overflow**: `l1 = [9, 9]`, `l2 = [1]` -> Generates additional node `[0, 0, 1]` (100).
3. **Single Digit Zeroes**: `l1 = [0]`, `l2 = [0]` -> Returns `[0]`.

---

## Interview Tips

- **Explain Loop Termination Condition**: State *"We include `carry > 0` in the while loop condition `while (l1 || l2 || carry > 0)` so that any leftover carry at the highest digit position automatically appends a new most-significant-digit node."*

---

## Similar Problems

1. [LeetCode #445: Add Two Numbers II](https://leetcode.com/problems/add-two-numbers-ii/)
2. [LeetCode #43: Multiply Strings](https://leetcode.com/problems/multiply-strings/)
3. [LeetCode #66: Plus One](https://leetcode.com/problems/plus-one/)

---

## Revision Notes

- Problem: Add two numbers stored as reversed linked lists.
- Pattern: Single-Pass Digit Addition with `carry`.
- Loop: `while (l1 != nullptr || l2 != nullptr || carry > 0)`.
- `val1 = l1 ? l1->val : 0`, `val2 = l2 ? l2->val : 0`.
- `sum = val1 + val2 + carry`, `carry = sum / 10`.
- `curr->next = new ListNode(sum % 10)`.
- Optimal Complexity: Time $\mathcal{O}(\max(N, M))$, Space $\mathcal{O}(\max(N, M))$.
