# Find the Smallest Divisor Given a Threshold

- **Problem Number**: 1283
- **Platform**: LeetCode #1283
- **Difficulty**: Medium
- **Pattern**: Linear Search on Divisors

---

## Brute Force Intuition

Test every divisor $d$ starting from $1$ up to $\max(\text{nums})$. For each candidate divisor $d$, compute the sum of rounded divisions:
$$\text{sum}(d) = \sum_{i=0}^{n-1} \lceil \text{nums}[i] / d \rceil = \sum_{i=0}^{n-1} \frac{\text{nums}[i] + d - 1}{d}$$

Return the first divisor $d$ for which $\text{sum}(d) \le \text{threshold}$.

---

## Algorithm

1. `max_val = max(nums)`.
2. Loop `d` from `1` to `max_val`:
   a. `current_sum = 0`.
   b. For each `x` in `nums`:
      - `current_sum += (x + d - 1) / d`.
   c. If `current_sum <= threshold`, return `d`.
3. Return `max_val`.

---

## Code

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    int smallestDivisor(const std::vector<int>& nums, int threshold) {
        int max_val = *std::max_element(nums.begin(), nums.end());
        
        for (int d = 1; d <= max_val; ++d) {
            long long current_sum = 0;
            for (int x : nums) {
                current_sum += (x + d - 1) / d;
            }
            if (current_sum <= threshold) {
                return d;
            }
        }
        
        return max_val;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(M \times N)$
  - Where $M = \max(\text{nums})$ and $N = \text{nums.length}$.
  - For $M = 10^6$ and $N = 5 \times 10^4$, total operations equal $5 \times 10^{10}$, causing TLE.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Constant auxiliary space.

---

## Why This Approach Is Not Optimal

Testing all divisors linearly takes $\mathcal{O}(M \times N)$ time. Because the division sum function is **monotonically decreasing** with respect to the divisor (increasing $d$ decreases the sum), we can apply **Binary Search on Answer Space** in logarithmic $\mathcal{O}(N \log M)$ time.
