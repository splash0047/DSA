# Problem Summary

Determine the minimum number of minutes for all fresh oranges (`1`) in a grid to become rotted (`2`) via 4-directional spreading from initially rotten oranges (`2`). Return `-1` if impossible. The optimal approach uses **Multi-Source Queue BFS**:
- Count `freshCount` and enqueue all initially rotten oranges `2`.
- Perform level-order BFS: each queue level iteration represents 1 minute.
- Pop rotten oranges, convert fresh neighbors to rotten (`2`), decrement `freshCount`, and enqueue.
- Return `freshCount == 0 ? minutes : -1`.
This finds the minimum rotting time in $\mathcal{O}(M \times N)$ time and $\mathcal{O}(M \times N)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need the **minimum time / steps for simultaneous multi-source propagation** (infection, fire, flood).
- Multi-Source BFS pattern.

---

## Important Clues

1. **"Minimum number of minutes"**: Shortest path $\implies$ BFS.
2. **"Multiple initial rotten oranges"**: Multi-source queue initialization.

---

## Example

### Input
`grid = [[2,1,1],[1,1,0],[0,1,1]]`

### Visual Step-by-Step Progression

```text
Min 0:  [2,1,1]  (Fresh: 6)
        [1,1,0]
        [0,1,1]

Min 1:  [2,2,1]  (Fresh: 4)
        [2,1,0]
        [0,1,1]

Min 2:  [2,2,2]  (Fresh: 2)
        [2,2,0]
        [0,1,1]

Min 3:  [2,2,2]  (Fresh: 1)
        [2,2,0]
        [0,2,1]

Min 4:  [2,2,2]  (Fresh: 0) -> Done!
        [2,2,0]
        [0,2,2]

Result: 4
```

---

## Alternative Solutions

### Minute-by-Minute Full Grid Scan ($\mathcal{O}((M \times N)^2)$ Time)
- Scan entire grid on every minute to find current rotten oranges and rot neighbors.

---

## Edge Cases

1. **No fresh oranges initially**: Returns `0`.
2. **Fresh orange isolated by empty cells (`0`)**: Returns `-1`.
3. **No rotten oranges initially (with fresh oranges)**: Returns `-1`.

---

## Interview Tips

- **Explain Multi-Source Initialization**: State *"By pushing ALL initial rotten oranges into the BFS queue before starting the level loop, all rotting fronts expand simultaneously per minute, guaranteeing shortest time calculation."*

---

## Similar Problems

1. [LeetCode #286: Walls and Gates](https://leetcode.com/problems/walls-and-gates/)
2. [LeetCode #1162: As Far from Land as Possible](https://leetcode.com/problems/as-far-from-land-as-possible/)
3. [LeetCode #542: 01 Matrix](https://leetcode.com/problems/01-matrix/)

---

## Revision Notes

- Problem: Minimum minutes to rot all fresh oranges.
- Pattern: Multi-Source Queue BFS.
- Queue Init: Push all `2`s into `q`, count `fresh`.
- Loop: `while (!q.empty() && fresh > 0) { sz = q.size(); minutes++; for (sz) pop -> rot 4-neighbors -> fresh-- -> push; }`
- Result: `fresh == 0 ? minutes : -1`.
- Optimal Complexity: Time $\mathcal{O}(M \times N)$, Space $\mathcal{O}(M \times N)$.
