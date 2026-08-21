# 04 Interview Follow-ups & System Variations: Single Element in a Sorted Array

The problem finds the single unique element in a sorted array where every other element appears exactly twice. The optimal binary search uses the **Even-Odd Index Pairing Invariant** in $\mathcal{O}(\log N)$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem is used to compare Bitwise XOR ($\mathcal{O}(N)$) vs. Binary Search ($\mathcal{O}(\log N)$) and bitwise XOR index mapping (`mid ^ 1`).

---

## 1. Why Bitwise XOR is Sub-Optimal Here ($\mathcal{O}(N)$ vs. $\mathcal{O}(\log N)$)

### 💡 XOR Technique
- XORing all elements together cancels out duplicate pairs: $x \oplus x = 0$.
- Result is the single element.
- **Limitation**: Requires visiting all $N$ elements ($\mathcal{O}(N)$ time), completely ignoring the fact that the array is **sorted**.

---

## 2. The Even-Odd Index Invariant & The `mid ^ 1` Bitwise Trick

### 💡 The Pairing Pattern
- **Before the unique element**: Pairs start at EVEN indices and end at ODD indices:
  - $(0, 1), (2, 3), (4, 5) \dots$
  - Invariant: `nums[even] == nums[even + 1]`.
- **After the unique element**: The shift causes pairs to start at ODD indices and end at EVEN indices:
  - $(1, 2), (3, 4), (5, 6) \dots$
  - Invariant: `nums[odd] == nums[odd + 1]`.

### 💡 Elegant `mid ^ 1` Implementation
```cpp
int singleNonDuplicate(vector<int>& nums) {
    int left = 0, right = nums.size() - 1;
    while (left < right) {
        int mid = left + (right - left) / 2;
        // mid ^ 1 toggles even to odd (mid + 1) and odd to even (mid - 1)
        if (nums[mid] == nums[mid ^ 1]) {
            left = mid + 1; // Invariant holds; single element is to the right
        } else {
            right = mid;    // Invariant broken; single element is at mid or to the left
        }
    }
    return nums[left];
}
```

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Array Sorted? | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| **Bitwise XOR** | Not required | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **Binary Search (`mid ^ 1`)**| Must be sorted | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
