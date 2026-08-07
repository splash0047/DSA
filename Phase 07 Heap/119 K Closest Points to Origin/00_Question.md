# 119. K Closest Points to Origin

- **Platform**: LeetCode
- **Problem Number**: #973
- **Difficulty**: Medium
- **URL**: [LeetCode #973 - K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/)

---

## Problem Statement

Given an array of `points` where `points[i] = [xi, yi]` represents a point on the **X-Y** plane and an integer `k`, return the `k` closest points to the origin `(0, 0)`.

The distance between two points on the **X-Y** plane is the Euclidean distance (i.e., $\sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}$).

You may return the answer in **any order**. The answer is **guaranteed** to be **unique** (except for the order that it is in).

---

## Examples

### Example 1
```text
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(1^2 + 3^2) = sqrt(10).
The distance between (-2, 2) and the origin is sqrt((-2)^2 + 2^2) = sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the k = 1 closest points, so the answer is [[-2,2]].
```

### Example 2
```text
Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
(Buffer order [[-2,4],[3,3]] is also accepted).
```

---

## Constraints

- $1 \le k \le \text{points.length} \le 10^4$
- $-10^4 \le x_i, y_i \le 10^4$
