# Next Greater Element I

## Pattern Used

- **Pattern**: **Monotonic Decreasing Stack + Hash Map Lookup**
- **Concept**:
  1. Precompute Next Greater Element for **all elements in `nums2`** using a Monotonic Decreasing Stack `st` and store results in `unordered_map<int, int> next_greater`.
  2. For each element `num` in `nums2`:
     - While `!st.empty() && num > st.top()`:
       - `next_greater[st.top()] = num`.
       - `st.pop()`.
     - `st.push(num)`.
  3. For elements remaining in `st` after traversal, set `next_greater[val] = -1`.
  4. Query `next_greater[x]` for each `x` in `nums1` in $\mathcal{O}(1)$ time!

---

## Observation

1. `nums1` is a subset of `nums2` containing unique numbers.
2. Monotonic Stack precomputes Next Greater Element for every element in `nums2` in a single pass of $\mathcal{O}(N_2)$ time.
3. Hash Map provides instant $\mathcal{O}(1)$ query responses for all elements in `nums1`.

---

## Intuition

First compute Next Greater Element for all numbers in `nums2` using a Monotonic Stack. Save the mapping `{num -> next_greater}` in a Hash Map. Then look up each target number from `nums1` in the Hash Map.

---

## Algorithm

1. `unordered_map<int, int> next_greater`, `stack<int> st`.
2. For each `num` in `nums2`:
   a. While `!st.empty()` and `num > st.top()`:
      - `next_greater[st.top()] = num`.
      - `st.pop()`.
   b. `st.push(num)`.
3. While `!st.empty()`:
   - `next_greater[st.top()] = -1`.
   - `st.pop()`.
4. Create `ans` of size `nums1.size()`.
5. For `i` from `0` to `nums1.size() - 1`:
   - `ans[i] = next_greater[nums1[i]]`.
6. Return `ans`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <stack>
#include <unordered_map>

class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {

        stack<int> st;
        unordered_map<int, int> next;

        for (int num : nums2) {

            while (!st.empty() && num > st.top()) {
                next[st.top()] = num;
                st.pop();
            }

            st.push(num);
        }

        vector<int> ans;

        for (int num : nums1) {
            if (next.count(num))
                ans.push_back(next[num]);
            else
                ans.push_back(-1);
        }

        return ans;
    }
};
```

---

## Dry Run

### Input
- `nums1 = [4, 1, 2]`, `nums2 = [1, 3, 4, 2]`

### Execution Trace

- **Precomputing `nums2`**:
  - `num = 1`: Push `1`. Stack: `[1]`
  - `num = 3`: `3 > 1` $\implies$ `next_greater[1] = 3`, pop `1`. Push `3`. Stack: `[3]`
  - `num = 4`: `4 > 3` $\implies$ `next_greater[3] = 4`, pop `3`. Push `4`. Stack: `[4]`
  - `num = 2`: Push `2`. Stack: `[4, 2]`
  - Remaining in Stack: `next_greater[2] = -1`, `next_greater[4] = -1`.

- **Map Result**: `{1: 3, 3: 4, 2: -1, 4: -1}`.
- **Queries for `nums1`**:
  - `x = 4` $\implies -1$
  - `x = 1` $\implies 3$
  - `x = 2` $\implies -1$

### Result
- Output: `[-1, 3, -1]`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N_1 + N_2)$
  - Building `next_greater` table takes $\mathcal{O}(N_2)$ time. Querying `nums1` elements takes $\mathcal{O}(N_1)$ time.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N_2)$
  - Stack and Hash Map store up to $N_2$ entries.

---

## Why This is Optimal

- Meets the follow-up requirement for an $\mathcal{O}(N_1 + N_2)$ linear time algorithm.
- Precomputes answers efficiently in $\mathcal{O}(1)$ query time per element.

---

## Common Mistakes

1. **Searching `nums2` for Every `nums1` Query**: Running Monotonic Stack per query rather than precomputing for `nums2` once.
2. **Missing Leftover Stack Values**: Forgetting to assign `-1` to elements remaining in `st` after `nums2` loop finishes.
