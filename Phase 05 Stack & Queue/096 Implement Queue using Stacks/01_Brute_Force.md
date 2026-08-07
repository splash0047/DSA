# Implement Queue using Stacks

- **Problem Number**: 232
- **Platform**: LeetCode #232
- **Difficulty**: Easy
- **Pattern**: Push Heavy (Transfer on Push)

---

## Brute Force Intuition

Maintain two stacks `s1` and `s2`.
- When `push(x)` is called:
  - Transfer all elements from `s1` into `s2`.
  - Push `x` onto `s1`.
  - Transfer all elements back from `s2` into `s1`.
  - Now `s1.top()` is ALWAYS the front element of the queue!
- `pop()`, `peek()`, and `empty()` run in $\mathcal{O}(1)$ time by operating directly on `s1.top()`.

---

## Algorithm

1. `push(x)`:
   - While `!s1.empty()`: `s2.push(s1.top())`, `s1.pop()`.
   - `s1.push(x)`.
   - While `!s2.empty()`: `s1.push(s2.top())`, `s2.pop()`.
2. `pop()`:
   - `val = s1.top()`, `s1.pop()`, `return val`.
3. `peek()`:
   - `return s1.top()`.
4. `empty()`:
   - `return s1.empty()`.

---

## Code

```cpp
#include <stack>

class MyQueue {
private:
    std::stack<int> s1;
    std::stack<int> s2;
public:
    MyQueue() {}
    
    void push(int x) {
        while (!s1.empty()) {
            s2.push(s1.top());
            s1.pop();
        }
        s1.push(x);
        while (!s2.empty()) {
            s1.push(s2.top());
            s2.pop();
        }
    }
    
    int pop() {
        int val = s1.top();
        s1.pop();
        return val;
    }
    
    int peek() {
        return s1.top();
    }
    
    bool empty() {
        return s1.empty();
    }
};
```

---

## Time Complexity

- **`push(x)`**: $\mathcal{O}(N)$
  - Transfers all $N$ elements twice on every push.
- **`pop()` / `peek()` / `empty()`**: $\mathcal{O}(1)$

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Stores $N$ elements across two stacks.

---

## Why This Approach Is Not Optimal

Every `push` call forces an $\mathcal{O}(N)$ element transfer. Using **Lazy Transfer (Amortized $\mathcal{O}(1)$ Stacks)**, we achieve amortized $\mathcal{O}(1)$ time for ALL operations.
