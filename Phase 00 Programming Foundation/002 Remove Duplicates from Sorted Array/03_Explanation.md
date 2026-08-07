# Problem Summary

Given an array of integers `nums` sorted in non-decreasing order, remove all duplicate elements in-place such that each unique element appears only once in the array's prefix. The relative order of unique elements must be preserved. Return the total count $k$ of unique elements, with the array modified such that its first $k$ positions hold these unique elements.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You are given a **sorted** array or sequence and asked to perform operations based on element equality.
- The problem explicitly demands an **in-place** modification with $\mathcal{O}(1)$ auxiliary space constraint.
- You need to separate or filter elements into a prefix window of the array (**Two Pointers: Slow/Fast or Write/Read Pointers**).

---

## Important Clues

1. **"Sorted in non-decreasing order"**: Duplicates are contiguous. No hashing or sorting is needed.
2. **"In-Place with $\mathcal{O}(1)$ Extra Memory"**: Prevents using sets, maps, or auxiliary vectors.
3. **"First $k$ elements must contain unique elements"**: You only need to update the prefix up to index $k-1$; elements past index $k-1$ can be ignored.

---

## Example

### Input
`nums = [1, 1, 2, 3, 3, 4]`

### Visual Step-by-Step Progression

```text
Initial Array:  [ 1 ,  1 ,  2 ,  3 ,  3 ,  4 ]
Pointers:        w,r

Step 1 (r=1):   nums[1] == nums[w] (1 == 1) -> Duplicate! Skip r.
Array:          [ 1 ,  1 ,  2 ,  3 ,  3 ,  4 ]
Pointers:        w     r

Step 2 (r=2):   nums[2] != nums[w] (2 != 1) -> Unique!
                w++, nums[w] = nums[r]
Array:          [ 1 ,  2 ,  2 ,  3 ,  3 ,  4 ]
Pointers:              w    r

Step 3 (r=3):   nums[3] != nums[w] (3 != 2) -> Unique!
                w++, nums[w] = nums[r]
Array:          [ 1 ,  2 ,  3 ,  3 ,  3 ,  4 ]
Pointers:                   w    r

Step 4 (r=4):   nums[4] == nums[w] (3 == 3) -> Duplicate! Skip r.
Array:          [ 1 ,  2 ,  3 ,  3 ,  3 ,  4 ]
Pointers:                   w         r

Step 5 (r=5):   nums[5] != nums[w] (4 != 3) -> Unique!
                w++, nums[w] = nums[r]
Array:          [ 1 ,  2 ,  3 ,  4 ,  3 ,  4 ]
Pointers:                        w         r

Final Result:   k = w + 1 = 4. Prefix: [1, 2, 3, 4]
```

---

## Alternative Solutions

### STL `std::unique` (C++ Idiomatic approach)
C++ standard library provides `std::unique` which implements the two-pointer in-place deduplication natively:
```cpp
class Solution {
public:
    int removeDuplicates(std::vector<int>& nums) {
        auto it = std::unique(nums.begin(), nums.end());
        return std::distance(nums.begin(), it);
    }
};
```
*Note: In interviews, explain the underlying two-pointer mechanism before using STL algorithms.*

---

## Edge Cases

1. **Empty Array**: `nums = []` -> Return `0`.
2. **Single Element Array**: `nums = [1]` -> Return `1`.
3. **All Identical Elements**: `nums = [2, 2, 2, 2]` -> Return `1`, array modified to `[2, ...]`.
4. **All Unique Elements**: `nums = [1, 2, 3, 4]` -> Return `4`, array remains unchanged.
5. **Negative Numbers**: `nums = [-10, -10, -5, 0, 0, 5]` -> Handles negative bounds cleanly without issue.

---

## Interview Tips

- **Mention In-Place Constraint**: Emphasize early that since `nums` is sorted, an $\mathcal{O}(1)$ space two-pointer approach avoids $\mathcal{O}(N)$ memory allocation.
- **Explain Pointer Roles**: Clearly label the two pointers: one **write pointer** (`slow`) maintaining the processed unique boundary, and one **read pointer** (`fast`) exploring new elements.
- **Clarify Array Modification**: Confirm with the interviewer whether elements beyond index $k-1$ need to be wiped or if leaving original values is acceptable.

---

## Similar Problems

1. [LeetCode #27: Remove Element](https://leetcode.com/problems/remove-element/)
2. [LeetCode #80: Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)
3. [LeetCode #283: Move Zeroes](https://leetcode.com/problems/move-zeroes/)
4. [LeetCode #844: Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/)
5. [LeetCode #977: Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/)

---

## Revision Notes

- Array is pre-sorted -> duplicates are contiguous.
- Use Two Pointers (Slow/Fast or Write/Read).
- `write_index` tracks end of unique prefix (starts at 0).
- Loop `read_index` from 1 to `N - 1`.
- If `nums[read_index] != nums[write_index]`: increment `write_index` and set `nums[write_index] = nums[read_index]`.
- Return `write_index + 1` (count of unique elements).
- Time Complexity: $\mathcal{O}(N)$.
- Space Complexity: $\mathcal{O}(1)$ extra memory.
- C++ STL equivalent: `std::unique(nums.begin(), nums.end())`.
