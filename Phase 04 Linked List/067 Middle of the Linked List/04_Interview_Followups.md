# 04 Interview Follow-ups & System Variations: Middle of the Linked List

The problem finds the middle node of a singly linked list. The optimal approach uses **Fast and Slow Pointers** (`slow` advances 1 step, `fast` advances 2 steps) in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem tests even-length middle conventions (first vs. second middle) and deleting middle nodes in $\mathcal{O}(1)$ space.

---

## 1. Even Length Ambiguity: First Middle vs. Second Middle

### 💡 Pointer Termination Invariants
1. **Return Second Middle (LeetCode #876)**:
   - Loop condition: `while (fast != nullptr && fast->next != nullptr)`
   - For `[1, 2, 3, 4]`, returns node `3`.
2. **Return First Middle (Crucial for Merge Sort / Palindrome splitting)**:
   - Loop condition: `while (fast->next != nullptr && fast->next->next != nullptr)`
   - For `[1, 2, 3, 4]`, returns node `2`.
   - Leaves the left half `[1, 2]` cleanly separated from the right half `[3, 4]`.

---

## 2. Follow-up: Delete the Middle Node (LeetCode #2095)

### 💡 Tracking Previous Pointer
- Initialize `dummy(0, head)`, `slow = &dummy`, `fast = head`.
- Advance `slow` by 1 and `fast` by 2 until `fast == nullptr || fast->next == nullptr`.
- At termination, `slow` points **immediately before the middle node**.
- Delete: `slow->next = slow->next->next`.

---

## Summary Matrix: Trade-offs at a Glance

| Goal | Loop Condition | Even Length Node (e.g., 4 nodes) |
| :--- | :--- | :--- |
| **Second Middle** | `fast && fast->next` | Node 3 (2nd middle) |
| **First Middle** | `fast->next && fast->next->next` | Node 2 (1st middle) |
| **Delete Middle** | `slow` starts at dummy head | Directly unlinks middle node |
