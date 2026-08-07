# Problem Summary

Given an integer array `nums`, return an array `answer` where `answer[i]` is the product of all elements in `nums` except `nums[i]`, without using the division operator. The optimal approach uses **Prefix & Suffix Accumulated Products**. Pass 1 computes prefix products directly in `answer`. Pass 2 accumulates suffix products backwards in a single integer variable `suffix_prod`, achieving $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ extra space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to compute a cumulative property for every element excluding itself (e.g. product/sum except self).
- Combining a forward (prefix) pass with a backward (suffix) pass.

---

## Important Clues

1. **"Product of array except self"**: Left product $\times$ Right product.
2. **"Without using division"**: Excludes total product division strategy.
3. **"O(1) extra space follow-up"**: Reuse output vector for prefix pass, use scalar for suffix pass.

---

## Example

### Input
`nums = [1, 2, 3, 4]`

### Visual Step-by-Step Progression

```text
Pass 1 (Prefix products to left):
answer = [ 1 , 1 , 2 , 6 ]

Pass 2 (Multiply suffix products from right):
suffix_prod = 1
i = 3: answer[3] =  6 * 1 =  6, suffix_prod = 4
i = 2: answer[2] =  2 * 4 =  8, suffix_prod = 12
i = 1: answer[1] =  1 * 12 = 12, suffix_prod = 24
i = 0: answer[0] =  1 * 24 = 24

Result: [24, 12, 8, 6]
```

---

## Alternative Solutions

### Division with Zero Handling (O(N) Time, O(1) Space)
- Count total zeroes in array.
- If zeroes $> 1$: return all 0s.
- If zeroes $== 1$: output is 0 everywhere except at the zero index, which gets total product of non-zero elements.
- If zeroes $== 0$: `answer[i] = total_product / nums[i]`.
- *(Disqualified by problem statement "without using division")*.

---

## Edge Cases

1. **Array Contains One Zero**: `nums = [-1, 1, 0, -3, 3]` -> Returns `[0, 0, 9, 0, 0]`.
2. **Array Contains Multiple Zeroes**: `nums = [0, 0, 2, 3]` -> Returns `[0, 0, 0, 0]`.
3. **Minimum Size Array**: `nums = [2, 3]` -> Returns `[3, 2]`.

---

## Interview Tips

- **Explain Space Optimization Rationale**: Point out *"By storing prefix products directly into the return vector `answer` and keeping only a single scalar `suffix_prod` for the backward pass, we achieve $\mathcal{O}(1)$ extra memory."*

---

## Similar Problems

1. [LeetCode #42: Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)
2. [LeetCode #152: Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)

---

## Revision Notes

- Problem: Product of all elements except `nums[i]` without division.
- Strategy: Two passes (Prefix pass + Suffix scalar pass).
- Pass 1: `answer[0] = 1`, `for i=1..N-1: answer[i] = answer[i-1] * nums[i-1]`.
- Pass 2: `suffix_prod = 1`, `for i=N-1..0: answer[i] *= suffix_prod; suffix_prod *= nums[i]`.
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(1)$ auxiliary space.
