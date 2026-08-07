# 130. Course Schedule II

- **Platform**: LeetCode
- **Problem Number**: #210
- **Difficulty**: Medium
- **URL**: [LeetCode #210 - Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)

---

## Problem Statement

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you **must** take course `bi` first if you want to take course `ai`.

- For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.

Return *the ordering of courses you should take to finish all courses*. If there are many valid answers, return **any** of them. If it is impossible to finish all courses, return **an empty array**.

---

## Examples

### Example 1
```text
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
```

### Example 2
```text
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after course 0.
So one correct course order is [0,1,2,3]. Another correct order is [0,2,1,3].
```

### Example 3
```text
Input: numCourses = 1, prerequisites = []
Output: [0]
```

---

## Constraints

- $1 \le \text{numCourses} \le 2000$
- $0 \le \text{prerequisites.length} \le 5000$
- $\text{prerequisites}[i].\text{length} == 2$
- $0 \le a_i, b_i < \text{numCourses}$
- $a_i \neq b_i$
- All the pairs `prerequisites[i]` are **distinct**.
