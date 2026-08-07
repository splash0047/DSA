# Task Scheduler

- **Problem Number**: 621
- **Platform**: LeetCode #621
- **Difficulty**: Medium
- **Pattern**: Max-Heap & Cooling Queue Simulation

---

## Brute Force Intuition

Simulate CPU scheduling cycle by cycle using a Max-Heap `std::priority_queue<int> max_heap` and a Cooling Queue `std::queue<pair<int, int>> cool_queue` (`{count, available_time}`):
- Count task frequencies into a frequency map.
- Push all non-zero frequencies into `max_heap`.
- Maintain current `time = 0`.
- In each cycle:
  - Increment `time++`.
  - If `max_heap` is non-empty, pop the highest frequency task, decrement its count, and if `count > 0`, push `{count, time + n}` into `cool_queue`.
  - If `cool_queue.front().second == time`, pop from `cool_queue` and push back into `max_heap`.
- Repeat until both `max_heap` and `cool_queue` are empty.

---

## Algorithm

1. Count frequency of each task `'A'..'Z'`.
2. Push non-zero frequencies into `max_heap`.
3. `cool_queue` of `{count, ready_time}` pairs, `time = 0`.
4. While `!max_heap.empty()` or `!cool_queue.empty()`:
   a. `time++`.
   b. If `!max_heap.empty()`:
      - `cnt = max_heap.top() - 1`.
      - `max_heap.pop()`.
      - If `cnt > 0`: `cool_queue.push({cnt, time + n})`.
   c. If `!cool_queue.empty()` and `cool_queue.front().second == time`:
      - `max_heap.push(cool_queue.front().first)`.
      - `cool_queue.pop()`.
5. Return `time`.

---

## Code

```cpp
#include <vector>
#include <queue>
#include <unordered_map>
#include <utility>

class Solution {
public:
    int leastInterval(const std::vector<char>& tasks, int n) {
        std::unordered_map<char, int> counts;
        for (char t : tasks) {
            counts[t]++;
        }
        
        std::priority_queue<int> max_heap;
        for (const auto& pair : counts) {
            max_heap.push(pair.second);
        }
        
        // {remaining_count, ready_time}
        std::queue<std::pair<int, int>> cool_queue;
        int time = 0;
        
        while (!max_heap.empty() || !cool_queue.empty()) {
            time++;
            
            if (!max_heap.empty()) {
                int cnt = max_heap.top() - 1;
                max_heap.pop();
                if (cnt > 0) {
                    cool_queue.push({cnt, time + n});
                }
            }
            
            if (!cool_queue.empty() && cool_queue.front().second == time) {
                max_heap.push(cool_queue.front().first);
                cool_queue.pop();
            }
        }
        
        return time;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(T \log K)$
  - Where $T$ is total output intervals (which can include idle slots) and $K \le 26$ is unique task count.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(K)$
  - Max Heap and Queue store at most $26$ unique task frequencies.

---

## Why This Approach Is Not Optimal

Simulation steps through every single interval (including idle slots), taking $\mathcal{O}(T)$ time. By using **Greedy Frame Calculation**, we can compute the minimum interval count mathematically in $\mathcal{O}(N)$ time with $\mathcal{O}(1)$ space!
