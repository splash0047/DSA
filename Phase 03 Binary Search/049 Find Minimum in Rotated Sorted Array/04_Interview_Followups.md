# 04 Interview Follow-ups & System Variations: Find Minimum in Rotated Sorted Array

The problem finds the minimum element (the rotation pivot) in a rotated sorted array of unique integers. The optimal binary search compares `nums[mid]` with `nums[right]` in $\mathcal{O}(\log N)$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem tests boundary comparison selection (`nums[right]` vs. `nums[left]`) and calculating the exact rotation count.

---

## 1. Why Compare `nums[mid]` with `nums[right]` instead of `nums[left]`?

### 🛑 The Asymmetry of Unrotated Arrays
Consider an array that is not rotated (or already sorted): `nums = [1, 2, 3, 4, 5]`.
- `left = 0` (`nums[left] = 1`), `mid = 2` (`nums[mid] = 3`), `right = 4` (`nums[right] = 5`).
- If you compare with `nums[left]`: `nums[mid] > nums[left]` ($3 > 1$). In a rotated array, this means the minimum is in the right half, but here the minimum is at index 0 (left half)!
- **If you compare with `nums[right]`**:
  - If `nums[mid] > nums[right]`: Minimum MUST be in the right half `[mid + 1 ... right]`.
  - If `nums[mid] < nums[right]`: Minimum MUST be in `[left ... mid]` (note: include `mid`!).
- Comparing with `nums[right]` works universally across both rotated and unrotated arrays without special checks.

---

## 2. Finding the Exact Rotation Count $K$

### 💡 Rotation Count Formula
- The index of the minimum element `min_idx` represents exactly how many times the array was rotated right.
- For example: `[4, 5, 1, 2, 3]` $	o$ minimum is at index 2 $\implies$ rotated right by 2 steps.

---

## 3. What if Duplicates Are Allowed (LeetCode #154)?

### 💡 Shrinking `right--` on Equality
- If `nums[mid] == nums[right]`, we cannot know which side holds the pivot.
- Action: `right--` (decrement right boundary by 1).
- Time Complexity: $\mathcal{O}(\log N)$ average, $\mathcal{O}(N)$ worst case.

---

## Summary Matrix: Trade-offs at a Glance

| Scenario | Elements | Comparison | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **Distinct (#153)** | Unique | `nums[mid]` vs `nums[right]` | $\mathcal{O}(\log N)$ strictly | $\mathcal{O}(1)$ |
| **Duplicates (#154)** | With Duplicates | `nums[mid] == nums[right] ? right--` | $\mathcal{O}(\log N)$ avg / $\mathcal{O}(N)$ worst | $\mathcal{O}(1)$ |
