# 04 Interview Follow-ups & System Variations: Peak Index in a Mountain Array

The problem finds the peak index in a strictly increasing then strictly decreasing mountain array. The optimal binary search checks `nums[mid] < nums[mid + 1]` in $\mathcal{O}(\log N)$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem is compared with general peak finding, Ternary Search on unimodal functions, and Golden Section Search.

---

## 1. Binary Search vs. Ternary Search on Unimodal Functions

| Method | Probes Per Step | Shrink Factor | Recurrence | Total Iterations |
| :--- | :--- | :--- | :--- | :--- |
| **Binary Search (Gradient)** | 2 probes (`mid`, `mid+1`) | $1/2$ (halved) | $T(N) = T(N/2) + \mathcal{O}(1)$ | $pprox \log_2 N$ |
| **Ternary Search** | 2 probes ($m_1, m_2$) | $2/3$ (tri-section)| $T(N) = T(2N/3) + \mathcal{O}(1)$ | $pprox 2 \log_{1.5} N$ |

- **Conclusion**: Binary search via slope gradient requires fewer comparison operations than ternary search.

---

## 2. Search in Mountain Array (LeetCode #1095)

### 💡 3-Phase Search with Restricted Probes
- You are given a `MountainArray` interface with at most 100 calls allowed:
  1. **Phase 1**: Find the peak index using Binary Search ($pprox 30$ calls).
  2. **Phase 2**: Binary search target in the increasing left slope `[0 ... peak]` ($pprox 30$ calls).
  3. **Phase 3**: If not found, binary search target in the decreasing right slope `[peak + 1 ... n - 1]` with reverse comparator ($pprox 30$ calls).
- **Total API Calls**: $\le 90 \ll 100$.

---

## Summary Matrix: Trade-offs at a Glance

| Problem | Strategy | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| **Find Mountain Peak** | Binary Search on slope | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| **Search Target in Mountain (#1095)**| Find Peak $	o$ 2 Binary Searches | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
