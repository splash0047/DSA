# 04 Interview Follow-ups & System Variations: Sort Array by Increasing Frequency

The problem sorts an array based on the frequency of values in ascending order. If multiple values have the same frequency, sort them in **descending order of their value**. The optimal solution uses a Frequency Hash Map + Custom Comparator in $\mathcal{O}(N \log N)$ time and $\mathcal{O}(N)$ space.

In technical interviews, this problem tests multi-key comparator ordering, stability in sorting, and counting sort adaptations.

---

## 1. Custom Comparator with Tie-Breaking Rules

```cpp
vector<int> frequencySort(vector<int>& nums) {
    unordered_map<int, int> freq;
    for (int x : nums) freq[x]++;
    
    sort(nums.begin(), nums.end(), [&](int a, int b) {
        if (freq[a] != freq[b]) {
            return freq[a] < freq[b]; // Primary key: Ascending Frequency
        }
        return a > b;                 // Tie-breaker: Descending Value
    });
    return nums;
}
```

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Time | Space | Comparator Logic |
| :--- | :--- | :--- | :--- |
| **Hash Map + Sort** | $\mathcal{O}(N \log N)$ | $\mathcal{O}(N)$ | Frequency ASC $	o$ Value DESC |
| **Bucket Sort** | $\mathcal{O}(N \log N)$ | $\mathcal{O}(N)$ | Sort within each frequency bucket |
