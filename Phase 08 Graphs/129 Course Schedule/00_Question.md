# 129. Course Schedule

- **Platform**: LeetCode
- **Problem Number**: #207
- **Difficulty**: Medium
- **URL**: [LeetCode #207 - Course Schedule](https://leetcode.com/problems/course-schedule/)

---

## Problem Statement

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [a, b]` indicates that you **must** take course `b` first if you want to take course `a`.

- For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.

Return `true` if you can finish all courses. Otherwise, return `false`.

---

## Examples

### Example 1
```text
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
```

### Example 2
```text
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
```

---

## Constraints

- $1 \le \text{numCourses} \le 2000$
- $0 \le \text{prerequisites.length} \le 5000$
- $\text{prerequisites}[i].\text{length} == 2$
- $0 \le a_i, b_i < \text{numCourses}$
- All the pairs prerequisites[i] are **unique**.
