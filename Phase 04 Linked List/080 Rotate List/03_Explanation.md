# Problem Summary

Given the `head` of a linked list, rotate the list to the right by `k` places. The optimal approach uses **Circular Ring Closing & Break Cut**:
1. Compute total length $N$ and connect `tail->next = head` to form a circular ring.
2. Modulo $k = k \pmod N$.
3. Traverse $N - k$ steps from `head` to locate `new_tail`.
4. Record `new_head = new_tail->next` and break the ring `new_tail->next = nullptr`.
This rotates the list in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to **rotate / shift elements** of a linked list or cyclic sequence by $K$ positions.
- Circular Ring Closing & Break Cut pattern.

---

## Important Clues

1. **"Rotate list right by k places"**: Cyclic shift pattern.
2. **"k up to 2 * 10^9"**: Mandatory `k = k % N` optimization.

---

## Example

### Input
`head = [1 -> 2 -> 3 -> 4 -> 5]`, `k = 2`

### Visual Step-by-Step Progression

```text
Step 1 (Form Ring):
 1 -> 2 -> 3 -> 4 -> 5
 ^-------------------|

Step 2 (Find new_tail at N - k = 3):
 1 -> 2 -> 3 (new_tail)    4 (new_head) -> 5
 
Step 3 (Break Ring):
 3->next = nullptr

Result: 4 -> 5 -> 1 -> 2 -> 3
```

---

## Alternative Solutions

### Step-by-Step Single Rotations (Brute Force)
- Perform single rightward rotation $k$ times.
- **Time Complexity**: $\mathcal{O}(K \times N)$ (Triggers TLE for large $K$).
- **Space Complexity**: $\mathcal{O}(1)$.

---

## Edge Cases

1. **`k == 0` or `k % N == 0`**: List remains unchanged.
2. **Single Element List**: Returns `head`.
3. **`k` Larger Than `N`** ($k = 2000, N = 5$): Handled by `k % N`.

---

## Interview Tips

- **Explain Modulo Optimization**: State *"Since rotating a list of length $N$ by $N$ positions returns the exact same list, taking $k = k \pmod N$ handles arbitrary values of $K$ up to $2 \times 10^9$ in constant time."*

---

## Similar Problems

1. [LeetCode #189: Rotate Array](https://leetcode.com/problems/rotate-array/)
2. [LeetCode #72: Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

---

## Revision Notes

- Problem: Rotate linked list right by $k$ places.
- Pattern: Circular Ring Closing.
- `n = 1`, `tail = head`. While (`tail->next`) `n++`, `tail = tail->next`.
- `k = k % n`. If `k == 0` return `head`.
- `tail->next = head` (Form ring).
- Traverse $n - k$ steps to `new_tail`.
- `new_head = new_tail->next`.
- `new_tail->next = nullptr` (Break ring).
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(1)$.
