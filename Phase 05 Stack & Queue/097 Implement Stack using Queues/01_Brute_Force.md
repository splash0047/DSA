# Implement Stack using Queues

- **Problem Number**: 225
- **Platform**: LeetCode #225
- **Difficulty**: Easy
- **Pattern**: Two Queues Push-Heavy Transfer

---

## Brute Force Intuition

Maintain two queues `q1` and `q2`.
- When `push(x)` is called:
  - Push `x` into `q2`.
  - Transfer all elements from `q1` into `q2`.
  - Swap `q1` and `q2`.
  - Now `q1.front()` is ALWAYS the top element of the stack!
- `pop()`, `top()`, and `empty()` run in $\mathcal{O}(1)$ time operating on `q1.front()`.

---

## Algorithm

1. `push(x)`:
   - `q2.push(x)`.
   - While `!q1.empty()`: `q2.push(q1.front())`, `q1.pop()`.
   - Swap `q1` and `q2`.
2. `pop()`:
   - `val = q1.front()`, `q1.pop()`, `return val`.
3. `top()`:
   - `return q1.front()`.
4. `empty()`:
   - `return q1.empty()`.

---

## Code

```cpp
#include <queue>

class MyStack {
private:
    std::queue<int> q1;
    std::queue<int> q2;
public:
    MyStack() {}
    
    void push(int x) {
        q2.push(x);
        while (!q1.empty()) {
            q2.push(q1.front());
            q1.pop();
        }
        std::swap(q1, q2);
    }
    
    int pop() {
        int val = q1.front();
        q1.pop();
        return val;
    }
    
    int top() {
        return q1.front();
    }
    
    bool empty() {
        return q1.empty();
    }
};
```

---

## Time Complexity

- **`push(x)`**: $\mathcal{O}(N)$
  - Transfers all $N$ elements between queues on every push.
- **`pop()` / `top()` / `empty()`**: $\mathcal{O}(1)$

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Stores $N$ elements across two queues.

---

## Why This Approach Is Not Optimal

Requires two separate queues. The problem follow-up asks: **Can you implement the stack using only ONE queue?** By using **Single Queue Rotation**, we can implement LIFO behavior with a single queue.
