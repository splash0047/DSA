# Asteroid Collision

- **Problem Number**: 735
- **Platform**: LeetCode #735
- **Difficulty**: Medium
- **Pattern**: Vector Simulation Loop

---

## Brute Force Intuition

Simulate collision passes over a `std::vector<int> res`. In each pass, scan adjacent elements `res[i]` and `res[i+1]`. If `res[i] > 0` (moving right) and `res[i+1] < 0` (moving left), a collision occurs! Resolve the collision according to size rules (erase the smaller element or both if equal) and restart scanning. Repeat until no adjacent colliding pairs remain.

---

## Algorithm

1. `res = asteroids`.
2. Loop indefinitely:
   a. `collided = false`.
   b. For `i` from `0` to `res.size() - 2`:
      - If `res[i] > 0 && res[i+1] < 0`:
        - `collided = true`.
        - If `abs(res[i]) > abs(res[i+1])`: erase `res[i+1]`.
        - Else if `abs(res[i]) < abs(res[i+1])`: erase `res[i]`.
        - Else: erase both `res[i]` and `res[i+1]`.
        - Break inner loop.
   c. If `!collided`: break outer loop.
3. Return `res`.

---

## Code

```cpp
#include <vector>
#include <cmath>

class Solution {
public:
    std::vector<int> asteroidCollision(std::vector<int>& asteroids) {
        std::vector<int> res = asteroids;
        
        while (true) {
            bool collided = false;
            for (size_t i = 0; i + 1 < res.size(); ++i) {
                if (res[i] > 0 && res[i + 1] < 0) {
                    collided = true;
                    int left_size = std::abs(res[i]);
                    int right_size = std::abs(res[i + 1]);
                    
                    if (left_size > right_size) {
                        res.erase(res.begin() + i + 1);
                    } else if (left_size < right_size) {
                        res.erase(res.begin() + i);
                    } else {
                        res.erase(res.begin() + i, res.begin() + i + 2);
                    }
                    break;
                }
            }
            if (!collided) break;
        }
        
        return res;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N^2)$
  - Each collision scan and vector `erase` takes $\mathcal{O}(N)$ time, repeated up to $N/2$ times.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Vector copy storage.

---

## Why This Approach Is Not Optimal

Repeated vector element deletion takes quadratic $\mathcal{O}(N^2)$ time. Using a **Collision Stack**, we can simulate asteroid collisions in a single pass in linear $\mathcal{O}(N)$ time.
