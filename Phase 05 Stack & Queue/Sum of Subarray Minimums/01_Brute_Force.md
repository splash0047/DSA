# Sum of Subarray Minimums - Brute Force

- **Problem Number**: 907
- **Platform**: LeetCode #907
- **Difficulty**: Medium
- **Pattern**: Double Loop Subarray Minimum Accumulation

---

## Algorithm

For each start index $i$, find minimum for all subarrays ending at $j \ge i$ and sum them up.

---

## Code

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    int sumSubarrayMins(std::vector<int>& arr) {
        long long total = 0;
        int MOD = 1e9 + 7;
        int n = arr.size();

        for (int i = 0; i < n; i++) {
            int current_min = arr[i];
            for (int j = i; j < n; j++) {
                current_min = std::min(current_min, arr[j]);
                total = (total + current_min) % MOD;
            }
        }
        return total;
    }
};
```

---

## Time & Space Complexity

- **Time Complexity**: $\mathcal{O}(N^2)$
- **Space Complexity**: $\mathcal{O}(1)$
