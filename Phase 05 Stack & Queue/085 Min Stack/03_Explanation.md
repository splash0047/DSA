# Problem Summary

Design a stack data structure supporting `push`, `pop`, `top`, and `getMin` in $\mathcal{O}(1)$ time for each operation. The optimal approach uses a **Pair Stack** `std::stack<pair<int, int>>` where each entry stores `{value, min_so_far}`:
- `push(val)`: Stores `{val, min(val, st.top().second)}`.
- `pop()`: Pops top pair.
- `top()`: Returns `st.top().first`.
- `getMin()`: Returns `st.top().second`.
This achieves $\mathcal{O}(1)$ time for all operations and $\mathcal{O}(N)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to design a **stack / queue variant** that tracks running minimum / maximum in $\mathcal{O}(1)$ time.
- Pair Stack / Running Min-Max Tracking pattern.

---

## Important Clues

1. **"Retrieve minimum element in constant time O(1)"**: Running minimum tracking requirement.
2. **"Stack operations push, pop, top"**: LIFO structure.

---

## Example

### Input Operations
`push(-2)`, `push(0)`, `push(-3)`, `getMin()`, `pop()`, `getMin()`

### Visual Step-by-Step Progression

```text
push(-2) -> Stack: [ {-2, -2} ]               getMin() = -2
push(0)  -> Stack: [ {-2, -2}, {0, -2} ]       getMin() = -2
push(-3) -> Stack: [ {-2, -2}, {0, -2}, {-3, -3} ] getMin() = -3

pop()    -> Stack: [ {-2, -2}, {0, -2} ]       getMin() = -2
```

---

## Alternative Solutions

### Two Separate Stacks (O(1) Time, O(N) Space)
- Primary stack `val_st` stores values. Auxiliary stack `min_st` stores minimums (`min_st.push(val)` when `val <= min_st.top()`).
- **Time Complexity**: $\mathcal{O}(1)$.
- **Space Complexity**: $\mathcal{O}(N)$.

---

## Edge Cases

1. **Pushing Duplicates of Minimum**: `push(-2)`, `push(-2)` -> Stack correctly maintains `min_so_far = -2` at both levels.
2. **Pushing Negative Values**: `push(INT_MIN)` -> Handled safely without overflow.
3. **Empty Stack Initial Push**: Checks `st.empty()` to set initial `min_so_far = val`.

---

## Interview Tips

- **Explain Why Pair Stack Prevents Integer Overflow**: State *"While single-stack mathematical formulas like pushing `2 * val - min` achieve $\mathcal{O}(1)$ space optimization, they risk 32-bit integer overflow when values approach `INT_MIN` or `INT_MAX`. The Pair Stack `{val, min_so_far}` approach is overflow-safe and production-ready."*

---

## Similar Problems

1. [LeetCode #239: Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)
2. [LeetCode #716: Max Stack](https://leetcode.com/problems/max-stack/)
3. [LeetCode #84: Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)

---

## Revision Notes

- Problem: Design MinStack with $\mathcal{O}(1)$ `getMin()`.
- Pattern: Pair Stack `stack<pair<int, int>>` storing `{val, min_so_far}`.
- `push(val)`: `curr_min = st.empty() ? val : min(val, st.top().second); st.push({val, curr_min});`.
- `pop()`: `st.pop();`.
- `top()`: `return st.top().first;`.
- `getMin()`: `return st.top().second;`.
- Optimal Complexity: Time $\mathcal{O}(1)$, Space $\mathcal{O}(N)$.
