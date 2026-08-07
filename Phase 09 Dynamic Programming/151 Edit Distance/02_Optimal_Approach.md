# Edit Distance

## Pattern Used

- **Pattern**: **Levenshtein Distance 2D Grid DP (1D Double Buffering)**
- **Concept**:
  - `dp[i][j]` represents minimum operations to convert `word1[0...i-1]` to `word2[0...j-1]`.
  - Base Cases:
    - `dp[i][0] = i` (Deletions to convert prefix `word1[0...i-1]` to empty string).
    - `dp[0][j] = j` (Insertions to convert empty string to prefix `word2[0...j-1]`).
  - State Transitions:
    - If `word1[i-1] == word2[j-1]`:
      - `dp[i][j] = dp[i-1][j-1]` (No edit required!).
    - Else:
      - `dp[i][j] = 1 + min({dp[i-1][j], dp[i][j-1], dp[i-1][j-1]})`
      - Where `dp[i-1][j]` is Delete, `dp[i][j-1]` is Insert, and `dp[i-1][j-1]` is Replace.
  - Space Optimization: Use two 1D rows (`prev` and `curr`) of size $N + 1$ to optimize auxiliary memory to $\mathcal{O}(N)$.

---

## Observation

1. If the current characters match (`word1[i-1] == word2[j-1]`), cost is $0$ extra edits $\implies$ carry forward diagonal value `dp[i-1][j-1]`.
2. If they mismatch, take $1 + \min(\text{Delete}, \text{Insert}, \text{Replace})$.

---

## Intuition

Construct a 2D matrix of operations needed to turn each prefix of `word1` into each prefix of `word2`. At each cell `(i, j)`, look at the cost of your 3 options: deleting a character from `word1` (top), inserting a character into `word1` (left), or replacing a character (diagonal). Pick the minimum cost.

---

## Algorithm

1. `m = word1.size()`, `n = word2.size()`.
2. `vector<int> prev(n + 1), curr(n + 1)`.
3. Init `prev[j] = j` for `j` from `0` to `n`.
4. Loop `i` from `1` to `m`:
   - `curr[0] = i`.
   - For `j` from `1` to `n`:
     - If `word1[i - 1] == word2[j - 1]`:
       - `curr[j] = prev[j - 1]`.
     - Else:
       - `curr[j] = 1 + min({prev[j], curr[j - 1], prev[j - 1]})`.
   - `prev = curr`.
5. Return `prev[n]`.

---

## Clean C++17 Solution

```cpp
#include <string>
#include <vector>
#include <algorithm>

class Solution {
public:
    int minDistance(std::string word1, std::string word2) {
        int m = word1.size();
        int n = word2.size();
        
        // Ensure word2 is the shorter string for space optimization
        if (m < n) {
            return minDistance(word2, word1);
        }
        
        std::vector<int> prev(n + 1);
        std::vector<int> curr(n + 1);
        
        // Base case: empty word1 to word2[0...j-1] requires j insertions
        for (int j = 0; j <= n; ++j) {
            prev[j] = j;
        }
        
        for (int i = 1; i <= m; ++i) {
            curr[0] = i; // Base case: word1[0...i-1] to empty word2 requires i deletions
            
            for (int j = 1; j <= n; ++j) {
                if (word1[i - 1] == word2[j - 1]) {
                    curr[j] = prev[j - 1]; // Character match: 0 extra operations
                } else {
                    // Mismatch: 1 + min(Delete, Insert, Replace)
                    curr[j] = 1 + std::min({prev[j], curr[j - 1], prev[j - 1]});
                }
            }
            prev = curr;
        }
        
        return prev[n];
    }
};
```

---

## Dry Run

### Input
- `word1 = "horse"`, `word2 = "ros"`

### Execution Trace

- `m = 5, n = 3`. Init `prev = [0, 1, 2, 3]`.
- `i = 1 ('h')`:
  - `j = 1 ('r')`: mismatch $\implies 1 + \min(1, 1, 0) = 1$.
  - `j = 2 ('o')`: mismatch $\implies 1 + \min(2, 1, 1) = 2$.
  - `j = 3 ('s')`: mismatch $\implies 1 + \min(3, 2, 2) = 3$.
  - `prev = [1, 1, 2, 3]`.
- `i = 2 ('o')`:
  - `j = 2 ('o')`: match $\implies \text{prev}[1] = 1$.
  - `prev = [2, 2, 1, 2]`.
- `i = 3 ('r')`: `prev = [3, 2, 2, 2]`.
- `i = 4 ('s')`: `prev = [4, 3, 3, 2]`.
- `i = 5 ('e')`: `prev = [5, 4, 3, 3]`.

### Result
- Output: `3`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(M \times N)$
  - Double loop iterates $M \times N$ times.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(\min(M, N))$
  - Uses two 1D arrays of size $\min(M, N) + 1$.

---

## Why This is Optimal

- Solves Edit Distance in quadratic $\mathcal{O}(M \times N)$ time.
- Uses space optimization to reduce memory from $\mathcal{O}(M \times N)$ to $\mathcal{O}(\min(M, N))$.

---

## Common Mistakes

1. **Mapping DP Operations Incorrectly**: `prev[j]` is Delete, `curr[j-1]` is Insert, `prev[j-1]` is Replace.
2. **Missing Base Case Initialization**: Forgetting `curr[0] = i` inside the outer loop.
