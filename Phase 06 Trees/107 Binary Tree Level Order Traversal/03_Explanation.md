# Problem Summary

Given the `root` of a binary tree, return its level order traversal (left to right, level by level). The optimal approach uses **Queue-Based Iterative Level Order Traversal (BFS)**:
- Push `root` into `std::queue<TreeNode*> q`.
- While `!q.empty()`:
  - Record `sz = q.size()`.
  - Pop `sz` nodes, collect values into `current_level`, and enqueue non-null `left` and `right` children.
  - Append `current_level` to `ans`.
This traverses the tree level-by-level in $\mathcal{O}(N)$ time and $\mathcal{O}(N)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to process a **tree or graph layer-by-layer / level-by-level**.
- Queue-Based BFS Level Snapshot pattern.

---

## Important Clues

1. **"Level order traversal level by level"**: Standard BFS pattern.
2. **"Left to right order within levels"**: Queue FIFO order.

---

## Example

### Input
`root = [3, 9, 20, null, null, 15, 7]`

### Visual Step-by-Step Progression

```text
       3       <-- Level 0: [3]
      / \
     9   20    <-- Level 1: [9, 20]
        /  \
       15   7  <-- Level 2: [15, 7]

Result: [[3], [9, 20], [15, 7]]
```

---

## Alternative Solutions

### Recursive Preorder DFS with Level Depth Tracking
- Pass `depth` index in DFS. Append to `ans[depth]`.
- **Time Complexity**: $\mathcal{O}(N)$.
- **Space Complexity**: $\mathcal{O}(H)$ (auxiliary stack).

---

## Edge Cases

1. **Empty Tree**: `root = nullptr` -> Returns `[]`.
2. **Single Node Tree**: `root = [1]` -> Returns `[[1]]`.
3. **Skewed Linked-List Tree**: `1 -> 2 -> 3` -> Returns `[[1], [2], [3]]`.

---

## Interview Tips

- **Explain `sz = q.size()` Snapshot Technique**: State *"Capturing `sz = q.size()` at the start of each level iteration allows us to process PRECISELY the nodes belonging to the current level while safely pushing their children to the back of the queue for the NEXT level."*

---

## Similar Problems

1. [LeetCode #103: Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)
2. [LeetCode #107: Binary Tree Level Order Traversal II](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/)
3. [LeetCode #199: Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/)

---

## Revision Notes

- Problem: Level order traversal of binary tree.
- Pattern: Queue BFS (`sz = q.size()`).
- `while (!q.empty())`:
  - `sz = q.size(); vector<int> level;`
  - `for (i = 0; i < sz; ++i)`:
    - `curr = q.front(); q.pop();`
    - `level.push_back(curr->val);`
    - `if (curr->left) q.push(curr->left);`
    - `if (curr->right) q.push(curr->right);`
  - `ans.push_back(level);`
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(N)$.
