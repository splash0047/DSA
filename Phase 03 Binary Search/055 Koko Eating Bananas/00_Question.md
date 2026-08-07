# 055. Koko Eating Bananas

- **Platform**: LeetCode
- **Problem Number**: #875
- **Difficulty**: Medium
- **URL**: [LeetCode #875 - Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/)

---

## Problem Statement

Koko loves to eat bananas. There are `n` piles of bananas, the $i^{\text{th}}$ pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours.

Koko can decide her banana-eating speed of `k` bananas per hour. Each hour, she chooses some pile of bananas and eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return *the minimum integer `k` such that she can eat all the bananas within `h` hours*.

---

## Examples

### Example 1
```text
Input: piles = [3,6,7,11], h = 8
Output: 4
```

### Example 2
```text
Input: piles = [30,11,23,4,20], h = 5
Output: 30
```

### Example 3
```text
Input: piles = [30,11,23,4,20], h = 6
Output: 23
```

---

## Constraints

- $1 \le \text{piles.length} \le 10^4$
- $\text{piles.length} \le h \le 10^9$
- $1 \le \text{piles}[i] \le 10^9$
