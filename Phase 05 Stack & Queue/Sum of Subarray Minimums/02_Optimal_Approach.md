# Sum of Subarray Minimums - Optimal Approach (Monotonic Stack PLE & NLE)

- **Problem Number**: 907
- **Platform**: LeetCode #907
- **Difficulty**: Medium
- **Pattern**: Contribution Technique + Monotonic Increasing Stack ($\mathcal{O}(N)$)

---

## Optimal Intuition

For each element `arr[i]`, determine how many subarrays have `arr[i]` as their minimum.
Let:
- `left[i]`: distance to Previous Less Element (PLE).
- `right[i]`: distance to Next Less or Equal Element (NLE).
Total subarrays where `arr[i]` is minimum $= \text{left}[i] \times \text{right}[i]$.
Total contribution $= \text{arr}[i] \times \text{left}[i] \times \text{right}[i]$.

---

## Code

```cpp
#include <vector>
#include <stack>

class Solution {
public:
    int sumSubarrayMins(std::vector<int>& arr) {
        int n = arr.size();
        int MOD = 1e9 + 7;
        std::vector<int> left(n), right(n);
        std::stack<int> st;

        // Previous Less Element
        for (int i = 0; i < n; i++) {
            while (!st.empty() && arr[st.top()] > arr[i]) st.pop();
            left[i] = st.empty() ? (i + 1) : (i - st.top());
            st.push(i);
        }

        while (!st.empty()) st.pop();

        // Next Less or Equal Element
        for (int i = n - 1; i >= 0; i--) {
            while (!st.empty() && arr[st.top()] >= arr[i]) st.pop();
            right[i] = st.empty() ? (n - i) : (st.top() - i);
            st.push(i);
        }

        long long total = 0;
        for (int i = 0; i < n; i++) {
            long long count = (1LL * left[i] * right[i]) % MOD;
            total = (total + count * arr[i]) % MOD;
        }
        return total;
    }
};
```

---

## Time & Space Complexity

- **Time Complexity**: $\mathcal{O}(N)$
- **Space Complexity**: $\mathcal{O}(N)$
