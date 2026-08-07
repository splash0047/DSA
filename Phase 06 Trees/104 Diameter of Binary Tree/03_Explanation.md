# Problem Summary

Given the `root` of a binary tree, return the length of its **diameter** (longest path of edges between any two nodes). The optimal approach uses **Bottom-Up Postorder DFS with Global Diameter Tracking**:
- Helper `getHeight(node)`:
  - Base case: `if (!node) return 0;`
  - `left_h = getHeight(node->left); right_h = getHeight(node->right);`
  - Update `max_diameter = max(max_diameter, left_h + right_h);`
  - Return `1 + max(left_h, right_h);`
This calculates the diameter in $\mathcal{O}(N)$ time and $\mathcal{O}(H)$ call stack space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to find the **longest path / max sum path passing through turning nodes** in a tree.
- Bottom-Up Postorder DFS + Global Max Accumulator pattern.

---

## Important Clues

1. **"Longest path between any two nodes"**: Tree diameter.
2. **"Path may or may not pass through root"**: Global maximum tracking at every node.

---

## Example

### Input
`root = [1, 2, 3, 4, 5]`

### Visual Step-by-Step Progression

```text
       1
      / \
     2   3
    / \
   4   5

Path [4 -> 2 -> 1 -> 3] has 3 edges!
- Left height of root 1 = 2
- Right height of root 1 = 1
- Diameter at root 1 = 2 + 1 = 3 edges
```

---

## Alternative Solutions

### Top-Down Recomputed Height (Brute Force)
- For every node, calculate `height(node->left) + height(node->right)` via separate recursive helper calls.
- **Time Complexity**: $\mathcal{O}(N^2)$.
- **Space Complexity**: $\mathcal{O}(H)$.

---

## Edge Cases

1. **Single Node Tree**: `root = [1]` -> Returns `0` edges.
2. **Linear / Skewed Tree**: `1 -> 2 -> 3` -> Returns `2` edges.
3. **Diameter Does Not Pass Through Root**: Subtree has longer diameter than root path. Global `max_diameter` captures this correctly.

---

## Interview Tips

- **Explain Edges vs Nodes Representation**: State *"The path length in edges passing through a node is `left_height + right_height` (without adding 1). The return value to the parent node `1 + max(left_height, right_height)` represents the node height in terms of edges going up."*

---

## Similar Problems

1. [LeetCode #124: Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)
2. [LeetCode #687: Longest Univalue Path](https://leetcode.com/problems/longest-univalue-path/)
3. [LeetCode #1522: Diameter of N-Ary Tree](https://leetcode.com/problems/diameter-of-n-ary-tree/)

---

## Revision Notes

- Problem: Diameter of binary tree (longest path in edges).
- Pattern: Postorder DFS + `max_diameter`.
- Helper `getHeight(node)`:
  - `if (!node) return 0;`
  - `left = getHeight(node->left); right = getHeight(node->right);`
  - `max_diameter = max(max_diameter, left + right);`
  - `return 1 + max(left, right);`
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(H)$.
