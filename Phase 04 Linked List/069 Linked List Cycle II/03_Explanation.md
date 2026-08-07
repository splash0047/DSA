# Problem Summary

Given the `head` of a linked list, return the node where the cycle begins, or `null` if there is no cycle. The optimal approach uses **Floyd's Cycle Entry Finding Algorithm**. After detecting collision (`slow == fast`), we place an `entry` pointer at `head` and advance both `entry` and `slow` 1 step at a time (`entry = entry->next`, `slow = slow->next`). They meet precisely at the cycle start node in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to find the **starting entry node** of a cycle in a linked list or sequence.
- Floyd's Entry Pointer Collision pattern.

---

## Important Clues

1. **"Return the node where the cycle begins"**: Entry node identification.
2. **"O(1) memory constraint"**: Floyd's dual-phase pointer algorithm.

---

## Example

### Input
`head = [3 -> 2 -> 0 -> -4]` (where `-4` connects back to `2`)

### Visual Step-by-Step Progression

```text
Phase 1 (Collision Detection):
slow & fast collide at node -4.

Phase 2 (Entry Pointer Meeting):
Entry:  [ 3 ]  ->  [ 2 ] (Cycle Start!)
                   ^
Slow:   [ -4 ] ->  [ 2 ] (Cycle Start!)

Meeting Node: Node 2
```

---

## Alternative Solutions

### Hash Set Address Tracking (O(N) Time, O(N) Space)
- Store visited node pointers in `std::unordered_set<ListNode*>`. The first repeated pointer is the cycle start.
- **Time Complexity**: $\mathcal{O}(N)$.
- **Space Complexity**: $\mathcal{O}(N)$.

---

## Edge Cases

1. **No Cycle**: Returns `nullptr`.
2. **Cycle Starts at Head** (`pos = 0`): `entry` and `slow` meet immediately at `head`.
3. **Single Self-Loop Node**: Returns `head`.

---

## Interview Tips

- **Derive $L_1 = k \cdot C - L_2$ On Board**: Explain *"When slow and fast collide, $2(L_1 + L_2) = L_1 + L_2 + k \cdot C$, simplifying to $L_1 = k \cdot C - L_2$. This proves mathematically that advancing `head` and `slow` at equal speed guarantees meeting at the cycle entry node."*

---

## Similar Problems

1. [LeetCode #141: Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)
2. [LeetCode #287: Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)
3. [LeetCode #160: Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/)

---

## Revision Notes

- Problem: Find starting node of linked list cycle in $\mathcal{O}(1)$ space.
- Pattern: Floyd's 2-Phase Algorithm.
- Phase 1: `slow = slow->next`, `fast = fast->next->next` until `slow == fast`.
- Phase 2: `entry = head`. While `entry != slow`, `entry = entry->next`, `slow = slow->next`.
- Return `entry`.
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(1)$.
