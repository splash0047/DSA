# 04 Interview Follow-ups & System Variations: Search in Rotated Sorted Array II

The problem searches for `target` in a rotated sorted array that **may contain duplicates**. The optimal approach shrinks boundaries when `nums[left] == nums[mid] == nums[right]` by incrementing `left++` and decrementing `right--`, achieving $\mathcal{O}(\log N)$ average time and $\mathcal{O}(N)$ worst-case time with $\mathcal{O}(1)$ space.

In technical interviews, this is the definitive question for proving why duplicates break sub-linear worst-case time complexity.

---

## 1. Why Duplicates Force $\mathcal{O}(N)$ Worst-Case Time (Mathematical Proof)

### 🛑 The Ambiguity Hazard
Consider the input:
$$	ext{nums} = [1, 1, 1, 1, 1, 2, 1, 1], \quad 	ext{target} = 2$$
- `left = 0` (`nums[0] = 1`), `right = 7` (`nums[7] = 1`), `mid = 3` (`nums[3] = 1`).
- Notice that:
  $$	ext{nums}[left] == 	ext{nums}[mid] == 	ext{nums}[right] == 1$$
- Is the left half sorted? Yes (`[1, 1, 1, 1]`).
- Is the right half sorted? Yes (`[1, 2, 1, 1]` is rotated, but `[1, 1]` is sorted).
- **The Dilemma**: It is mathematically impossible to know whether the single target element `2` is in the left half or right half without examining elements sequentially.
- Therefore, in the worst case (all elements identical except one), any deterministic algorithm must degrade to $\mathcal{O}(N)$ linear scan.

---

## 2. The Duplicate Resolution Step

```cpp
if (nums[left] == nums[mid] && nums[mid] == nums[right]) {
    left++;
    right--; // Safely eliminate duplicate boundaries
}
```

---

## Summary Matrix: Trade-offs at a Glance

| Feature | Rotated Array I (#33) | Rotated Array II (#81) |
| :--- | :--- | :--- |
| **Duplicate Elements** | Strictly Forbidden (Distinct) | Allowed |
| **Average Time Complexity** | $\mathcal{O}(\log N)$ | $\mathcal{O}(\log N)$ |
| **Worst-Case Time Complexity** | $\mathcal{O}(\log N)$ guaranteed | $\mathcal{O}(N)$ worst-case |
| **Space Complexity** | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ |
