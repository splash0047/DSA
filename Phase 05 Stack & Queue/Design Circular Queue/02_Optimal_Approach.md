# Design Circular Queue - Optimal Approach (Fixed Ring Buffer)

- **Problem Number**: 622
- **Platform**: LeetCode #622
- **Difficulty**: Medium
- **Pattern**: Ring Buffer with Modulo Index Arithmetic ($\mathcal{O}(1)$)

```cpp
#include <vector>

class MyCircularQueue {
    std::vector<int> buffer;
    int head, tail, count, capacity;
public:
    MyCircularQueue(int k) : buffer(k), head(0), tail(0), count(0), capacity(k) {}

    bool enQueue(int value) {
        if (isFull()) return false;
        buffer[tail] = value;
        tail = (tail + 1) % capacity;
        count++;
        return true;
    }

    bool deQueue() {
        if (isEmpty()) return false;
        head = (head + 1) % capacity;
        count--;
        return true;
    }

    int Front() { return isEmpty() ? -1 : buffer[head]; }
    int Rear() { return isEmpty() ? -1 : buffer[(tail - 1 + capacity) % capacity]; }
    bool isEmpty() { return count == 0; }
    bool isFull() { return count == capacity; }
};
```
