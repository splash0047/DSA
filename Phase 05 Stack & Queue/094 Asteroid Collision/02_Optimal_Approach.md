# Asteroid Collision

## Pattern Used

- **Pattern**: **Stack Collision Simulation**
- **Concept**: Use a `vector<int> st` (acting as a Stack) to process `asteroids` from left to right.
  - For each `ast` in `asteroids`:
    - Set boolean `alive = true`.
    - Collision Condition: While `alive == true`, `!st.empty()`, `st.back() > 0` (moving right), and `ast < 0` (moving left):
      - If `abs(st.back()) < abs(ast)`: Top rightward asteroid is destroyed $\implies$ `st.pop_back()` and continue loop.
      - Else if `abs(st.back()) == abs(ast)`: Both asteroids destroy each other $\implies$ `st.pop_back()`, set `alive = false`, break loop.
      - Else (`abs(st.back()) > abs(ast)`): Incoming leftward asteroid is destroyed $\implies$ set `alive = false`, break loop.
    - If `alive == true`: `st.push_back(ast)`.

---

## Observation

1. When does a collision occur?
   - A collision occurs ONLY when a right-moving asteroid (`st.back() > 0`) is followed by a left-moving asteroid (`ast < 0`).
2. If `st.back() < 0` and `ast > 0`, they are moving away from each other $\implies$ NO collision!
3. Using `vector<int>` directly as a stack avoids needing a separate reversal step at the end.

---

## Intuition

Push incoming asteroids onto a stack. When a left-moving asteroid meets right-moving asteroids at the top of the stack, battle them until the left-moving asteroid is destroyed or clears all smaller right-moving obstacles.

---

## Algorithm

1. Initialize `vector<int> st`.
2. For each `ast` in `asteroids`:
   a. `alive = true`.
   b. While `alive && !st.empty() && st.back() > 0 && ast < 0`:
      - If `st.back() < -ast`:
        - `st.pop_back()`. // Top rightward destroyed, continue while loop
      - Else if `st.back() == -ast`:
        - `st.pop_back()`. // Both destroyed
        - `alive = false`.
      - Else:
        - `alive = false`. // Incoming leftward destroyed
   c. If `alive`:
      - `st.push_back(ast)`.
3. Return `st`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <cmath>

#include <vector>

class Solution {
public:
    std::vector<int> asteroidCollision(const std::vector<int>& asteroids) {
        std::vector<int> st;

        for (int ast : asteroids) {

            while (!st.empty() && st.back() > 0 && ast < 0) {

                if (st.back() < -ast) {
                    st.pop_back();
                }
                else if (st.back() == -ast) {
                    st.pop_back();
                    ast = 0;
                    break;
                }
                else {
                    ast = 0;
                    break;
                }
            }

            if (ast != 0) {
                st.push_back(ast);
            }
        }

        return st;
    }
};
```

---

## Dry Run

### Input
- `asteroids = [10, 2, -5]`

### Execution Trace

- `ast = 10`: Push `10`. Stack: `[10]`
- `ast = 2`: `2 > 0`, no collision with `10`. Push `2`. Stack: `[10, 2]`
- `ast = -5`: `ast < 0` & `st.back() (2) > 0` $\implies$ Collision!
  - `st.back() (2) < |-5| (5)` $\implies$ Pop `2`. Stack: `[10]`. `alive` remains `true`.
  - Next check: `st.back() (10) > |-5| (5)` $\implies$ `alive = false`.
- Final Stack state: `[10]`

### Result
- Output: `[10]`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Each asteroid is pushed onto `st` once and popped at most once across all iterations.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Vector stores up to $N$ surviving asteroids.

---

## Why This is Optimal

- Simulates all collisions in a single pass in linear $\mathcal{O}(N)$ time.
- Uses optimal stack space.

---

## Common Mistakes

1. **Colliding Same Direction Asteroids**: Triggering collisions when `st.back() < 0` and `ast < 0` (both moving left).
2. **Missing `alive = false` Flag**: Continuing to push `ast` onto the stack after it has already exploded in an earlier collision check.
