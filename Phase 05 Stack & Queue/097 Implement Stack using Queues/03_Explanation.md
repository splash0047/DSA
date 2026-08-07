# Problem Summary

Implement a LIFO stack using queues. The optimal approach satisfies the follow-up requirement using **ONLY ONE Queue**:
- `push(x)`: Append `x` to `q`, then rotate the preceding `sz` elements to the back of `q` (`q.push(q.front()); q.pop();`). This brings `x` directly to `q.front()`.
- `pop()`: Pop from `q.front()` in $\mathcal{O}(1)$ time.
- `top()`: Access `q.front()` in $\mathcal{O}(1)$ time.
- `empty()`: Return `q.empty()` in $\mathcal{O}(1)$ time.
This achieves single-queue LIFO simulation with $\mathcal{O}(N)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to **simulate LIFO Stack using ONLY 1 FIFO Queue**.
- Single Queue In-Place Rotation pattern.

---

## Important Clues

1. **"Implement stack using queues"**: Queue Stack simulation.
2. **"Can you implement the stack using only one queue? follow-up"**: Single queue rotation pattern.

---

## Example

### Input Operations
`push(1)`, `push(2)`, `top()`, `pop()`, `empty()`

### Visual Step-by-Step Progression

```text
Single Queue State Evolution:

1. push(1) -> q: [1]
2. push(2) -> Append 2: [1, 2] -> Rotate 1 element -> q: [2, 1]
3. top()   -> q.front() = 2
4. pop()   -> Pop front (2) -> q: [1] -> Return 2
5. empty() -> q.empty() = false
```

---

## Alternative Solutions

### Two Queues Push-Heavy Approach
- Maintain `q1` and `q2`. Insert `x` into `q2`, copy all elements from `q1` to `q2`, and swap.
- **Time Complexity**: `push` $\mathcal{O}(N)$, `pop` $\mathcal{O}(1)$.
- **Space Complexity**: $\mathcal{O}(N)$ (Requires 2 Queues).

---

## Edge Cases

1. **Single Push**: `sz = 0`, no rotation performed.
2. **Multiple Consecutive Pushes**: Every push brings new element to `q.front()`.

---

## Interview Tips

- **Highlight Single Queue Follow-up Advantage**: State *"Using single-queue rotation on `push(x)` eliminates the need for a secondary auxiliary queue. By rotating the preceding $N$ elements behind the newly pushed item $x$, we maintain $x$ at `q.front()` for instant $\mathcal{O}(1)$ `pop` and `top` access."*

---

## Similar Problems

1. [LeetCode #232: Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)
2. [LeetCode #155: Min Stack](https://leetcode.com/problems/min-stack/)

---

## Revision Notes

- Problem: Implement LIFO Stack using 1 Queue.
- Pattern: Single Queue Rotation (`std::queue<int> q`).
- `push(x)`:
  - `sz = q.size(); q.push(x);`
  - `for (i = 0; i < sz; ++i) q.push(q.front()), q.pop();`
- `pop()`: `val = q.front(); q.pop(); return val;`.
- `top()`: `return q.front();`.
- `empty()`: `return q.empty();`.
- Optimal Complexity: `push` $\mathcal{O}(N)$, `pop`/`top` $\mathcal{O}(1)$, Space $\mathcal{O}(N)$ (1 Queue).
