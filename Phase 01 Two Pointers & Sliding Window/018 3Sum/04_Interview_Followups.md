# 04 Interview Follow-ups & System Variations: 3Sum

The 3Sum problem finds all unique triplets $[a, b, c]$ such that $a + b + c = 0$. The optimal solution sorts the array and runs a two-pointer scan for each element in $\mathcal{O}(N^2)$ time and $\mathcal{O}(1)$ or $\mathcal{O}(\log N)$ extra space.

In top-tier interviews, interviewers test your mastery of aggressive search pruning, generalization to $K$-Sum, 3Sum Smaller/Closest variations, and distributed parallel execution.

---

## 1. High-Performance Search Space Pruning (How to Beat 99% of Solutions)

### 💡 4 Critical Early-Exit Pruning Rules
```cpp
sort(nums.begin(), nums.end());
int n = nums.size();

for (int i = 0; i < n - 2; i++) {
    // Prune 1: Smallest element > 0 -> impossible to sum to 0
    if (nums[i] > 0) break;
    
    // Prune 2: Skip identical outer values to avoid duplicate triplets
    if (i > 0 && nums[i] == nums[i - 1]) continue;
    
    // Prune 3: Minimum possible sum with nums[i] is already > 0 -> break
    if ((long long)nums[i] + nums[i + 1] + nums[i + 2] > 0) break;
    
    // Prune 4: Maximum possible sum with nums[i] is still < 0 -> skip i
    if ((long long)nums[i] + nums[n - 2] + nums[n - 1] < 0) continue;

    int left = i + 1, right = n - 1;
    while (left < right) {
        int sum = nums[i] + nums[left] + nums[right];
        if (sum == 0) {
            res.push_back({nums[i], nums[left], nums[right]});
            while (left < right && nums[left] == nums[left + 1]) left++;
            while (left < right && nums[right] == nums[right - 1]) right--;
            left++; right--;
        } else if (sum < 0) {
            left++;
        } else {
            right--;
        }
    }
}
```

---

## 2. Generalized $K$-Sum (Recursive Reduction to 2-Sum)

### 💡 The Recursive Template
Reduce $K$-Sum to $(K-1)$-Sum down to 2-Sum:
- Base Case ($K = 2$): Run standard Two Pointers.
- Recursive Step ($K > 2$): Loop through index $i \in [\text{start}, N - K]$ with duplicate skipping and bound pruning, then recurse with $K - 1$ and $\text{target} - \text{nums}[i]$.
- **Time Complexity**: $\mathcal{O}(N^{K-1})$, **Space Complexity**: $\mathcal{O}(K)$ recursion stack.

---

## 3. Problem Variations

### 1. 3Sum Closest (LeetCode #16)
- Instead of checking `sum == 0`, track `diff = abs(target - sum)`.
- If `diff < min_diff`, update `closest_sum = sum`.
- Time: $\mathcal{O}(N^2)$, Space: $\mathcal{O}(1)$.

### 2. 3Sum Smaller (LeetCode #259)
- Count triplets with $a + b + c < \text{target}$.
- When `nums[i] + nums[left] + nums[right] < target`:
  - Because array is sorted, **all elements** between `left` and `right` also satisfy the condition!
  - Increment count by $(right - left)$ in $\mathcal{O}(1)$ without scanning each pair.
  - Advance `left++`.

---

## 4. Distributed 3Sum for Massive Datasets (MapReduce / MPI)

### 💡 Partitioning by Outer Element Slices
- Machine $k$ is assigned a subset of outer indices $i$.
- Because the array is read-only after sorting, worker nodes only need a copy of the sorted array (or slice) and compute their two-pointer passes in parallel with zero inter-worker locking.

---

## Summary Matrix: Trade-offs at a Glance

| Variation | Core Technique | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| **3Sum Standard** | Sort + Two Pointers + Duplicate skips | $\mathcal{O}(N^2)$ | $\mathcal{O}(1)$ / $\mathcal{O}(\log N)$ |
| **3Sum Closest** | Sort + Two Pointers tracking `min_diff` | $\mathcal{O}(N^2)$ | $\mathcal{O}(1)$ |
| **3Sum Smaller** | Two Pointers with $+(R - L)$ count leap | $\mathcal{O}(N^2)$ | $\mathcal{O}(1)$ |
| **$K$-Sum Generalized** | Recursive reduction to 2-Sum | $\mathcal{O}(N^{K-1})$ | $\mathcal{O}(K)$ |
