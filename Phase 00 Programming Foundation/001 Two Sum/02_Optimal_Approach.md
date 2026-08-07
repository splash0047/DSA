# Two Sum

## Pattern Used

- **Pattern**: **HashMap / Hash Table (One-Pass Lookup)**
- **Concept**: Trading space for time by caching previously visited numbers and their indices in an unordered hash map (`std::unordered_map`).

---

## Observation

For any element `nums[i]`, we need to find another element `nums[j]` such that:
$$\text{nums}[i] + \text{nums}[j] = \text{target}$$

Rewriting this equation gives:
$$\text{nums}[j] = \text{target} - \text{nums}[i]$$

The key observation is that for every element `x` we inspect, we are looking for its **complement**:
$$\text{complement} = \text{target} - x$$

Instead of searching forward in the array for `complement` using an $\mathcal{O}(N)$ loop, we can check if `complement` was already visited in past iterations by querying a Hash Map in average $\mathcal{O}(1)$ time.

---

## Intuition

Imagine walking through the array element by element. At each step:
1. You hold a number `current`.
2. You ask: *"Have I already seen the exact number needed to pair with `current` to reach `target`?"*
3. If yes, you immediately get the index of that complimentary number from your memory notepad (Hash Map) and you are done.
4. If no, you write down `current` and its current index into your memory notepad so future elements can find it.

This transforms an $\mathcal{O}(N^2)$ exhaustive search into a single pass $\mathcal{O}(N)$ algorithm.

---

## Algorithm

1. Initialize an empty hash map `seen` mapping `element_value -> element_index`.
2. Loop through the array from `i = 0` to `n - 1`:
   a. Calculate `complement = target - nums[i]`.
   b. Check if `complement` exists in `seen`.
   c. If `complement` is found:
      - Return `{seen[complement], i}`.
   d. If `complement` is not found:
      - Insert `seen[nums[i]] = i`.
3. Return an empty vector `{}` if no pair is found (guaranteed not to happen under problem constraints).

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <unordered_map>

class Solution {
public:
vector<int> twoSum(vector<int>& nums, int target) {
    unordered_map<int, int> num_map;  // Stores {num, index}
    
    for (int i = 0; i < nums.size(); i++) {
        int complement = target - nums[i];
        
        // If complement exists in the map, return the indices
        if (num_map.find(complement) != num_map.end()) {
            return {num_map[complement], i};
        }
        
        // Store the current number and its index
        num_map[nums[i]] = i;
    }
    
    return {};  // This should never be reached as per the problem statement
}


};
```

---

## Dry Run

### Input
- `nums = [2, 7, 11, 15]`
- `target = 9`

### Execution Trace

| Step | `i` | `nums[i]` | `complement` (`9 - nums[i]`) | `visited` Map State (Before Check) | Match Found? | Action Taken |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 0 | `2` | `7` | `{}` | No | Store `visited[2] = 0` |
| 2 | 1 | `7` | `2` | `{2: 0}` | **Yes** (`visited[2]` exists) | Return `{0, 1}` |

### Result
- Output: `[0, 1]`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - We traverse the list containing $N$ elements exactly once.
  - Each lookup and insertion operation in `std::unordered_map` takes average $\mathcal{O}(1)$ time.
  - Total time complexity is $N \times \mathcal{O}(1) = \mathcal{O}(N)$.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - In the worst case (where the complementary pair is found at the very end of the array), the hash map will store up to $N - 1$ elements.
  - Extra space used is proportional to the number of elements in `nums`.

---

## Why This is Optimal

- **Lower Bound on Time**: To find a solution in an unsorted array, we must inspect every element at least once; otherwise, the missing pair could be hiding in an unvisited element. Therefore, any valid algorithm must take at least $\Omega(N)$ time.
- Since our algorithm runs in $\mathcal{O}(N)$ time, it is asymptotically optimal.

---

## Common Mistakes

1. **Reusing the Same Element**: Checking `target - nums[i] == nums[i]` and returning `{i, i}`. 
   *Prevention*: Store elements in the map *after* checking for complement, or check `seen[complement] != i`.
2. **Two-Pass Hash Map Index Overwrite**: If using a two-pass hash map (populating map first, then searching), duplicate values in `nums` overwrite previous indices.
   *Prevention*: Use the single-pass approach where lookups happen before insertion.
3. **Assuming Sorted Input**: Attempting to use Two Pointers without sorting first. Sorting changes the original indices, requiring extra index tracking.
