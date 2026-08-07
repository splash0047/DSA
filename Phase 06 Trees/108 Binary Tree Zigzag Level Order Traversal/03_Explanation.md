# Problem Summary

Given the `root` of a binary tree, return its zigzag level order traversal (left-to-right, then right-to-left, alternating per level). The optimal approach uses **BFS Direct Index Insertion**:
- Maintain `leftToRight = true`.
- At each level of size `sz`:
  - Pre-allocate `level(sz)`.
  - Calculate `index = leftToRight ? i : (sz - 1 - i)`.
  - Place `level[index] = curr->val`.
  - Enqueue non-null children.
  - Toggle `leftToRight = !leftToRight`.
This evaluates zigzag level order traversal in $\mathcal{O}(N)$ time and $\mathcal{O}(N)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to perform **level order traversal with alternating directional orientation**.
- BFS Direct Index Insertion pattern.

---

## Important Clues

1. **"Zigzag level order traversal"**: Alternating level directions.
2. **"Left to right, then right to left"**: Flag-based index placement.

---

## Example

### Input
`root = [3, 9, 20, null, null, 15, 7]`

### Visual Step-by-Step Progression

```text
       3       <-- Level 0 (L -> R): [3]
      / \
     9   20    <-- Level 1 (R -> L): [20, 9]
        /  \
       15   7  <-- Level 2 (L -> R): [15, 7]

Result: [[3], [20, 9], [15, 7]]
```

---

## Alternative Solutions

### Standard BFS + `std::reverse` (Brute Force)
- Run standard BFS and call `std::reverse(level.begin(), level.end())` on odd level vectors.
- **Time Complexity**: $\mathcal{O}(N)$.
- **Space Complexity**: $\mathcal{O}(N)$.

---

## Edge Cases

1. **Empty Tree**: `root = nullptr` -> Returns `[]`.
2. **Single Node Tree**: `root = [1]` -> Returns `[[1]]`.
3. **Deep Linear Tree**: Alternates direction at each single-node level.

---

## Interview Tips

- **Highlight Direct Index Placement Advantage**: State *"By calculating `index = leftToRight ? i : (sz - 1 - i)` and inserting directly into a pre-allocated vector of size `sz`, we eliminate the need to call `std::reverse` on level vectors, achieving zero-overhead $\mathcal{O}(N)$ performance."*

---

## Similar Problems

1. [LeetCode #102: Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)
2. [LeetCode #107: Binary Tree Level Order Traversal II](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/)
3. [LeetCode #199: Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/)

---

## Revision Notes

- Problem: Zigzag level order traversal of binary tree.
- Pattern: BFS + `index = leftToRight ? i : (sz - 1 - i)`.
- `while (!q.empty())`:
  - `sz = q.size(); vector<int> level(sz);`
  - `for (i = 0; i < sz; ++i)`:
    - `curr = q.front(); q.pop();`
    - `index = leftToRight ? i : (sz - 1 - i); level[index] = curr->val;`
    - `if (curr->left) q.push(curr->left);`
    - `if (curr->right) q.push(curr->right);`
  - `leftToRight = !leftToRight; ans.push_back(level);`
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(N)$.
