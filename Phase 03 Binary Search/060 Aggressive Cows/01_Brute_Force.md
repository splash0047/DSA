# Aggressive Cows

- **Problem Number**: SPOJ AGGRCOW / GFG
- **Platform**: SPOJ / GeeksforGeeks
- **Difficulty**: Medium
- **Pattern**: Linear Search on Distance Space

---

## Brute Force Intuition

Sort `stalls` in ascending order. Test every possible minimum distance $d$ starting from $1$ up to $(\text{stalls}[n-1] - \text{stalls}[0])$. For each distance $d$, attempt to place $k$ cows greedily:
- Place 1st cow at `stalls[0]`.
- Place subsequent cows at the next stall `stalls[i]` such that `stalls[i] - last_placed >= d`.
- If we successfully place $\ge k$ cows, $d$ is valid.
- Return the maximum valid distance $d$.

---

## Algorithm

1. Sort `stalls`.
2. `max_dist = stalls[n - 1] - stalls[0]`.
3. Loop distance `d` from `1` to `max_dist`:
   a. `cows_placed = 1`, `last_pos = stalls[0]`.
   b. For `i` from `1` to `n - 1`:
      - If `stalls[i] - last_pos >= d`:
        - `cows_placed++`.
        - `last_pos = stalls[i]`.
   c. If `cows_placed < k`: return `d - 1`.
4. Return `max_dist`.

---

## Code

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    int aggressiveCows(std::vector<int>& stalls, int k) {
        std::sort(stalls.begin(), stalls.end());
        int n = stalls.size();
        int max_dist = stalls[n - 1] - stalls[0];
        
        for (int d = 1; d <= max_dist; ++d) {
            int cows_placed = 1;
            int last_pos = stalls[0];
            
            for (int i = 1; i < n; ++i) {
                if (stalls[i] - last_pos >= d) {
                    cows_placed++;
                    last_pos = stalls[i];
                }
            }
            
            if (cows_placed < k) {
                return d - 1;
            }
        }
        
        return max_dist;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N \log N + (\text{max\_dist} \times N))$
  - Sorting takes $\mathcal{O}(N \log N)$.
  - Testing each distance $d$ takes $\mathcal{O}(N)$ simulation time.
  - For $\text{max\_dist} = 10^9$, this causes TLE.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$ auxiliary space.

---

## Why This Approach Is Not Optimal

Testing all distances linearly takes $\mathcal{O}(\text{max\_dist} \times N)$ time. Because the cow placement feasibility function `canPlace(distance)` is **monotonic** (if $k$ cows can be placed with distance $D$, they CANNOT be placed with any distance $> D$ once $D$ becomes too large), we can apply **Binary Search on Answer Space** in $\mathcal{O}(N \log(\text{max\_dist}))$ time.
