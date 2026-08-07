# Koko Eating Bananas

- **Problem Number**: 875
- **Platform**: LeetCode #875
- **Difficulty**: Medium
- **Pattern**: Linear Search on Answer Space

---

## Brute Force Intuition

Test every possible eating speed $k$ starting from $1$ up to $\max(\text{piles})$. For each speed $k$, compute the total hours required to finish all piles:
$$\text{hours}(k) = \sum_{i=0}^{n-1} \lceil \text{piles}[i] / k \rceil = \sum_{i=0}^{n-1} \frac{\text{piles}[i] + k - 1}{k}$$

Return the very first speed $k$ for which $\text{hours}(k) \le h$.

---

## Algorithm

1. `max_pile = max(piles)`.
2. Loop speed $k$ from `1` to `max_pile`:
   a. `total_hours = 0`.
   b. For each `pile` in `piles`:
      - `total_hours += (pile + k - 1) / k`.
   c. If `total_hours <= h`, return `k`.
3. Return `max_pile`.

---

## Code

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    int minEatingSpeed(const std::vector<int>& piles, int h) {
        int max_pile = *std::max_element(piles.begin(), piles.end());
        
        for (int k = 1; k <= max_pile; ++k) {
            long long total_hours = 0;
            for (int pile : piles) {
                total_hours += (pile + k - 1LL) / k;
            }
            if (total_hours <= h) {
                return k;
            }
        }
        
        return max_pile;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(M \times N)$
  - Where $M = \max(\text{piles})$ and $N = \text{piles.length}$.
  - For $M = 10^9$ and $N = 10^4$, total operations equal $10^{13}$, causing severe TLE.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Constant auxiliary space.

---

## Why This Approach Is Not Optimal

Testing all speeds linearly takes $\mathcal{O}(M \times N)$ time. Because the feasibility function $\text{canFinish}(k)$ is **monotonic** (if Koko can finish at speed $K$, she can also finish at any speed $> K$), we can apply **Binary Search on Answer Space** in logarithmic $\mathcal{O}(N \log M)$ time.
