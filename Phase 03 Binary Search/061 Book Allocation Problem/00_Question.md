# 061. Book Allocation Problem

- **Platform**: GeeksforGeeks
- **Problem Number**: GFG "Allocate Minimum Pages"
- **Difficulty**: Hard
- **URL**: [GeeksforGeeks - Allocate Minimum Pages](https://www.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1)

---

## Problem Statement

You have `n` books, each with `arr[i]` number of pages. There are `m` students, and the books have to be allocated to all `m` students such that:

1. Each student gets **at least one book**.
2. Each book should be allocated to **only one student**.
3. Book allocation should be in **contiguous order**.

You have to allocate the book to `m` students such that the **maximum number of pages** allocated to a student is **minimized**.

Return *the **minimum possible value** of the maximum pages allocated*. If allocation is not possible, return `-1`.

---

## Examples

### Example 1
```text
Input: arr = [12, 34, 67, 90], m = 2
Output: 113
Explanation: Allocation can be done in following ways:
{12} and {34, 67, 90} Maximum Pages = 191
{12, 34} and {67, 90} Maximum Pages = 157
{12, 34, 67} and {90} Maximum Pages = 113
The minimum of these maximum pages is 113.
```

### Example 2
```text
Input: arr = [15, 17, 20], m = 5
Output: -1
Explanation: Allocation is not possible as there are 5 students and only 3 books.
```

---

## Constraints

- $1 \le \text{arr.length} \le 10^5$
- $1 \le \text{arr}[i] \le 10^3$
- $1 \le m \le 10^5$
