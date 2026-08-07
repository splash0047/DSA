# 017. Container With Most Water

- **Platform**: LeetCode
- **Problem Number**: #11
- **Difficulty**: Medium
- **URL**: [LeetCode #11 - Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

---

## Problem Statement

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the $i^{\text{th}}$ line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return *the maximum amount of water a container can store*.

**Notice** that you may not slant the container.

---

## Examples

### Example 1
```text
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section) the container can contain is 49.
Formed by line at index 1 (height 8) and line at index 8 (height 7):
Area = min(8, 7) * (8 - 1) = 7 * 7 = 49.
```

### Example 2
```text
Input: height = [1,1]
Output: 1
```

---

## Constraints

- $n == \text{height.length}$
- $2 \le n \le 10^5$
- $0 \le \text{height}[i] \le 10^4$
