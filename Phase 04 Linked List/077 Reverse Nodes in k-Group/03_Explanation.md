# Problem Summary

Given the `head` of a linked list and `k`, reverse the nodes of the list $k$ at a time. If the number of nodes is not a multiple of $k$, the remaining trailing nodes must stay unchanged. The optimal approach uses **Iterative $K$-Group Subsegment Reversal**:
1. Check if $k$ nodes exist ahead (`getKthNode`). If not, terminate.
2. Reverse the $k$-node subsegment in-place with initial `prev = groupNext`.
3. Re-stitch boundary pointers (`groupPrev->next = kth`, `groupPrev = former_group_head`).
This achieves in-place reversal in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to **reverse a linked list in chunks of fixed size $K$** while maintaining trailing remainder nodes.
- Iterative $K$-Group Pointer Reversal pattern.

---

## Important Clues

1. **"Reverse nodes of list k at a time"**: Grouped subsegment reversal.
2. **"O(1) extra memory follow-up"**: Mandatory in-place boundary re-stitching.

---

## Example

### Input
`head = [1 -> 2 -> 3 -> 4 -> 5]`, `k = 2`

### Visual Step-by-Step Progression

```text
Group 1 [1, 2]:
[0 (dummy)] -> [ 1  ->  2 ] -> [ 3  ->  4  ->  5 ]
Reverse [1, 2] and stitch:
[0 (dummy)] -> [ 2  ->  1 ] -> [ 3  ->  4  ->  5 ]
                        ^ groupPrev

Group 2 [3, 4]:
Reverse [3, 4] and stitch:
[0] -> [ 2  ->  1 ] -> [ 4  ->  3 ] -> [ 5 ]
                                ^ groupPrev

Group 3 [5]: Fewer than k=2 nodes remaining -> Stop!

Result: [2 -> 1 -> 4 -> 3 -> 5]
```

---

## Alternative Solutions

### Vector Pointer Partitioning (O(N) Time, O(N) Space)
- Store nodes in `vector<ListNode*>`. Reverse sub-ranges of size $k$ using `std::reverse`.
- **Time Complexity**: $\mathcal{O}(N)$.
- **Space Complexity**: $\mathcal{O}(N)$.

---

## Edge Cases

1. **$k = 1$**: Returns original list immediately.
2. **$k == N$**: Entire list is reversed.
3. **$N < k$**: No nodes reversed; returns original list.

---

## Interview Tips

- **Explain Helper `getKthNode` Rationale**: State *"Using helper `getKthNode(curr, k)` allows us to look ahead $k$ nodes BEFORE attempting any pointer reversals. If fewer than $k$ nodes remain, we safely break without corrupting list links."*

---

## Similar Problems

1. [LeetCode #206: Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)
2. [LeetCode #92: Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/)
3. [LeetCode #24: Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)

---

## Revision Notes

- Problem: Reverse nodes in $k$-group in $\mathcal{O}(1)$ space.
- Pattern: Iterative $K$-Group Reversal (`dummy`, `groupPrev`).
- `while (true)`:
  - `kth = getKthNode(groupPrev, k)`.
  - `if (!kth) break`.
  - `groupNext = kth->next`.
  - Reverse subsegment `[groupPrev->next ... kth]` with `prev = groupNext`.
  - Re-stitch: `tmp = groupPrev->next; groupPrev->next = kth; groupPrev = tmp;`.
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(1)$.
