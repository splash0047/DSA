# Implement Queue using Stacks

## Pattern Used

- **Pattern**: **Lazy Two-Stack In/Out Transfer (Amortized O(1))**
- **Concept**: Maintain two stacks: `in_st` (for `push` operations) and `out_st` (for `pop` / `peek` operations).
  - `push(x)`: Always push `x` directly onto `in_st` in $\mathcal{O}(1)$ time.
  - `pop()` / `peek()`:
    - If `out_st` is empty, transfer ALL elements from `in_st` into `out_st` (which reverses their order, making `out_st.top()` the front of the FIFO queue!).
    - Perform `pop()` / `peek()` directly from `out_st.top()`.

---

## Observation

1. Reversing a reverse gives the original order!
   - `in_st` stores elements in LIFO order (newest at top).
   - Transferring from `in_st` to `out_st` flips the elements so that `out_st` stores elements in FIFO order (oldest at top)!
2. Amortized $\mathcal{O}(1)$ Analysis: Each element is pushed to `in_st` once, transferred to `out_st` once, and popped from `out_st` once. Over $N$ operations, total cost is $\mathcal{O}(N)$, giving an **amortized time of $\mathcal{O}(1)$ per operation**.

---

## Intuition

Decouple insertion (`in_st`) and deletion (`out_st`). Only transfer elements from `in_st` to `out_st` when `out_st` is completely empty.

---

## Algorithm

1. Primary Stacks: `stack<int> in_st`, `stack<int> out_st`.
2. `push(x)`:
   - `in_st.push(x)`.
3. `transfer()` helper:
   - If `out_st.empty()`:
     - While `!in_st.empty()`: `out_st.push(in_st.top()); in_st.pop();`.
4. `pop()`:
   - `transfer()`.
   - `val = out_st.top()`, `out_st.pop()`, `return val`.
5. `peek()`:
   - `transfer()`.
   - `return out_st.top()`.
6. `empty()`:
   - `return in_st.empty() && out_st.empty()`.

---

## Clean C++17 Solution

```cpp
#include <stack>

class MyQueue {
private:
    std::stack<int> in_st;
    std::stack<int> out_st;
    
    void transfer() {
        if (out_st.empty()) {
            while (!in_st.empty()) {
                out_st.push(in_st.top());
                in_st.pop();
            }
        }
    }

public:
    MyQueue() {}
    
    void push(int x) {
        in_st.push(x);
    }
    
    int pop() {
        transfer();
        int val = out_st.top();
        out_st.pop();
        return val;
    }
    
    int peek() {
        transfer();
        return out_st.top();
    }
    
    bool empty() {
        return in_st.empty() && out_st.empty();
    }
};
```

---

## Dry Run

### Input Operations
`push(1)`, `push(2)`, `peek()`, `pop()`, `empty()`

### Execution Trace

1. `push(1)`: `in_st = [1]`, `out_st = []`
2. `push(2)`: `in_st = [1, 2]`, `out_st = []`
3. `peek()`: `out_st` is empty $\implies$ transfer `in_st` to `out_st`.
   - `in_st = []`, `out_st = [2, 1]` (top is 1).
   - Return `out_st.top()` = `1`.
4. `pop()`: `out_st` is not empty. Pop `out_st.top()`.
   - `out_st = [2]`. Return `1`.
5. `empty()`: `in_st` empty? (Yes), `out_st` empty? (No, has 2) $\implies$ Return `false`.

---

## Time Complexity

- **`push(x)`**: $\mathcal{O}(1)$ strict.
- **`pop()` / `peek()`**: $\mathcal{O}(1)$ amortized.
- **`empty()`**: $\mathcal{O}(1)$ strict.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Stores $N$ elements across two stacks.

---

## Why This is Optimal

- Meets the follow-up requirement for **amortized $\mathcal{O}(1)$ time complexity** across all operations.
- Avoids unnecessary transfer loops when `out_st` already has elements.

---

## Common Mistakes

1. **Transferring Every Call**: Transferring `in_st` to `out_st` on every `pop()` even when `out_st` is non-empty, which corrupts the element order! Transfer MUST only occur `if (out_st.empty())`.
2. **Incorrect `empty()` Check**: Returning only `in_st.empty()`. Queue is empty ONLY when BOTH `in_st` and `out_st` are empty.
