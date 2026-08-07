# Problem Summary

Given the heads of two sorted linked lists `list1` and `list2`, merge them into a single sorted linked list by splicing node pointers. The optimal approach uses a **Dummy Sentinel Node** and a **Tail Pointer**. Comparing front nodes of `list1` and `list2`, we iteratively stitch `tail->next` to the smaller node. Remaining nodes are attached directly in $\mathcal{O}(N + M)$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to **combine / merge two sorted lists or sequences** (e.g. Merge Sort on Linked List, Merge $K$ Sorted Lists).
- Dummy Head Node & Two-Pointer Splicing pattern.

---

## Important Clues

1. **"Merge two sorted lists"**: Zip merge.
2. **"Splicing together nodes"**: In-place pointer manipulation constraint.

---

## Example

### Input
`list1 = [1 -> 2 -> 4]`, `list2 = [1 -> 3 -> 4]`

### Visual Step-by-Step Progression

```text
Dummy -> [ ]
          |
         Compare list1 (1) vs list2 (1) -> Link list1 (1)

Dummy -> [1] -> [1] -> [2] -> [3] -> [4] -> [4]

Result Head: dummy.next (Value 1)
```

---

## Alternative Solutions

### Recursive Merge (O(N + M) Time, O(N + M) Stack Space)
```cpp
ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
    if (!l1) return l2;
    if (!l2) return l1;
    if (l1->val <= l2->val) {
        l1->next = mergeTwoLists(l1->next, l2);
        return l1;
    } else {
        l2->next = mergeTwoLists(l1, l2->next);
        return l2;
    }
}
```
- **Time Complexity**: $\mathcal{O}(N + M)$.
- **Space Complexity**: $\mathcal{O}(N + M)$ recursion stack depth.

---

## Edge Cases

1. **Both Lists Empty**: `list1 = nullptr, list2 = nullptr` -> Returns `nullptr`.
2. **One List Empty**: `list1 = [], list2 = [0]` -> Returns `[0]`.
3. **Different Lengths**: One list finishes early; remaining portion attached in $\mathcal{O}(1)$ time.

---

## Interview Tips

- **Explain Dummy Node Sentinel Utility**: State *"Using a stack-allocated dummy node `ListNode dummy(0)` eliminates special boundary checks for initializing the head of the merged list, allowing clean uniform pointer updates `tail = tail->next`."*

---

## Similar Problems

1. [LeetCode #23: Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)
2. [LeetCode #88: Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)
3. [LeetCode #148: Sort List](https://leetcode.com/problems/sort-list/)

---

## Revision Notes

- Problem: Merge 2 sorted linked lists in-place.
- Pattern: Dummy Sentinel Node (`ListNode dummy(0)`, `tail = &dummy`).
- `while (list1 && list2)`:
  - `if (list1->val <= list2->val) tail->next = list1, list1 = list1->next`.
  - `else tail->next = list2, list2 = list2->next`.
  - `tail = tail->next`.
- Attach remainder: `tail->next = (list1 ? list1 : list2)`.
- Return `dummy.next`.
- Optimal Complexity: Time $\mathcal{O}(N + M)$, Space $\mathcal{O}(1)$.
