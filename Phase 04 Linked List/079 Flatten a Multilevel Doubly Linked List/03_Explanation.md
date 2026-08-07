# Problem Summary

Given the head of a multilevel doubly linked list where nodes contain `prev`, `next`, and optional `child` pointers, flatten the structure into a single-level doubly linked list. The optimal approach uses **In-Place Iterative Splice Re-linking**. When encountering a node `curr` with a `child`, we locate the tail of the child branch (`child_tail`), splice `child_tail` to `curr->next`, link `curr->next = child_head`, and clear `curr->child = nullptr`. This flattens the structure in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to **flatten a multilevel / hierarchical linked list** in-place without recursion.
- In-Place Branch Splicing pattern.

---

## Important Clues

1. **"Multilevel doubly linked list"**: Hierarchical doubly-linked structure.
2. **"Child pointers must be set to null"**: Inline branch flattening requirement.

---

## Example

### Input
`1 <-> 2 <-> 3 <-> 4` (where `3` has child `7 <-> 8`)

### Visual Step-by-Step Progression

```text
Before:
1 <-> 2 <-> 3 <-> 4
            |
            7 <-> 8

Splicing Step at Node 3:
1 <-> 2 <-> 3 <-> 7 <-> 8 <-> 4
            ^ (child set to nullptr)

Result: 1 <-> 2 <-> 3 <-> 7 <-> 8 <-> 4
```

---

## Alternative Solutions

### Stack Preorder DFS Traversal (O(N) Time, O(N) Space)
- Perform Preorder DFS using `std::stack<Node*>`. Reconstruct doubly linked pointers from the collected sequence.
- **Time Complexity**: $\mathcal{O}(N)$.
- **Space Complexity**: $\mathcal{O}(N)$.

---

## Edge Cases

1. **Empty List**: `head = nullptr` -> Returns `nullptr`.
2. **No Child Pointers**: Returns original list unchanged.
3. **Child Branch at Last Node**: `curr->next == nullptr` -> Child tail's `next` remains `nullptr`.

---

## Interview Tips

- **Explain Why In-Place Traversal Handles Nested Children**: State *"Because `curr` moves forward node-by-node (`curr = curr->next`), inserting child branch $C$ inline guarantees that if node $C_i$ inside the child branch itself has a sub-child branch, the traversal loop will encounter and flatten it naturally!"*

---

## Similar Problems

1. [LeetCode #114: Flatten Binary Tree to Linked List](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/)
2. [LeetCode #138: Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/)

---

## Revision Notes

- Problem: Flatten multilevel doubly linked list in $\mathcal{O}(1)$ space.
- Pattern: In-Place Branch Splicing (`curr->child`).
- `while (curr)`:
  - `if (curr->child)`:
    - Find `child_tail`.
    - `if (curr->next) child_tail->next = curr->next; curr->next->prev = child_tail;`
    - `curr->next = child_head; child_head->prev = curr;`
    - `curr->child = nullptr;`
  - `curr = curr->next`.
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(1)$.
