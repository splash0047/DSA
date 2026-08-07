# Problem Summary

Given an integer array `nums`, rotate the array to the right by `k` steps in-place. The optimal approach uses the **Array Reversal Trick**: normalize $k = k \pmod N$, reverse the entire array, reverse the first $k$ elements, and then reverse the remaining $N-k$ elements. This completes the rotation in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You are asked to perform a **cyclic shift or rotation** on an array or string.
- You need to do the shift **in-place** without extra memory allocation.

---

## Important Clues

1. **"Rotate right by k steps"**: Indicates cyclic shift.
2. **"In-place with O(1) space"**: Excludes allocating a temporary auxiliary array.
3. **$k$ can be greater than $N$**: Requires modulo operation `k %= N`.

---

## Example

### Input
`nums = [1, 2, 3, 4, 5, 6, 7]`, `k = 3`

### Visual Step-by-Step Progression

```text
Initial:      [ 1 ,  2 ,  3 ,  4 ,  5 ,  6 ,  7 ]

1. Rev All:   [ 7 ,  6 ,  5 ,  4 ,  3 ,  2 ,  1 ]
                |_______|    |______________|
                 First k         Rest (N-k)

2. Rev 0..k-1: [ 5 ,  6 ,  7 ,  4 ,  3 ,  2 ,  1 ]

3. Rev k..N-1: [ 5 ,  6 ,  7 ,  1 ,  2 ,  3 ,  4 ]  <- Final Result
```

---

## Alternative Solutions

### Cyclic Replacements (Jumping Indices)
- Jump from index `i` to `(i + k) % n`, storing displaced elements.
- Repeat for $\gcd(N, k)$ cycles until all $N$ elements are placed.
- **Time Complexity**: $\mathcal{O}(N)$.
- **Space Complexity**: $\mathcal{O}(1)$.
- *Note*: Harder to write cleanly in an interview compared to 3-step Reversal.

---

## Edge Cases

1. **$k = 0$**: No rotation needed (`k %= n` makes it a no-op).
2. **$k = N$**: Rotates back to original array (`k %= n` evaluates to `0`).
3. **$k > N$**: `k = 10, N = 3` $\rightarrow$ `k = 1` step rotation.
4. **Single Element**: `nums = [1], k = 5` $\rightarrow$ no-op.

---

## Interview Tips

- **Always mention Modulo**: Start by saying *"First, I normalize $k = k \pmod N$ to handle cases where $k \ge N$."*
- **Walk through the Reversal Trick**: Clearly explain why reversing the whole array places the last $k$ elements at the front before fixing their internal order.

---

## Similar Problems

1. [LeetCode #61: Rotate List](https://leetcode.com/problems/rotate-list/)
2. [LeetCode #186: Reverse Words in a String II](https://leetcode.com/problems/reverse-words-in-a-string-ii/)
3. [LeetCode #151: Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/)

---

## Revision Notes

- Problem: Rotate array right by $k$ steps in-place.
- Step 1: `k %= n`.
- Step 2: `std::reverse(nums.begin(), nums.end())`.
- Step 3: `std::reverse(nums.begin(), nums.begin() + k)`.
- Step 4: `std::reverse(nums.begin() + k, nums.end())`.
- Time Complexity: $\mathcal{O}(N)$.
- Space Complexity: $\mathcal{O}(1)$.
