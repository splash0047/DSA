# Problem Summary

Given stall positions `stalls` and `k` cows, place all $k$ cows such that the **minimum distance** between any two cows is as **large as possible**. The optimal approach sorts `stalls` and uses **Binary Search on Answer Space** over distance range $[1, \text{stalls}[n-1] - \text{stalls}[0]]$. Greedy placement verifies if $k$ cows fit at least `mid` units apart. If valid, we record `ans = mid` and expand `low = mid + 1` in $\mathcal{O}(N \log N + N \log D)$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You are asked to **maximize the minimum** separation/distance between $K$ items.
- Maximin Binary Search on Answer Space pattern.

---

## Important Clues

1. **"Minimum distance is as large as possible"**: Maximin search objective.
2. **"Place k cows in stalls"**: Greedy placement on sorted coordinates.

---

## Example

### Input
`stalls = [1, 2, 4, 8, 9]`, `k = 3`

### Visual Step-by-Step Progression

```text
Sorted stalls: [1, 2, 4, 8, 9]

Target dist = 3:
Place Cow 1 at 1
Place Cow 2 at 4 (4 - 1 = 3 >= 3)
Place Cow 3 at 8 (8 - 4 = 4 >= 3)

Placed 3 cows with min distance = 3!
```

---

## Alternative Solutions

### Sequential Distance Testing (Brute Force)
- Test distances $d = 1, 2, 3, \dots$ until `canPlace(d)` returns `false`.
- **Time Complexity**: $\mathcal{O}(N \log N + N \times D)$.
- **Space Complexity**: $\mathcal{O}(1)$.

---

## Edge Cases

1. **$k = 2$**: Maximum distance is simply `stalls[n-1] - stalls[0]`.
2. **$k = N$**: Minimum distance is $\min_{i} (\text{stalls}[i] - \text{stalls}[i-1])$.
3. **Large coordinate range**: Distance up to $10^9$; binary search handles in 30 iterations.

---

## Interview Tips

- **Highlight Maximin vs Minimax Difference**: State *"Maximin problems ('maximize the minimum distance') and Minimax problems ('minimize the maximum sum') are both solved using Binary Search on Answer Space. For Maximin, when `canPlace(mid)` is true, we push `low = mid + 1` to search for larger distances."*

---

## Similar Problems

1. [LeetCode #1552: Magnetic Force Between Two Balls](https://leetcode.com/problems/magnetic-force-between-two-balls/)
2. [LeetCode #2517: Maximum Tastiness of Candy Basket](https://leetcode.com/problems/maximum-tastiness-of-candy-basket/)

---

## Revision Notes

- Problem: Maximize minimum distance between $k$ placed cows in `stalls`.
- Strategy: Sort `stalls` + Binary Search on Answer Space (`low = 1`, `high = back - front`).
- `while (low <= high)`:
  - `mid = low + (high - low) / 2`.
  - Place cows greedily at distance $\ge mid$.
  - `if (cows_placed >= k) ans = mid, low = mid + 1`.
  - `else high = mid - 1`.
- Return `ans`.
- Optimal Complexity: Time $\mathcal{O}(N \log N + N \log D)$, Space $\mathcal{O}(1)$.
