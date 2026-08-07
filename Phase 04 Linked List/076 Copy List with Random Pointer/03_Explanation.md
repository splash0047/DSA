# Problem Summary

Given the `head` of a linked list where each node contains a value, `next` pointer, and an arbitrary `random` pointer, create a **deep copy** of the list. The optimal approach uses **Interleaved Node Weaving**:
1. **Pass 1**: Insert cloned nodes directly after original nodes ($A \rightarrow A' \rightarrow B \rightarrow B'$).
2. **Pass 2**: Set `curr->next->random = curr->random->next`.
3. **Pass 3**: Separate the interleaved list back into original and copied lists.
This creates a deep copy in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ auxiliary space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to **deep copy a graph or linked list** with auxiliary pointers in $\mathcal{O}(1)$ auxiliary space.
- Interleaved Node Weaving pattern.

---

## Important Clues

1. **"Deep copy of list with random pointer"**: Arbitrary graph pointer cloning.
2. **"O(1) auxiliary space requirement"**: Interleaved node weaving trick.

---

## Example

### Input
`head = [A -> B]` (`A.random = B`, `B.random = A`)

### Visual Step-by-Step Progression

```text
Step 1 (Weave Clones):
[ A ] -> [ A' ] -> [ B ] -> [ B' ] -> nullptr

Step 2 (Assign Random Pointers):
A'.random = A.random.next = B'
B'.random = B.random.next = A'

Step 3 (Unweave / Separate):
Original: [ A ] -> [ B ] -> nullptr
Copy:     [ A' ] -> [ B' ] -> nullptr (Return A')
```

---

## Alternative Solutions

### Hash Map Pointer Mapping (O(N) Time, O(N) Space)
- Use `std::unordered_map<Node*, Node*> old_to_new` to map original nodes to clones. Pass 1 creates nodes, Pass 2 wires pointers.
- **Time Complexity**: $\mathcal{O}(N)$.
- **Space Complexity**: $\mathcal{O}(N)$.

---

## Edge Cases

1. **Empty List**: `head = nullptr` -> Returns `nullptr`.
2. **All Random Pointers Null**: `curr->random == nullptr` -> Handled via null guard.
3. **Random Pointer Points to Self**: `A->random = A` $\implies A' \rightarrow \text{random} = A'$.

---

## Interview Tips

- **Explain Why Interleaving Replaces Hash Map**: State *"Interleaving clone node $A'$ right after original node $A$ establishes an implicit $\mathcal{O}(1)$ lookup structure inside the linked list itself ($A'$ is at $A \rightarrow \text{next}$ and $A'\text{.random}$ is at $A \rightarrow \text{random} \rightarrow \text{next}$), completely eliminating the $\mathcal{O}(N)$ auxiliary memory required by a Hash Map."*

---

## Similar Problems

1. [LeetCode #133: Clone Graph](https://leetcode.com/problems/clone-graph/)
2. [LeetCode #1485: Clone Binary Tree With Random Pointer](https://leetcode.com/problems/clone-binary-tree-with-random-pointer/)

---

## Revision Notes

- Problem: Deep copy linked list with random pointers in $\mathcal{O}(1)$ space.
- Strategy: 3-Pass Interleaved Weaving:
  1. Weave: Insert clone `curr->next = new Node(curr->val)` after each node.
  2. Wire Random: `if (curr->random) curr->next->random = curr->random->next`.
  3. Unweave: Separate original and cloned list links (`curr->next = curr->next->next`).
- Optimal Complexity: Time $\mathcal{O}(N)$, Auxiliary Space $\mathcal{O}(1)$.
