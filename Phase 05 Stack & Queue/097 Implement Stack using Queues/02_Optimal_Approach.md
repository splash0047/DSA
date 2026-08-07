# Implement Stack using Queues

## Pattern Used

- **Pattern**: **Single Queue In-Place Rotation**
- **Concept**: Use only **ONE queue** `std::queue<int> q`.
  - `push(x)`:
    1. Record the current queue size `sz = q.size()`.
    2. Push `x` to the back of `q`.
    3. Rotate the first `sz` elements by popping from front and pushing to back (`q.push(q.front()); q.pop();`).
    4. Now `x` (the newly pushed element) is brought to the FRONT of the queue!
  - `pop()`, `top()`, and `empty()` run directly on `q.front()` in $\mathcal{O}(1)$ time.

---

## Observation

1. Rotating `sz` elements inside a single queue moves the newly appended element from the tail of the queue to the front of the queue!
2. `q.front()` becomes the Last-In (most recently pushed) element, giving perfect LIFO stack semantics!
3. Satisfies the follow-up requirement using **only 1 queue**.

---

## Intuition

When pushing a new element, append it to the end of the single queue, then rotate all older elements behind it so that the new element lands at the front.

---

## Algorithm

1. Single Queue: `std::queue<int> q`.
2. `push(x)`:
   - `sz = q.size()`.
   - `q.push(x)`.
   - Loop `sz` times:
     - `q.push(q.front())`.
     - `q.pop()`.
3. `pop()`:
   - `val = q.front()`, `q.pop()`, `return val`.
4. `top()`:
   - `return q.front()`.
5. `empty()`:
   - `return q.empty()`.

---

## Clean C++17 Solution

```cpp
#include <queue>

class MyStack {
private:
    std::queue<int> q;
public:
    MyStack() {}
    
    void push(int x) {
        int sz = q.size();
        q.push(x);
        for (int i = 0; i < sz; ++i) {
            q.push(q.front());
            q.pop();
        }
    }
    
    int pop() {
        int val = q.front();
        q.pop();
        return val;
    }
    
    int top() {
        return q.front();
    }
    
    bool empty() {
        return q.empty();
    }
};
```

---

## Dry Run

### Input Operations
`push(1)`, `push(2)`, `top()`, `pop()`, `empty()`

### Execution Trace

1. `push(1)`: `sz = 0`. `q = [1]`.
2. `push(2)`: `sz = 1`.
   - `q.push(2)` $\implies `q = [1, 2]`.
   - Rotate 1 element: `q.push(1); q.pop();` $\implies `q = [2, 1]`.
3. `top()`: `return q.front()` $\implies$ **`2`**.
4. `pop()`: `val = q.front()` (2), `q.pop()` $\implies `q = [1]`. Return **`2`**.
5. `empty()`: `return q.empty()` $\implies$ **`false`**.

---

## Time Complexity

- **`push(x)`**: $\mathcal{O}(N)$
  - Rotates $N - 1$ elements in single queue.
- **`pop()` / `top()` / `empty()`**: $\mathcal{O}(1)$

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Stores $N$ elements inside 1 queue.

---

## Why This is Optimal

- Fully satisfies the follow-up requirement by using **only 1 queue**.
- Guarantees $\mathcal{O}(1)$ time for `pop`, `top`, and `empty`.

---

## Common Mistakes

1. **Rotating `sz + 1` Times**: Rotating `q.size()` after pushing instead of recorded size `sz` before pushing, which accidentally leaves the element at the back again!
2. **Using Two Queues Unnecessarily**: Overcomplicating the design with two queues when single queue rotation is cleaner and satisfies follow-up.
