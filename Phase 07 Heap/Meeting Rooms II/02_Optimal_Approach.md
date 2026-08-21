# Meeting Rooms II - Optimal Approach (Min-Heap / Chronological Line Sweep)

- **Problem Number**: 253
- **Pattern**: Min-Heap of Active End Times / Two Pointers on Sorted Starts & Ends

```cpp
#include <vector>
#include <queue>
#include <algorithm>

class Solution {
public:
    int minMeetingRooms(std::vector<std::vector<int>>& intervals) {
        if (intervals.empty()) return 0;
        std::sort(intervals.begin(), intervals.end());

        std::priority_queue<int, std::vector<int>, std::greater<int>> min_heap;
        min_heap.push(intervals[0][1]);

        for (size_t i = 1; i < intervals.size(); i++) {
            if (intervals[i][0] >= min_heap.top()) {
                min_heap.pop(); // Room freed up
            }
            min_heap.push(intervals[i][1]); // Allocate room
        }
        return min_heap.size();
    }
};
```
