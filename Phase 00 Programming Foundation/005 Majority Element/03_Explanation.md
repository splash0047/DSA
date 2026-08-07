# Problem Summary

Given an array `nums` of size `n`, find the majority element that appears strictly more than $\lfloor n / 2 \rfloor$ times. The Boyer-Moore Voting Algorithm solves this in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space by maintaining a running candidate and incrementing/decrementing a counter to cancel non-majority pairs.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You are asked to find an element with frequency $> N/2$ (or $> N/K$ in general variants).
- The problem demands an $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space solution without extra memory allocation.

---

## Important Clues

1. **"Frequency $> \lfloor n/2 \rfloor$"**: Mathematical guarantee that majority element occurrences strictly outnumber all other elements combined.
2. **"Majority element always exists"**: Eliminates the need for a second verification pass.

---

## Example

### Input
`nums = [2, 2, 1, 1, 1, 2, 2]`

### Visual Step-by-Step Progression

```text
nums:      [ 2 ,  2 ,  1 ,  1 ,  1 ,  2 ,  2 ]
candidate:   2    2    2    2    1    1    2
count:       1    2    1    0    1    0    1 -> Final Candidate = 2
```

---

## Alternative Solutions

### Sorting
1. Sort `nums` in $\mathcal{O}(N \log N)$ time.
2. The element at index $\lfloor N / 2 \rfloor$ is guaranteed to be the majority element because it occupies more than half of the array length.
3. **Time Complexity**: $\mathcal{O}(N \log N)$.
4. **Space Complexity**: $\mathcal{O}(1)$ or $\mathcal{O}(\log N)$.

---

## Edge Cases

1. **Single Element Array**: `nums = [1]` -> Returns `1`.
2. **Two Identical Elements**: `nums = [3, 3]` -> Returns `3`.
3. **Alternating Elements**: `nums = [1, 2, 1, 2, 1]` -> Returns `1`.

---

## Interview Tips

- **Explain Cancellation Analogy**: Use the "battle of votes" or "pair cancellation" analogy to explain why the algorithm works intuitively.
- **Discuss > N/K Generalization**: Note that Boyer-Moore can be generalized to find elements appearing $> N/K$ times using $K-1$ candidate-counter pairs (e.g., Majority Element II for $> N/3$).

---

## Similar Problems

1. [LeetCode #229: Majority Element II](https://leetcode.com/problems/majority-element-ii/)
2. [LeetCode #1150: Check If a Number Is Majority Element in a Sorted Array](https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/)
3. [LeetCode #136: Single Number](https://leetcode.com/problems/single-number/)

---

## Revision Notes

- Problem: Find element appearing $> N/2$ times.
- Algorithm: Boyer-Moore Voting Algorithm ($\mathcal{O}(N)$ time, $\mathcal{O}(1)$ space).
- Maintain `candidate` and `count`.
- If `count == 0`, `candidate = num`.
- `count += (num == candidate) ? 1 : -1`.
- Sorting Alternative: `nums[N/2]` after $\mathcal{O}(N \log N)$ sort.
