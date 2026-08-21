# Design Circular Queue - Brute Force (Dynamic Array / Vector Pop Front)

- **Problem Number**: 622
- **Platform**: LeetCode #622
- **Difficulty**: Medium
- **Pattern**: Dynamic Array Simulation ($\mathcal{O}(N)$ Dequeue)

```cpp
#include <vector>

class MyCircularQueue {
    std::vector<int> data;
    int k;
public:
    MyCircularQueue(int k) : k(k) {}
    bool enQueue(int value) {
        if (data.size() == k) return false;
        data.push_back(value);
        return true;
    }
    bool deQueue() {
        if (data.empty()) return false;
        data.erase(data.begin()); // O(N) shifting!
        return true;
    }
    int Front() { return data.empty() ? -1 : data.front(); }
    int Rear() { return data.empty() ? -1 : data.back(); }
    bool isEmpty() { return data.empty(); }
    bool isFull() { return data.size() == k; }
};
```
