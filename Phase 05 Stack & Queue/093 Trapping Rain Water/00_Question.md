# 093. Trapping Rain Water

- **Platform**: LeetCode
- **Problem Number**: #42
- **Difficulty**: Hard
- **URL**: [LeetCode #42 - Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)

---

## Problem Statement

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

---

## Examples

### Example 1
```text
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
```

### Example 2
```text
Input: height = [4,2,0,3,2,5]
Output: 9
```

---

## Constraints

- $n == \text{height.length}$
- $1 \le n \le 2 \times 10^4$
- $0 \le \text{height}[i] \le 10^5$
