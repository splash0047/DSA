# Problem Summary

Given an array of integer `asteroids` (positive = moving right, negative = moving left), determine the surviving asteroids after all collisions. The optimal approach uses a **Stack Collision Simulation**:
- Iterate through `asteroids`. Maintain a `vector<int> st` acting as a stack.
- Collision occurs ONLY when `st.back() > 0` (moving right) and `ast < 0` (moving left).
- While collision condition holds:
  - If `st.back() < -ast`: Pop `st.back()` (rightward explodes) and continue loop.
  - If `st.back() == -ast`: Pop `st.back()` and mark `alive = false` (both explode).
  - If `st.back() > -ast`: Mark `alive = false` (leftward explodes).
- If `alive`, push `ast`.
This resolves all collisions in $\mathcal{O}(N)$ time and $\mathcal{O}(N)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to simulate **sequential interactions / cancellations of opposing directional objects**.
- Stack Collision Simulation pattern.

---

## Important Clues

1. **"Positive moving right, negative moving left"**: Directional collision vectors.
2. **"Smaller one explodes / same size both explode"**: LIFO cancellation mechanics.

---

## Example

### Input
`asteroids = [10, 2, -5]`

### Visual Step-by-Step Progression

```text
Asteroids: [10 ->] [2 ->] [<- -5]

1. [<- -5] collides with [2 ->]:
   |-5| > |2| -> [2 ->] explodes!
   Remaining: [10 ->] [<- -5]

2. [<- -5] collides with [10 ->]:
   |-5| < |10| -> [<- -5] explodes!
   Remaining: [10 ->]

Result: [10]
```

---

## Alternative Solutions

### Vector Erase Simulation (Brute Force)
- Repeatedly scan adjacent pairs for `res[i] > 0 && res[i+1] < 0` and erase smaller asteroid using `res.erase()`.
- **Time Complexity**: $\mathcal{O}(N^2)$.
- **Space Complexity**: $\mathcal{O}(N)$.

---

## Edge Cases

1. **No Collisions**: `[-2, -1, 1, 2]` -> All moving away from each other $\implies$ Returns `[-2, -1, 1, 2]`.
2. **All Asteroids Explode**: `[8, -8]` -> Returns `[]`.
3. **Chain Reaction Elimination**: `[10, 5, 2, -20]` -> `-20` destroys `2`, `5`, and `10` $\implies$ Returns `[-20]`.

---

## Interview Tips

- **Explain Collision Condition Precision**: State *"A collision can ONLY happen when `st.back() > 0` (moving right) and `ast < 0` (moving left). If `st.back() < 0` and `ast > 0`, both asteroids are moving away from each other, so no collision is possible."*

---

## Similar Problems

1. [LeetCode #739: Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)
2. [LeetCode #1047: Remove All Adjacent Duplicates In String](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/)
3. [LeetCode #2211: Count Collisions on a Road](https://leetcode.com/problems/count-collisions-on-a-road/)

---

## Revision Notes

- Problem: Asteroid collision state.
- Pattern: Stack (`vector<int> st`).
- Loop `int ast` in `asteroids`:
  - `bool alive = true;`
  - `while (alive && !st.empty() && st.back() > 0 && ast < 0)`:
    - `if (st.back() < -ast) st.pop_back();`
    - `else if (st.back() == -ast) st.pop_back(), alive = false;`
    - `else alive = false;`
  - `if (alive) st.push_back(ast);`
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(N)$.
