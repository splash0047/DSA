# K-th Element of Two Sorted Arrays

- **Problem Number**: GFG K-th Element of Two Sorted Arrays
- **Platform**: GeeksforGeeks
- **Difficulty**: Medium
- **Pattern**: Two-Pointer Linear Count

---

## Brute Force Intuition

Use two pointers `i` and `j` to simulate merging `a` and `b`. Keep a count `count` of elements processed. When `count == k`, return the current merged element.

---

## Algorithm

1. `i = 0`, `j = 0`, `count = 0`.
2. While `i < n` and `j < m`:
   a. `count++`.
   b. `curr_val = (a[i] <= b[j]) ? a[i++] : b[j++]`.
   c. If `count == k`, return `curr_val`.
3. While `i < n`:
   a. `count++`.
   b. If `count == k`, return `a[i]`.
   c. `i++`.
4. While `j < m`:
   a. `count++`.
   b. If `count == k`, return `b[j]`.
   c. `j++`.
5. Return `-1`.

---

## Code

```cpp
#include <vector>

class Solution {
public:
    int kthElement(const std::vector<int>& a, const std::vector<int>& b, int k) {
        int n = a.size();
        int m = b.size();
        int i = 0, j = 0;
        int count = 0;
        
        while (i < n && j < m) {
            int val;
            if (a[i] <= b[j]) {
                val = a[i++];
            } else {
                val = b[j++];
            }
            count++;
            if (count == k) return val;
        }
        
        while (i < n) {
            count++;
            if (count == k) return a[i];
            i++;
        }
        
        while (j < m) {
            count++;
            if (count == k) return b[j];
            j++;
        }
        
        return -1;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(K)$
  - In worst-case $K = N + M$, scanning takes $\mathcal{O}(N + M)$ time.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Constant auxiliary space.

---

## Why This Approach Is Not Optimal

Two-pointer linear count takes $\mathcal{O}(K)$ time. For $N, M = 10^6$, $K$ can be up to $2 \times 10^6$. Using **Binary Search on Array Partitions**, we can find the $k^{\text{th}}$ element in $\mathcal{O}(\log(\min(N, M)))$ time.
