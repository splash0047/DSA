# 04 Interview Follow-ups & System Variations: Find First and Last Position

The problem finds the starting and ending position of a given `target` in a sorted array with duplicates. The optimal approach runs two separate binary searches (`lower_bound` and `upper_bound - 1`) in $\mathcal{O}(\log N)$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem is used to test boundary binary search templates, counting element frequencies in $\mathcal{O}(\log N)$, and distributed inverted index search.

---

## 1. Single Reusable Binary Search Template for Both Left and Right Bounds

### 💡 Generalized Helper Function
```cpp
int findBound(vector<int>& nums, int target, bool isFirst) {
    int left = 0, right = nums.size() - 1, ans = -1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) {
            ans = mid;
            if (isFirst) right = mid - 1; // Keep searching left for first occurrence
            else left = mid + 1;         // Keep searching right for last occurrence
        } else if (nums[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return ans;
}
```

---

## 2. Follow-up: Count Frequency of Target in $\mathcal{O}(\log N)$ Time

### 💡 Constant-Time Count from Range Boundaries
- Instead of linearly scanning duplicates in $\mathcal{O}(K)$ time:
  $$	ext{Count}(	ext{target}) = 	ext{last\_pos} - 	ext{first\_pos} + 1$$
- If `first_pos == -1`, count is 0.
- Guarantees strictly $\mathcal{O}(\log N)$ runtime even if all $10^9$ elements in the array are equal to `target`.

---

## 3. What if $N = 10^9$ on Distributed Inverted Indices?

### 💡 Search Engine Postings List
- In search engines (Lucene / ElasticSearch), terms point to sorted lists of document IDs.
- To find all documents containing a term within a timestamp range $[T_1, T_2]$, run `lower_bound(T1)` and `upper_bound(T2)` on the postings list.

---

## Summary Matrix: Trade-offs at a Glance

| Variation | Strategy | Time | Space |
| :--- | :--- | :--- | :--- |
| **First & Last Position** | Two Binary Searches (Left & Right) | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| **Count Target Frequency** | `(last - first + 1)` formula | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| **Linear Duplicates Scan** | Find one + Scan both ways | $\mathcal{O}(\log N + K)$ | $\mathcal{O}(1)$ |
