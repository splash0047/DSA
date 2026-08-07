# Problem Summary

Implement a FIFO queue using only two standard stacks (`push`, `peek`, `pop`, `empty`). The optimal approach uses **Lazy Two-Stack In/Out Transfer**:
- `in_st`: Receives incoming `push(x)` elements in $\mathcal{O}(1)$ time.
- `out_st`: Serves `pop()` and `peek()` operations.
- When `out_st` is empty, transfer all elements from `in_st` into `out_st` (reversing LIFO into FIFO order!).
This achieves amortized $\mathcal{O}(1)$ time for all queue operations and $\mathcal{O}(N)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to **simulate FIFO Queue using LIFO Stacks** in amortized $\mathcal{O}(1)$ time.
- Lazy Two-Stack In/Out Transfer pattern.

---

## Important Clues

1. **"Implement FIFO queue using two stacks"**: Dual Stack Queue simulation.
2. **"Amortized O(1) time complexity follow-up"**: Lazy transfer on `out_st` depletion.

---

## Example

### Input Operations
`push(1)`, `push(2)`, `peek()`, `pop()`, `empty()`

### Visual Step-by-Step Progression

```text
1. push(1) -> in_st: [1], out_st: []
2. push(2) -> in_st: [1, 2], out_st: []
3. peek()  -> out_st empty -> Transfer in_st to out_st:
              in_st: [], out_st: [2, 1] (top is 1)
              Return out_st.top() = 1
4. pop()   -> out_st.pop() -> out_st: [2] -> Return 1
5. empty() -> in_st.empty() && out_st.empty() -> Return false
```

---

## Alternative Solutions

### Push-Heavy Transfer (O(N) Push, O(1) Pop)
- Transfer `s1` to `s2` on every `push`, insert element, then transfer back to `s1`.
- **Time Complexity**: `push` $\mathcal{O}(N)$, `pop` $\mathcal{O}(1)$.
- **Space Complexity**: $\mathcal{O}(N)$.

---

## Edge Cases

1. **Interleaved Push and Pop Operations**: Handled seamlessly because `out_st` retains elements until depleted before pulling next batch from `in_st`.
2. **Queue Emptied and Refilled**: `empty()` correctly checks `in_st.empty() && out_st.empty()`.

---

## Interview Tips

- **Explain Amortized Complexity Proof**: State *"Each element is pushed to `in_st` ONCE, moved to `out_st` ONCE, and popped from `out_st` ONCE. Across $N$ operations, total work is $3N$ steps, giving an overall amortized cost of $\mathcal{O}(1)$ per operation."*

---

## Similar Problems

1. [LeetCode #225: Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/)
2. [LeetCode #155: Min Stack](https://leetcode.com/problems/min-stack/)

---

## Revision Notes

- Problem: Implement FIFO Queue using 2 Stacks.
- Pattern: `in_st` and `out_st` (Lazy Transfer).
- `push(x)`: `in_st.push(x)`.
- `transfer()`: `if (out_st.empty()) while(!in_st.empty()) out_st.push(in_st.top()), in_st.pop();`.
- `pop()`: `transfer(); val = out_st.top(); out_st.pop(); return val;`.
- `peek()`: `transfer(); return out_st.top();`.
- `empty()`: `return in_st.empty() && out_st.empty();`.
- Optimal Complexity: Amortized Time $\mathcal{O}(1)$, Space $\mathcal{O}(N)$.
