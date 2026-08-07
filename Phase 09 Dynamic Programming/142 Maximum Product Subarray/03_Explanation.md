# Problem Summary

Find the contiguous subarray that has the largest product in an integer array `nums`. The optimal approach uses **Kadane's Variant (Min & Max Product Tracking)**:
- Negative numbers flip signs: a large negative product multiplied by a negative number becomes a large positive product!
- Maintain `curMax` and `curMin` initialized to `nums[0]`.
- Iterate `num` in `nums`:
  - `if (num < 0) swap(curMax, curMin);`
  - `curMax = max(num, curMax * num);`
  - `curMin = min(num, curMin * num);`
  - `ans = max(ans, curMax);`
This computes the max product subarray in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need the **maximum product of contiguous elements** in an array containing positive, negative, and zero values.
- Min & Max Dual Tracking DP pattern.

---

## Important Clues

1. **"Maximum product subarray"**: Contiguous subarray product optimization.
2. **"Array contains negative numbers"**: Dual min/max state tracking.

---

## Example

### Input
`nums = [2, 3, -2, 4]`

### Visual Step-by-Step Progression

```text
Elements:  2     3     -2     4

curMax:    2 ->  6 ->  -2 ->  4
curMin:    2 ->  3 -> -12 -> -48
ans:       2 ->  6 ->   6 ->  6

Result: 6 (Subarray [2, 3])
```

---

## Alternative Solutions

### Prefix & Suffix Product Scan ($\mathcal{O}(N)$ Time, $\mathcal{O}(1)$ Space)
- Compute prefix product and suffix product. If a zero is encountered, reset product to 1. The maximum product subarray is `max(all_prefix_products, all_suffix_products)`.

---

## Edge Cases

1. **Single element array**: `nums = [-2]` $\implies$ returns `-2`.
2. **Contains zero**: `nums = [-2, 0, -1]` $\implies$ `curMax` resets to 0. Returns `0`.
3. **Double negative**: `nums = [-2, -3, -4]` $\implies$ returns `12` (from `[-3, -4]`).

---

## Interview Tips

- **Explain Why `swap(curMax, curMin)` Is Necessary**: State *"When we multiply by a negative number, the maximum product becomes the minimum product and vice versa. Swapping them prior to evaluation accounts for sign inversions seamlessly."*

---

## Similar Problems

1. [LeetCode #53: Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
2. [LeetCode #1567: Maximum Length of Subarray With Positive Product](https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/)
3. [LeetCode #713: Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k/)

---

## Revision Notes

- Problem: Max product contiguous subarray.
- Pattern: Kadane's Variant with `curMax` and `curMin`.
- Core Loop: `if (num < 0) swap(curMax, curMin); curMax = max(num, curMax * num); curMin = min(num, curMin * num); ans = max(ans, curMax);`
- Key Insight: Negative numbers flip min/max products.
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(1)$.
