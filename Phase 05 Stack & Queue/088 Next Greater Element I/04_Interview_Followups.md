# 04 Interview Follow-ups & System Variations: Next Greater Element I

The problem finds the Next Greater Element for elements of `nums1` in `nums2`. The optimal approach preprocesses `nums2` using a **Monotonic Decreasing Stack** and stores results in a **Hash Map** in $\mathcal{O}(|nums1| + |nums2|)$ time and $\mathcal{O}(|nums2|)$ space.

In technical interviews, this problem tests monotonic lookup tables and generalized range queries.

---

## 1. Monotonic Stack + Hash Map Architecture

```cpp
vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
    unordered_map<int, int> next_greater;
    vector<int> stk;
    
    for (int x : nums2) {
        while (!stk.empty() && x > stk.back()) {
            next_greater[stk.back()] = x;
            stk.pop_back();
        }
        stk.push_back(x);
    }
    
    vector<int> ans;
    for (int x : nums1) {
        ans.push_back(next_greater.count(x) ? next_greater[x] : -1);
    }
    return ans;
}
```

---

## Summary Matrix: Trade-offs at a Glance

| Phase | Strategy | Time | Space |
| :--- | :--- | :--- | :--- |
| **Preprocessing `nums2`** | Monotonic Decreasing Stack | $\mathcal{O}(|nums2|)$ | $\mathcal{O}(|nums2|)$ |
| **Querying `nums1`** | Hash Map Lookup | $\mathcal{O}(|nums1|)$ | $\mathcal{O}(1)$ auxiliary |
