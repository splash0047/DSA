# Problem Summary

Given a 1-indexed sorted array `numbers`, find two indices whose elements add up to `target`. Using **Two Pointers (Opposite Ends)**, we start at boundaries `left = 0` and `right = N - 1`. Adjust `left++` if `sum < target` and `right--` if `sum > target`. This yields the 1-based index answer in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- The input array is **sorted**.
- You need to find a pair satisfying a sum or difference condition.
- You must achieve $\mathcal{O}(1)$ auxiliary space without hash maps.

---

## Important Clues

1. **"Sorted in non-decreasing order"**: Strongest signal for Two Pointers / Binary Search.
2. **"O(1) extra space"**: Disqualifies Hash Maps (`std::unordered_map`).
3. **"1-indexed array"**: Must return `left + 1` and `right + 1`.

---

## Example

### Input
`numbers = [2, 7, 11, 15]`, `target = 9`

### Visual Step-by-Step Progression

```text
L -> [ 2 ,  7 ,  11 ,  15 ] <- R   (sum = 2 + 15 = 17 > 9 -> move R)

L -> [ 2 ,  7 ,  11 ,  15 ]        (sum = 2 + 11 = 13 > 9 -> move R)
                 R

L -> [ 2 ,  7 ,  11 ,  15 ]        (sum = 2 + 7 = 9 == 9 -> MATCH!)
            R

Result: [1, 2]
```

---

## Alternative Solutions

### Binary Search (O(N log N) Time, O(1) Space)
- Iterate `i` from `0` to `N-2`, binary search `target - numbers[i]` in `[i+1, N-1]`.

---

## Edge Cases

1. **Negative Numbers**: `numbers = [-3, -1, 0, 4]`, `target = -1` -> Works identically.
2. **Duplicate Values**: `numbers = [2, 2, 7, 15]`, `target = 4` -> `left=0`, `right=1` returns `{1, 2}`.
3. **Minimum Size Array**: `numbers = [1, 2]`, `target = 3` -> Smallest input size.

---

## Interview Tips

- **Compare Two Sum I vs Two Sum II**:
  - Two Sum I (Unsorted): Hash Map ($\mathcal{O}(N)$ time, $\mathcal{O}(N)$ space).
  - Two Sum II (Sorted): Two Pointers ($\mathcal{O}(N)$ time, $\mathcal{O}(1)$ space).

---

## Similar Problems

1. [LeetCode #1: Two Sum](https://leetcode.com/problems/two-sum/)
2. [LeetCode #15: 3Sum](https://leetcode.com/problems/3sum/)
3. [LeetCode #653: Two Sum IV - Input is a BST](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/)

---

## Revision Notes

- Problem: Find 2 indices summing to target in 1-indexed sorted array.
- Strategy: Two Pointers (`left = 0`, `right = N - 1`).
- `while (left < right)`:
  - `sum = numbers[left] + numbers[right]`.
  - `sum == target`: return `{left + 1, right + 1}`.
  - `sum < target`: `left++`.
  - `sum > target`: `right--`.
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(1)$.
