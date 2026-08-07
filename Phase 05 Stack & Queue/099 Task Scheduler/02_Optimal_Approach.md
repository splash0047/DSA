# Task Scheduler

## Pattern Used

- **Pattern**: **Greedy Slot Formula / Frequency Frame Counting**
- **Concept**:
  1. Find the maximum task frequency `max_freq` among all tasks.
  2. Count how many tasks share this maximum frequency (`max_freq_count`).
  3. The most frequent task(s) partition the CPU schedule into `(max_freq - 1)` frames of size `(n + 1)`.
  4. Minimum intervals required by formula:
     $$\text{frame\_intervals} = (\text{max\_freq} - 1) \times (n + 1) + \text{max\_freq\_count}$$
  5. The actual answer is $\max(\text{tasks.size()}, \text{frame\_intervals})$.

---

## Observation

1. Why frame calculation works:
   - Suppose most frequent task `'A'` appears 3 times with $n = 2$.
   - Frame Layout: `A _ _ | A _ _ | A` $\implies 2$ chunks of size $(2 + 1) = 3$, plus final `A` $\implies (3 - 1) \times (2 + 1) + 1 = 7$.
   - Other lower-frequency tasks (`B`, `C`, etc.) can be placed into empty `_` slots without extending the total length!
2. If there are so many tasks that all idle `_` slots are filled without any idle intervals, then total time is simply `tasks.size()`.
3. Thus, `ans = max((int)tasks.size(), frame_intervals)`.

---

## Intuition

The task with the maximum frequency imposes the fundamental bottleneck structure. Arrange the most frequent tasks into frames separated by $n$ slots, then fill remaining empty slots with other tasks.

---

## Algorithm

1. Frequency array `freq[26] = {0}`.
2. Count task frequencies. Find `max_freq`.
3. Count how many tasks have `freq == max_freq` (`max_freq_count`).
4. `frame_intervals = (max_freq - 1) * (n + 1) + max_freq_count`.
5. Return `max((int)tasks.size(), frame_intervals)`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    int leastInterval(const std::vector<char>& tasks, int n) {
        int freq[26] = {0};
        for (char t : tasks) {
            freq[t - 'A']++;
        }
        
        int max_freq = 0;
        for (int count : freq) {
            max_freq = std::max(max_freq, count);
        }
        
        int max_freq_count = 0;
        for (int count : freq) {
            if (count == max_freq) {
                max_freq_count++;
            }
        }
        
        int frame_intervals = (max_freq - 1) * (n + 1) + max_freq_count;
        
        return std::max(static_cast<int>(tasks.size()), frame_intervals);
    }
};
```

---

## Dry Run

### Input
- `tasks = ["A","A","A","B","B","B"]`, `n = 2`

### Execution Trace

1. Frequencies: `A: 3`, `B: 3`.
2. `max_freq = 3`.
3. Tasks with `freq == 3`: `A` and `B` $\implies$ `max_freq_count = 2`.
4. `frame_intervals = (3 - 1) * (2 + 1) + 2 = 2 * 3 + 2 = 8`.
5. `tasks.size() = 6`.
6. `max(6, 8) = 8`.

### Result
- Output: `8` (`A -> B -> idle -> A -> B -> idle -> A -> B`)

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Single pass over $N$ tasks to build frequency table; operations on fixed 26-element array take $\mathcal{O}(1)$ time.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Constant space using fixed array of size 26.

---

## Why This is Optimal

- Computes minimum scheduling intervals mathematically in linear $\mathcal{O}(N)$ time.
- Uses zero auxiliary memory ($\mathcal{O}(1)$ space).

---

## Common Mistakes

1. **Forgetting `max(tasks.size(), frame_intervals)`**: When $n=0$ or when there are many distinct tasks, no idle slots exist. The minimum interval can never be less than `tasks.size()`.
2. **Incorrect `max_freq_count`**: Forgetting to count ALL tasks that tie for maximum frequency.
