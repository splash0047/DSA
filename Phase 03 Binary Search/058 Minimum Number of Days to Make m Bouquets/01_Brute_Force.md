# Minimum Number of Days to Make m Bouquets

- **Problem Number**: 1482
- **Platform**: LeetCode #1482
- **Difficulty**: Medium
- **Pattern**: Linear Search on Days

---

## Brute Force Intuition

Test every day `day` from $\min(\text{bloomDay})$ to $\max(\text{bloomDay})$. For each candidate day:
- Count how many adjacent bloomed flowers ($\text{bloomDay}[i] \le \text{day}$) are available.
- Form a bouquet whenever adjacent count reaches $k$.
- Return the first day where total formed bouquets $\ge m$.

---

## Algorithm

1. If `(long long)m * k > n`, return `-1`.
2. `min_day = min(bloomDay)`, `max_day = max(bloomDay)`.
3. Loop `day` from `min_day` to `max_day`:
   a. `bouquets = 0`, `count = 0`.
   b. For each `bd` in `bloomDay`:
      - If `bd <= day`:
        - `count++`
        - If `count == k`: `bouquets++`, `count = 0`.
      - Else: `count = 0`.
   c. If `bouquets >= m`, return `day`.
4. Return `-1`.

---

## Code

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    int minDays(const std::vector<int>& bloomDay, int m, int k) {
        int n = bloomDay.size();
        if (1LL * m * k > n) return -1;
        
        int min_day = *std::min_element(bloomDay.begin(), bloomDay.end());
        int max_day = *std::max_element(bloomDay.begin(), bloomDay.end());
        
        for (int day = min_day; day <= max_day; ++day) {
            int bouquets = 0;
            int count = 0;
            
            for (int bd : bloomDay) {
                if (bd <= day) {
                    count++;
                    if (count == k) {
                        bouquets++;
                        count = 0;
                    }
                } else {
                    count = 0;
                }
            }
            
            if (bouquets >= m) {
                return day;
            }
        }
        
        return -1;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(D \times N)$
  - Where $D = \max(\text{bloomDay}) - \min(\text{bloomDay})$ and $N = \text{bloomDay.length}$.
  - For $D = 10^9$ and $N = 10^5$, total operations exceed $10^{14}$, causing TLE.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Constant auxiliary space.

---

## Why This Approach Is Not Optimal

Testing all days linearly takes $\mathcal{O}(D \times N)$ time. Because the predicate function `canMake(day)` is **monotonic** (if $m$ bouquets can be made on day $D$, they can also be made on any day $> D$), we can apply **Binary Search on Answer Space** in logarithmic $\mathcal{O}(N \log(\max D))$ time.
