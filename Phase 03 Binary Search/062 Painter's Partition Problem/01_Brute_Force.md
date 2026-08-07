# Painter's Partition Problem

- **Problem Number**: GFG Painter's Partition
- **Platform**: GeeksforGeeks
- **Difficulty**: Hard
- **Pattern**: Linear Search on Time Limits

---

## Brute Force Intuition

Test every possible maximum time limit $T$ starting from $\max(\text{arr})$ up to $\sum \text{arr}$. For each time limit $T$, simulate assigning boards to painters sequentially:
- Assign contiguous boards to current painter until adding next board exceeds $T$.
- Increment painter count.
- If total painters needed $\le k$, return $T$.

---

## Algorithm

1. `low = max(arr)`, `high = sum(arr)`.
2. Loop time `t` from `low` to `high`:
   a. `painters = 1`, `current_time = 0`.
   b. For each `b` in `arr`:
      - If `current_time + b > t`:
        - `painters++`.
        - `current_time = b`.
      - Else: `current_time += b`.
   c. If `painters <= k`, return `t`.
3. Return `high`.

---

## Code

```cpp
#include <vector>
#include <numeric>
#include <algorithm>

class Solution {
public:
    long long minTime(const std::vector<int>& arr, int k) {
        long long low = *std::max_element(arr.begin(), arr.end());
        long long high = std::accumulate(arr.begin(), arr.end(), 0LL);
        
        for (long long t = low; t <= high; ++t) {
            int painters = 1;
            long long current_time = 0;
            
            for (int b : arr) {
                if (current_time + b > t) {
                    painters++;
                    current_time = b;
                } else {
                    current_time += b;
                }
            }
            
            if (painters <= k) {
                return t;
            }
        }
        
        return high;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}((\sum \text{arr} - \max(\text{arr})) \times N)$
  - Testing each time limit takes $\mathcal{O}(N)$ simulation time.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Constant auxiliary space.

---

## Why This Approach Is Not Optimal

Linear search over time limits takes $\mathcal{O}((\sum \text{arr} - \max(\text{arr})) \times N)$ time. Because painter assignment `canPaint(time)` is **monotonic**, we can apply **Binary Search on Answer Space** in $\mathcal{O}(N \log(\sum \text{arr}))$ time.
