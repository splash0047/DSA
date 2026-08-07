# Sort Array by Increasing Frequency

## Pattern Used

- **Pattern**: **Priority Queue (Heap with Custom Struct Comparator)**
- **Concept**:
  - Store `{frequency, value}` tuples in a Min-Heap with a custom comparison struct `Compare`:
    - Priority 1: Lower frequency comes first (Min-Heap on frequency).
    - Priority 2: Higher value comes first when frequencies are equal (Max-Heap on value).
  - Pop elements from the min-heap one by one and append each value `frequency` times into the result array.

---

## Observation

1. Priority queue ordering rule:
   - Primary metric: Frequency ascending $\implies$ `freq1 > freq2` means `element1` has lower priority than `element2` in C++ min priority queue.
   - Secondary metric: Value descending $\implies$ `val1 < val2` means `element1` has lower priority (so higher value comes out first).
2. Heap-based sorting guarantees elements emerge in the exact required tie-breaker sequence.

---

## Intuition

1. Count element frequencies with a hash map.
2. Push all `{frequency, value}` pairs into a priority queue that pops smallest frequency first (and largest value first on tie).
3. Extract each top element from the priority queue and insert it into `ans` `frequency` times.

---

## Algorithm

1. Build frequency map `freq`.
2. Define custom struct `Compare`:
   - Returns `true` if `a.freq > b.freq` (higher frequency has lower priority, so smaller frequency pops first).
   - If `a.freq == b.freq`, returns `true` if `a.val < b.val` (smaller value has lower priority, so larger value pops first).
3. Push all `{freq, val}` pairs into `std::priority_queue<Element, vector<Element>, Compare> pq`.
4. While `pq` is not empty:
   - `curr = pq.top(); pq.pop();`
   - Push `curr.val` into `ans` `curr.freq` times.
5. Return `ans`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <unordered_map>
#include <queue>

struct Element {
    int freq;
    int val;
};

struct Compare {
    bool operator()(const Element& a, const Element& b) {
        if (a.freq != b.freq) {
            return a.freq > b.freq; // Lower frequency has higher priority (pops first)
        }
        return a.val < b.val; // Higher value has higher priority (pops first)
    }
};

class Solution {
public:
    std::vector<int> frequencySort(std::vector<int>& nums) {
        std::unordered_map<int, int> freqMap;
        for (int num : nums) {
            freqMap[num]++;
        }
        
        std::priority_queue<Element, std::vector<Element>, Compare> pq;
        for (const auto& [val, freq] : freqMap) {
            pq.push({freq, val});
        }
        
        std::vector<int> ans;
        ans.reserve(nums.size());
        
        while (!pq.empty()) {
            Element curr = pq.top();
            pq.pop();
            
            for (int i = 0; i < curr.freq; ++i) {
                ans.push_back(curr.val);
            }
        }
        
        return ans;
    }
};
```

---

## Dry Run

### Input
- `nums = [1, 1, 2, 2, 2, 3]`

### Execution Trace

1. `freqMap = {1: 2, 2: 3, 3: 1}`
2. Heap pushes: `{2, 1}`, `{3, 2}`, `{1, 3}`
3. Heap order on pops:
   - Pop 1: `{freq: 1, val: 3}` $\implies$ Append `3` once $\implies$ `ans = [3]`
   - Pop 2: `{freq: 2, val: 1}` $\implies$ Append `1` twice $\implies$ `ans = [3, 1, 1]`
   - Pop 3: `{freq: 3, val: 2}` $\implies$ Append `2` 3 times $\implies$ `ans = [3, 1, 1, 2, 2, 2]`

### Result
- Output: `[3, 1, 1, 2, 2, 2]`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N + U \log U)$
  - Where $N$ is array size and $U$ is number of unique elements.
  - Building frequency map takes $\mathcal{O}(N)$.
  - Pushing $U$ elements into priority queue takes $\mathcal{O}(U \log U)$.
  - Popping elements takes $\mathcal{O}(U \log U)$. Total time is $\mathcal{O}(N + U \log U)$.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(U)$
  - Hash map and priority queue store $U$ unique elements.

---

## Why This is Optimal

- Priority queue organizes unique elements by frequency and value in logarithmic $\mathcal{O}(U \log U)$ time, avoiding unnecessary sorting of duplicate elements.

---

## Common Mistakes

1. **Reversing Comparator Logic**: In C++ `std::priority_queue`, `operator()` returning `true` means the left element has LOWER priority (placed deeper in heap).
2. **Tie-Breaker Inversion**: Sorting values ascending on tie instead of descending as required by the problem statement.
