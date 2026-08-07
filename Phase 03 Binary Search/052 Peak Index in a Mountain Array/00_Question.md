# 052. Peak Index in a Mountain Array

- **Platform**: LeetCode
- **Problem Number**: #852
- **Difficulty**: Medium
- **URL**: [LeetCode #852 - Peak Index in a Mountain Array](https://leetcode.com/problems/peak-index-in-a-mountain-array/)

---

## Problem Statement

An array `arr` is a **mountain** if the following properties hold:

- `arr.length >= 3`
- There exists some `i` with `0 < i < arr.length - 1` such that:
  - `arr[0] < arr[1] < ... < arr[i - 1] < arr[i]`
  - `arr[i] > arr[i + 1] > ... > arr[arr.length - 1]`

Given a mountain array `arr`, return the index `i` such that `arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1]`.

You must solve it in $\mathcal{O}(\log(\text{arr.length}))$ time complexity.

---

## Examples

### Example 1
```text
Input: arr = [0,1,0]
Output: 1
```

### Example 2
```text
Input: arr = [0,2,1,0]
Output: 1
```

### Example 3
```text
Input: arr = [0,10,5,2]
Output: 1
```

---

## Constraints

- $3 \le \text{arr.length} \le 10^5$
- $0 \le \text{arr}[i] \le 10^6$
- `arr` is **guaranteed** to be a mountain array.
