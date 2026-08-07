# 058. Minimum Number of Days to Make m Bouquets

- **Platform**: LeetCode
- **Problem Number**: #1482
- **Difficulty**: Medium
- **URL**: [LeetCode #1482 - Minimum Number of Days to Make m Bouquets](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/)

---

## Problem Statement

You are given an integer array `bloomDay`, an integer `m` and an integer `k`.

You want to make `m` bouquets. To make a bouquet, you need to use `k` **adjacent flowers** from the garden.

The garden consists of `n` flowers, the $i^{\text{th}}$ flower will bloom in the `bloomDay[i]` and then can be used in **exactly one** bouquet.

Return *the **minimum number of days** you need to wait to be able to make `m` bouquets from the garden*. If it is impossible to make `m` bouquets return `-1`.

---

## Examples

### Example 1
```text
Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
Output: 3
Explanation: Let us see what happened in the first three days. x means flower bloomed and _ means flower did not bloom in the garden.
Day 1: [x, _, _, _, _] -> we can get 1 bouquet because we need 1 flower.
Day 2: [x, _, _, _, x] -> we can get 2 bouquets.
Day 3: [x, _, x, _, x] -> we can get 3 bouquets. The answer is 3.
```

### Example 2
```text
Input: bloomDay = [1,10,3,10,2], m = 3, k = 2
Output: -1
Explanation: We need 3 bouquets each should have 2 flowers. That means we need 6 flowers. We only have 5 flowers so it is impossible to get the needed bouquets and we return -1.
```

### Example 3
```text
Input: bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3
Output: 12
Explanation: We need 2 bouquets each should have 3 flowers.
Day 7: [x, x, x, x, _, x, x] -> we can get 1 bouquet because we need 3 adjacent flowers.
Day 12: [x, x, x, x, x, x, x] -> we can get 2 bouquets. The answer is 12.
```

---

## Constraints

- `bloomDay.length == n`
- $1 \le n \le 10^5$
- $1 \le \text{bloomDay}[i] \le 10^9$
- $1 \le m \le 10^6$
- $1 \le k \le n$
