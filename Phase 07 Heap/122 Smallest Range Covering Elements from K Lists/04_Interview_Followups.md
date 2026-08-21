# 04 Interview Follow-ups & System Variations: Smallest Range Covering Elements from K Lists

The problem finds the smallest range that includes at least one number from each of the $K$ sorted lists (Hard). The optimal solution uses a **Min-Heap of size $K$ tracking `max_val`** in $\mathcal{O}(N \log K)$ time and $\mathcal{O}(K)$ space.

In technical interviews, this problem is compared with Sliding Window on flattened lists and multi-stream synchronization.

---

## 1. Min-Heap Priority Queue Architecture ($\mathcal{O}(N \log K)$ Optimal)

```cpp
vector<int> smallestRange(vector<vector<int>>& nums) {
    // Min-heap storing {val, list_idx, elem_idx}
    priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> pq;
    int current_max = INT_MIN;
    
    for (int i = 0; i < nums.size(); i++) {
        pq.push({nums[i][0], i, 0});
        current_max = max(current_max, nums[i][0]);
    }
    
    int start = 0, end = INT_MAX;
    while (pq.size() == nums.size()) {
        auto top = pq.top(); pq.pop();
        int min_val = top[0], r = top[1], c = top[2];
        
        // Update smallest range
        if (current_max - min_val < end - start) {
            start = min_val;
            end = current_max;
        }
        
        // Push next element from the same list
        if (c + 1 < nums[r].size()) {
            pq.push({nums[r][c + 1], r, c + 1});
            current_max = max(current_max, nums[r][c + 1]);
        }
    }
    return {start, end};
}
```

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Invariant | Time | Space |
| :--- | :--- | :--- | :--- |
| **Min-Heap of size $K$** | Maintain 1 element per list | $\mathcal{O}(N \log K)$ | $\mathcal{O}(K)$ |
| **Flatten + Sliding Window**| Minimum Window Substring | $\mathcal{O}(N \log N)$ | $\mathcal{O}(N)$ |
