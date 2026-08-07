# Problem Summary

Given a sorted array `nums` and a `target`, find the starting and ending indices of `target`. The optimal approach performs **Dual Binary Search**. The first binary search biases left to find the first occurrence (`findFirst`), and the second binary search biases right to find the last occurrence (`findLast`), completing in $\mathcal{O}(\log N)$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to find the range boundaries `[start, end]` of duplicates in a sorted array.
- Dual Binary Search (Lower Bound / Upper Bound) pattern.

---

## Important Clues

1. **"Starting and ending position"**: Dual binary search required.
2. **"O(log n) runtime complexity"**: Mandatory logarithmic constraint.

---

## Example

### Input
`nums = [5, 7, 7, 8, 8, 10]`, `target = 8`

### Visual Step-by-Step Progression

```text
First Occurence Search (bias left):
[5 , 7 , 7 , 8 , 8 , 10]
             ^ (Found at index 3)

Last Occurence Search (bias right):
[5 , 7 , 7 , 8 , 8 , 10]
                 ^ (Found at index 4)

Result Range: [3, 4]
```

---

## Alternative Solutions

### C++ Standard Library (`std::equal_range`)
```cpp
auto [first_it, last_it] = std::equal_range(nums.begin(), nums.end(), target);
if (first_it == last_it) return {-1, -1};
return {(int)(first_it - nums.begin()), (int)(last_it - nums.begin() - 1)};
```
- **Time Complexity**: $\mathcal{O}(\log N)$.
- **Space Complexity**: $\mathcal{O}(1)$.

---

## Edge Cases

1. **Target Not Found**: `nums = [5, 7, 7, 8, 8, 10]`, `target = 6` -> Returns `[-1, -1]`.
2. **Single Element Match**: `nums = [1]`, `target = 1` -> Returns `[0, 0]`.
3. **Empty Array**: `nums = []`, `target = 0` -> Returns `[-1, -1]`.

---

## Interview Tips

- **Explain Biasing Strategy**: State *"In standard Binary Search, finding `nums[mid] == target` terminates the search. In `findFirst`, when `nums[mid] == target`, we save `mid` and contract `high = mid - 1` to search for an EARLIER occurrence. In `findLast`, we contract `low = mid + 1` to search for a LATER occurrence."*

---

## Similar Problems

1. [LeetCode #704: Binary Search](https://leetcode.com/problems/binary-search/)
2. [LeetCode #35: Search Insert Position](https://leetcode.com/problems/search-insert-position/)

---

## Revision Notes

- Problem: Find first and last indices of `target` in sorted array.
- Pattern: Dual Binary Search (`findFirst` and `findLast`).
- `findFirst`: if `nums[mid] >= target`, save `ans` on match and `high = mid - 1`.
- `findLast`: if `nums[mid] <= target`, save `ans` on match and `low = mid + 1`.
- Return `{first, last}`.
- Optimal Complexity: Time $\mathcal{O}(\log N)$, Space $\mathcal{O}(1)$.
