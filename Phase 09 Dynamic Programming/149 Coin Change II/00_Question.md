# 149. Coin Change II

- **Platform**: LeetCode
- **Problem Number**: #518
- **Difficulty**: Medium
- **URL**: [LeetCode #518 - Coin Change II](https://leetcode.com/problems/coin-change-ii/)

---

## Problem Statement

You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return *the **number of combinations** that make up that amount*. If that amount of money cannot be made up by any combination of the coins, return `0`.

You may assume that you have an infinite number of each kind of coin.

The answer is **guaranteed** to fit into a signed **32-bit** integer.

---

## Examples

### Example 1
```text
Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: There are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
```

### Example 2
```text
Input: amount = 3, coins = [2]
Output: 0
Explanation: The amount of 3 cannot be made up just with coins of 2.
```

### Example 3
```text
Input: amount = 10, coins = [10]
Output: 1
```

---

## Constraints

- $1 \le \text{coins.length} \le 300$
- $1 \le \text{coins}[i] \le 5000$
- All the values of `coins` are **unique**.
- $0 \le \text{amount} \le 5000$
