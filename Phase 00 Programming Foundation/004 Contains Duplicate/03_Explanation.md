# Problem Summary

Given an integer array `nums`, return `true` if any element appears at least twice in the array, and `false` if every element is distinct. Using a hash set enables constant time lookups for each element, detecting duplicates in a single $\mathcal{O}(N)$ linear scan.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to determine element uniqueness or membership.
- The input array is unsorted and elements can appear in any order.
- You are asked to trade $\mathcal{O}(N)$ extra space for $\mathcal{O}(N)$ linear time complexity.

---

## Important Clues

1. **"At least twice"**: A single match is sufficient to immediately return `true`.
2. **"Every element is distinct"**: Returns `false` only after checking all elements.
3. **Unsorted Input**: Signals that sorting ($\mathcal{O}(N \log N)$) or hashing ($\mathcal{O}(N)$ space) is required.

---

## Example

### Input
`nums = [1, 2, 3, 1]`

### Visual Step-by-Step Progression

```text
nums: [ 1 ,  2 ,  3 ,  1 ]
seen:  { } -> {1} -> {1,2} -> {1,2,3} -> 1 is already in set! -> return true
```

---

## Alternative Solutions

### Sorting + Adjacent Comparison
1. Sort the input vector `nums` in $\mathcal{O}(N \log N)$ time.
2. Iterate through the sorted array from index `1` to `N - 1`.
3. If `nums[i] == nums[i - 1]`, return `true`.
4. **Time Complexity**: $\mathcal{O}(N \log N)$.
5. **Space Complexity**: $\mathcal{O}(1)$ or $\mathcal{O}(\log N)$ depending on sorting algorithm implementation.

---

## Edge Cases

1. **Single Element**: `nums = [1]` -> Returns `false`.
2. **All Identical**: `nums = [2, 2, 2, 2]` -> Returns `true` on index 1.
3. **Negative Numbers**: `nums = [-1, -2, -3, -1]` -> Hash set handles negative values seamlessly.
4. **Duplicates at Extremes**: `nums = [1, 5, 8, 9, 1]` -> Returns `true` on last element.

---

## Interview Tips

- **Discuss Trade-offs**: Compare the **Hash Set** approach ($\mathcal{O}(N)$ time, $\mathcal{O}(N)$ space) vs **Sorting** approach ($\mathcal{O}(N \log N)$ time, $\mathcal{O}(1)$ space).
- **Mention Hash Collisions**: Be ready to state that `std::unordered_set` uses hash tables with $\mathcal{O}(1)$ average time and $\mathcal{O}(N)$ worst-case time under heavy collisions.

---

## Similar Problems

1. [LeetCode #219: Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/)
2. [LeetCode #220: Contains Duplicate III](https://leetcode.com/problems/contains-duplicate-iii/)
3. [LeetCode #136: Single Number](https://leetcode.com/problems/single-number/)
4. [LeetCode #448: Find All Numbers Disappeared in an Array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/)
5. [LeetCode #287: Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)

---

## Revision Notes

- Problem: Check if array contains any duplicate values.
- Hash Set approach: Single loop inserting into `std::unordered_set<int>`.
- If `seen.find(num) != seen.end()` -> return `true`.
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(N)$.
- Alternative (Sorting): `std::sort` array and check `nums[i] == nums[i-1]`. Time $\mathcal{O}(N \log N)$, Space $\mathcal{O}(1)$.
