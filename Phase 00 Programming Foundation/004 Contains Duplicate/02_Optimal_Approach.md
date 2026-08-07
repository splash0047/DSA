# Contains Duplicate

## Pattern Used

- **Pattern**: **Hash Set Lookup**
- **Concept**: Using an unordered set (`std::unordered_set`) to record elements as we scan the array. Searching and inserting into a Hash Set takes average $\mathcal{O}(1)$ time.

---

## Observation

An array contains a duplicate if and only if we encounter an element that has **already been seen** in a previous index. A Hash Set provides average $\mathcal{O}(1)$ membership checks, allowing us to detect duplicates instantly during a single traversal.

---

## Intuition

Maintain a set `seen`. As you step through each number in `nums`:
1. Check if the current number is already in `seen`.
2. If it is present, return `true` immediately (duplicate found).
3. If it is not present, insert it into `seen` and move to the next number.
4. If the loop completes, all elements are unique; return `false`.

---

## Algorithm

1. Initialize an empty `std::unordered_set<int> seen`.
2. Iterate through each `num` in `nums`:
   a. If `seen.find(num) != seen.end()`, return `true`.
   b. `seen.insert(num)`.
3. Return `false`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <unordered_set>

class Solution {
public:
    bool containsDuplicate(const std::vector<int>& nums) {
        std::unordered_set<int> seen;
        for (int num : nums) {
            if (seen.find(num) != seen.end()) {
                return true;
            }
            seen.insert(num);
        }
        return false;
    }
};
```

---

## Dry Run

### Input
- `nums = [1, 2, 3, 1]`

### Execution Trace

| Step | `num` | `seen` Set State | `seen.find(num)` | Match Found? | Action |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `1` | `{}` | `end()` | No | `seen.insert(1)` |
| 2 | `2` | `{1}` | `end()` | No | `seen.insert(2)` |
| 3 | `3` | `{1, 2}` | `end()` | No | `seen.insert(3)` |
| 4 | `1` | `{1, 2, 3}` | `found` | **Yes** | Return `true` |

### Result
- Output: `true`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Traverses the $N$ elements of `nums` once.
  - Average time complexity of `unordered_set` lookup and insertion is $\mathcal{O}(1)$.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - In the worst case (where all elements are unique), the hash set stores $N$ elements.

---

## Why This is Optimal

- Checking for uniqueness requires examining each element at least once ($\Omega(N)$ lower bound).
- With $\mathcal{O}(N)$ time, our Hash Set approach is asymptotically optimal.

---

## Common Mistakes

1. **Forgetting Space Complexity Trade-off**: Failing to mention to the interviewer that Sorting offers an alternative $\mathcal{O}(N \log N)$ time and $\mathcal{O}(1)$ space solution.
2. **Worst-Case Hash Collisions**: Not recognizing that `std::unordered_map` / `std::unordered_set` can degrade to $\mathcal{O}(N^2)$ time under malicious hash collision scenarios.
