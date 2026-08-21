# 04 Interview Follow-ups & System Variations: Implement Stack using Queues

The problem implements a LIFO Stack using FIFO Queues. Optimal approaches use 1 Queue (rotating elements on push) in $\mathcal{O}(N)$ push and $\mathcal{O}(1)$ pop, or 2 Queues.

In technical interviews, this problem is contrasted with Queue using Stacks to demonstrate why no amortized $\mathcal{O}(1)$ pop exists for Queues.

---

## 1. Single Queue Implementation (Push Rotation)

```cpp
class MyStack {
    queue<int> q;
public:
    void push(int x) {
        q.push(x);
        int sz = q.size();
        for (int i = 0; i < sz - 1; i++) {
            q.push(q.front());
            q.pop(); // Rotate old elements behind the new top
        }
    }
    int pop() { int v = q.front(); q.pop(); return v; }
    int top() { return q.front(); }
    bool empty() { return q.empty(); }
};
```

---

## Summary Matrix: Trade-offs at a Glance

| Design | Push Time | Pop Time | Top Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **Push-Costly (1 Queue)**| $\mathcal{O}(N)$ | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ | $\mathcal{O}(N)$ |
| **Pop-Costly (2 Queues)** | $\mathcal{O}(1)$ | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
