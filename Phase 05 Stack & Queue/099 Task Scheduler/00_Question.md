# 099. Task Scheduler

- **Platform**: LeetCode
- **Problem Number**: #621
- **Difficulty**: Medium
- **URL**: [LeetCode #621 - Task Scheduler](https://leetcode.com/problems/task-scheduler/)

---

## Problem Statement

You are given an array of CPU tasks `tasks`, where `tasks[i]` is represented by a character from `'A'` to `'Z'`, and a cooling time `n`. Each cycle or interval allows the completion of one task. Tasks can be completed in any order, but there is a constraint: **identical tasks must be separated by at least `n` intervals** due to cooling time.

Return *the **minimum number of intervals** required to complete all tasks*.

---

## Examples

### Example 1
```text
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.
There are at least 2 intervals between any two same tasks.
```

### Example 2
```text
Input: tasks = ["A","C","A","B","D","B"], n = 1
Output: 6
Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.
With a cooling interval of 1, any task can be performed every other interval.
```

### Example 3
```text
Input: tasks = ["A","A","A","B","B","B"], n = 3
Output: 10
Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.
There are at least 3 intervals between any two same tasks.
```

---

## Constraints

- $1 \le \text{tasks.length} \le 10^4$
- `tasks[i]` is an uppercase English letter.
- $0 \le n \le 100$
