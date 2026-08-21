# First Bad Version - Brute Force

- **Problem Number**: 278
- **Platform**: LeetCode #278
- **Difficulty**: Easy
- **Pattern**: Linear Scan

---

## Algorithm

Iterate linearly from version $1$ to $n$. The first version where `isBadVersion(i) == true` is the answer.

---

## Code

```cpp
// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        for (int i = 1; i <= n; i++) {
            if (isBadVersion(i)) return i;
        }
        return n;
    }
};
```

---

## Time & Space Complexity

- **Time Complexity**: $\mathcal{O}(N)$ API calls.
- **Space Complexity**: $\mathcal{O}(1)$.
