# Problem Summary

Find the length of the shortest transformation sequence from `beginWord` to `endWord` changing 1 character at a time using words in `wordList`. Return `0` if impossible. The optimal approach uses **On-the-Fly Character Substitution BFS**:
- Store `wordList` in `unordered_set<string> wordSet`. If `endWord` absent, return `0`.
- Perform level-by-level BFS from `beginWord`.
- For each character position in current word, mutate from `'a'` to `'z'`.
- If mutated word exists in `wordSet`, erase it (mark visited) and enqueue.
- Incremental level count when target `endWord` reached returns sequence length.
This finds shortest transformation in $\mathcal{O}(N \times L \times 26)$ time and $\mathcal{O}(N \times L)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need the **shortest transformation / minimum edits between states**.
- State Mutation BFS pattern.

---

## Important Clues

1. **"Shortest transformation sequence"**: Unweighted shortest path $\implies$ BFS.
2. **"Differs by a single letter"**: 26-letter single character mutation.

---

## Example

### Input
`beginWord = "hit"`, `endWord = "cog"`, `wordList = ["hot","dot","dog","lot","log","cog"]`

### Visual Step-by-Step Progression

```text
hit (Level 1)
 |
hot (Level 2)
 / \
dot lot (Level 3)
 |   |
dog log (Level 4)
 \  /
 cog (Level 5) -> Found! Length = 5
```

---

## Alternative Solutions

### Bidirectional BFS ($\mathcal{O}(N \times L \times 26)$ Time with $2\times$ Speedup)
- Run two BFS queues simultaneously from `beginWord` and `endWord`, expanding whichever set is smaller to meet in the middle.

---

## Edge Cases

1. **`endWord` not in `wordList`**: Returns `0`.
2. **No valid transformation path**: Queue empties $\implies$ returns `0`.
3. **`beginWord` already 1 char away from `endWord`**: Returns `2`.

---

## Interview Tips

- **Explain Why 26-Letter Substitution Beats Pairwise Graph**: State *"Pairwise comparison takes $\mathcal{O}(N^2 \cdot L)$ which is quadratic in $N$. Mutating each character through 26 letters takes $\mathcal{O}(N \cdot L \cdot 26)$ which is linear in dictionary size $N$ for short word lengths."*

---

## Similar Problems

1. [LeetCode #126: Word Ladder II](https://leetcode.com/problems/word-ladder-ii/)
2. [LeetCode #433: Minimum Genetic Mutation](https://leetcode.com/problems/minimum-genetic-mutation/)
3. [LeetCode #752: Open the Lock](https://leetcode.com/problems/open-the-lock/)

---

## Revision Notes

- Problem: Shortest transformation sequence from `beginWord` to `endWord`.
- Pattern: On-the-fly 26-letter substitution BFS.
- Core Loop: `for (pos) for (ch = 'a'..'z') { mutate; if (wordSet.count(curr)) { wordSet.erase(curr); q.push(curr); } }`
- Termination: Return `level` when `curr == endWord`.
- Optimal Complexity: Time $\mathcal{O}(N \cdot L \cdot 26)$, Space $\mathcal{O}(N \cdot L)$.
