# Top K Frequent Elements

## Pattern Used

- **Pattern**: **Min-Heap of Size $k$** OR **Bucket Sort**
- **Optimal Approach 1 (Heap)**: Min-Heap of size $k$ storing `{frequency, element}` pairs.
- **Optimal Approach 2 (Bucket Sort)**: Frequency-indexed buckets array `vector<vector<int>> buckets(N + 1)`.

---

## Observation

1. Max frequency of any element cannot exceed $N$ (length of `nums`).
2. If we map frequency to an index array of buckets `buckets[freq]`, we can gather the elements with highest frequencies by scanning `buckets` backward from index $N$ down to $1$.
3. Alternatively, a Min-Heap of size $k$ maintains the top $k$ most frequent elements in $\mathcal{O}(U \log k)$ time.

---

## Intuition (Bucket Sort)

- Step 1: Count frequency of each number using Hash Map.
- Step 2: Create array of buckets where index $i$ holds all numbers that appear $i$ times.
- Step 3: Iterate backward from highest bucket $N$ to $1$, collecting numbers into our answer until we have $k$ elements.

---

## Algorithm (Bucket Sort - $\mathcal{O}(N)$ Time)

1. Compute frequency map `freq[num]++`.
2. Create `buckets` vector of size `n + 1`, where `buckets[i]` is a vector of integers with frequency $i$.
3. For each `{num, count}` in `freq`, push `num` into `buckets[count]`.
4. Create `ans` vector.
5. Loop `i` from `n` down to `1`:
   - For each `num` in `buckets[i]`:
     - Append `num` to `ans`.
     - If `ans.size() == k`, return `ans`.
6. Return `ans`.

---

## Clean C++17 Solution

### Approach 1: Bucket Sort ($\mathcal{O}(N)$ Time, $\mathcal{O}(N)$ Space) — Optimal

```cpp
#include <vector>
#include <unordered_map>

class Solution {
public:
    std::vector<int> topKFrequent(std::vector<int>& nums, int k) {
        int n = nums.size();
        std::unordered_map<int, int> freq;
        for (int num : nums) {
            freq[num]++;
        }
        
        // Buckets index represents frequency (0 to n)
        std::vector<std::vector<int>> buckets(n + 1);
        for (const auto& [num, count] : freq) {
            buckets[count].push_back(num);
        }
        
        std::vector<int> ans;
        for (int i = n; i >= 1 && ans.size() < k; --i) {
            for (int num : buckets[i]) {
                ans.push_back(num);
                if (ans.size() == k) {
                    return ans;
                }
            }
        }
        
        return ans;
    }
};
```

### Approach 2: Min-Heap ($\mathcal{O}(N \log k)$ Time, $\mathcal{O}(N)$ Space)

```cpp
#include <vector>
#include <unordered_map>
#include <queue>

class Solution {
public:
    std::vector<int> topKFrequent(std::vector<int>& nums, int k) {
        std::unordered_map<int, int> freq;
        for (int num : nums) {
            freq[num]++;
        }
        
        // Min-heap storing pair<frequency, element>
        using Pair = std::pair<int, int>;
        std::priority_queue<Pair, std::vector<Pair>, std::greater<Pair>> minHeap;
        
        for (const auto& [num, count] : freq) {
            minHeap.push({count, num});
            if (minHeap.size() > k) {
                minHeap.pop();
            }
        }
        
        std::vector<int> ans;
        while (!minHeap.empty()) {
            ans.push_back(minHeap.top().second);
            minHeap.pop();
        }
        
        return ans;
    }
};
```

---

## Dry Run (Bucket Sort)

### Input
- `nums = [1,1,1,2,2,3]`, `k = 2`

### Execution Trace

1. `freq = {1:3, 2:2, 3:1}`
2. `buckets`:
   - `buckets[1] = [3]`
   - `buckets[2] = [2]`
   - `buckets[3] = [1]`
3. Iterate `i` from `6` down to `1`:
   - `i = 3`: `buckets[3]` has `1` $\implies$ `ans = [1]`.
   - `i = 2`: `buckets[2]` has `2` $\implies$ `ans = [1, 2]`. `ans.size() == 2 == k` $\implies$ Stop!

### Result
- Output: `[1, 2]`

---

## Time Complexity

- **Bucket Sort**: $\mathcal{O}(N)$
  - Frequency counting takes $\mathcal{O}(N)$.
  - Populating buckets takes $\mathcal{O}(U) \le \mathcal{O}(N)$.
  - Scanning buckets takes $\mathcal{O}(N)$.
  - Total Time: $\mathcal{O}(N)$.
- **Min-Heap Approach**: $\mathcal{O}(N \log k)$
  - Hash map build takes $\mathcal{O}(N)$. Heap operations take $\mathcal{O}(U \log k)$.

---

## Space Complexity

- **Bucket Sort**: $\mathcal{O}(N)$
  - Frequency hash map and buckets array take $\mathcal{O}(N)$ space.
- **Min-Heap Approach**: $\mathcal{O}(N + k)$

---

## Why This is Optimal

- Bucket sort leverages bounded frequency range $[1, N]$ to sort frequencies in linear $\mathcal{O}(N)$ time, beating the $\mathcal{O}(N \log N)$ sorting barrier.

---

## Common Mistakes

1. **Ordering of Pair in Min-Heap**: Putting `{num, count}` instead of `{count, num}` into priority queue. In C++, pairs are compared by first element, so frequency MUST be the first element.
2. **Bucket Index Out of Bounds**: Size of buckets array must be `N + 1` (frequencies range from `1` to `N`).
