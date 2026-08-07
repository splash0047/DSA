# Problem Summary

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order. The challenge is to complete this lookup efficiently in a single pass without needing nested loops.

---

## Pattern Recognition

In an interview, recognize this problem pattern whenever you are asked to:
- Find a pair of elements in an unsorted array satisfying an equality condition ($A + B = K$).
- Optimize an $\mathcal{O}(N^2)$ brute-force pair lookup into $\mathcal{O}(N)$ by trading space for time using a Hash Table.
- Return **indices** of elements (which implies sorting will scramble original positions unless indices are preserved).

---

## Important Clues

1. **Unsorted Array**: Indicates binary search or two pointers directly on the array won't work without prior sorting.
2. **Return Indices (Not Values)**: Sorting the array directly loses original index information unless explicit index-value pairs are created.
3. **Exactly One Solution**: Guarantees we do not need to handle multiple valid pairs or return all pairs.
4. **Cannot Use Same Element Twice**: For any index `i`, we cannot pair it with itself ($i \neq j$).

---

## Example

### Input
`nums = [3, 2, 4]`, `target = 6`

### Visual Step-by-Step Progression

```
Initial State: visited map = {}

Step 1: i = 0, nums[0] = 3
Target Complement = 6 - 3 = 3
Lookup 3 in map -> Not found!
Map update: visited[3] = 0
Map state: { 3: 0 }

Step 2: i = 1, nums[1] = 2
Target Complement = 6 - 2 = 4
Lookup 4 in map -> Not found!
Map update: visited[2] = 1
Map state: { 3: 0, 2: 1 }

Step 3: i = 2, nums[2] = 4
Target Complement = 6 - 4 = 2
Lookup 2 in map -> FOUND at index 1!
Result: return { 1, 2 }
```

---

## Alternative Solutions

### Sorting + Two Pointers
1. Pair each number with its original index: `pairs[i] = {nums[i], i}`.
2. Sort `pairs` based on value in $\mathcal{O}(N \log N)$ time.
3. Use two pointers (`left = 0`, `right = n - 1`):
   - If `pairs[left].val + pairs[right].val == target`, return `{pairs[left].index, pairs[right].index}`.
   - If sum `< target`, `left++`.
   - If sum `> target`, `right--`.
- **Time Complexity**: $\mathcal{O}(N \log N)$ due to sorting.
- **Space Complexity**: $\mathcal{O}(N)$ to store index-value pairs.
- **Trade-off**: Useful if array is already sorted ($\mathcal{O}(1)$ extra space).

---

## Edge Cases

1. **Negative Numbers**: `nums = [-3, 4, 3, 90]`, `target = 0` (Complement calculation works cleanly with negative values).
2. **Duplicate Values**: `nums = [3, 3]`, `target = 6` (Single-pass map prevents overwriting before checking).
3. **Large Integers**: Values close to `INT_MAX` or `INT_MIN` (Check for overflow if sum calculations exceed standard integer range).
4. **Minimum Size Array**: `nums = [1, 2]`, `target = 3` (Smallest valid input size).

---

## Interview Tips

- **Clarify constraints first**: Ask if the array is sorted, if negative numbers exist, and if there are duplicate values.
- **Discuss Space-Time Trade-off**: Explicitly mention to the interviewer: *"We can trade $\mathcal{O}(N)$ memory to improve time complexity from $\mathcal{O}(N^2)$ to $\mathcal{O}(N)$."*
- **Explain Hash Collisions**: Be prepared to answer how `std::unordered_map` handles collisions (chaining/open addressing) and worst-case performance $\mathcal{O}(N^2)$ vs average $\mathcal{O}(N)$.

---

## Similar Problems

1. [LeetCode #167: Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
2. [LeetCode #15: 3Sum](https://leetcode.com/problems/3sum/)
3. [LeetCode #170: Two Sum III - Data structure design](https://leetcode.com/problems/two-sum-iii-data-structure-design/)
4. [LeetCode #560: Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)
5. [LeetCode #653: Two Sum IV - Input is a BST](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/)

---

## Revision Notes

- Problem: Find 2 indices in `nums` such that `nums[i] + nums[j] == target`.
- Brute Force: Two nested loops $\mathcal{O}(N^2)$ time, $\mathcal{O}(1)$ space.
- Optimal: Single pass with `std::unordered_map<int, int>` mapping `value -> index`.
- Key Formula: `complement = target - nums[i]`.
- Check `complement` in map BEFORE inserting `nums[i]` to avoid using same index twice and handle duplicates cleanly.
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(N)$.
- Alternative: Sorting + Two Pointers gives $\mathcal{O}(N \log N)$ time and $\mathcal{O}(1)$ extra space if modifying array is allowed.
