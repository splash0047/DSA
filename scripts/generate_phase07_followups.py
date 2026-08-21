import os

BASE_DIR = r"c:\Users\Pinak chimurkar\DSA\Phase 07 Heap"

data = {
    "113 Kth Largest Element in an Array": """# 04 Interview Follow-ups & System Variations: Kth Largest Element in an Array

The problem finds the $k$-th largest element in an unsorted array. Optimal approaches include **QuickSelect** ($\mathcal{O}(N)$ average time, $\mathcal{O}(1)$ space) and a **Min-Heap of size $K$** ($\mathcal{O}(N \log K)$ time, $\mathcal{O}(K)$ space).

In top-tier technical interviews, this is the benchmark for selection algorithms. Interviewers probe QuickSelect worst-case guarantees (Median-of-Medians), memory stream bottlenecks, and distributed top-$K$ map-reduce.

---

## 1. QuickSelect vs. Min-Heap of Size $K$

| Metric | QuickSelect (Hoare's Selection) | Min-Heap of Size $K$ |
| :--- | :--- | :--- |
| **Average Time** | **$\mathcal{O}(N)$ (Linear)** | $\mathcal{O}(N \log K)$ |
| **Worst-Case Time** | $\mathcal{O}(N^2)$ (Avoidable via random pivot)| **$\mathcal{O}(N \log K)$ (Guaranteed)** |
| **Space Complexity**| $\mathcal{O}(1)$ auxiliary | $\mathcal{O}(K)$ memory |
| **Streaming Suitability**| Fails (requires random array access) | **Optimal for infinite stream** |

---

## 2. Guaranteed $\mathcal{O}(N)$ Worst-Case: Median-of-Medians (BFPRT Algorithm)

### 💡 Deterministic Good Pivot Selection
- Group elements into blocks of 5.
- Find the median of each 5-element block.
- Recursively find the median of the $\lceil N/5 \rceil$ medians ($M$).
- Use $M$ as the partition pivot.
- **Recurrence**:
  $$T(N) \le T(N/5) + T(7N/10) + \mathcal{O}(N) \implies T(N) = \mathcal{O}(N) \text{ strictly}$$

---

## 3. What if $N = 10^9$ Elements on Distributed Cluster (MapReduce)?

### 💡 MapReduce Top-$K$ Pipeline
1. **Mapper Phase**: Each of the $M$ worker nodes processes its local partition using an in-memory Min-Heap of size $K$ and outputs its local top-$K$ candidates.
2. **Reducer Phase**: The single reducer receives $M \times K$ total candidate elements and merges them in a final Min-Heap of size $K$.
- **Network Traffic**: Transmits only $M \times K$ scalars instead of shuffling $10^9$ raw numbers!

---

## Summary Matrix: Trade-offs at a Glance

| Scenario | Recommended Approach | Time | Space |
| :--- | :--- | :--- | :--- |
| **Static In-Memory** | Randomized QuickSelect | $\mathcal{O}(N)$ avg | $\mathcal{O}(1)$ |
| **Live Stream** | Min-Heap of size $K$ | $\mathcal{O}(N \log K)$ | $\mathcal{O}(K)$ |
| **Distributed Cluster**| Local Min-Heap $\to$ Global Reducer Merge | $\mathcal{O}(\frac{N}{M} \log K)$ | $\mathcal{O}(K)$ / node |
""",

    "114 Kth Smallest Element in an Array": """# 04 Interview Follow-ups & System Variations: Kth Smallest Element in an Array

The problem finds the $k$-th smallest element in an unsorted array. Optimal approaches include QuickSelect ($\mathcal{O}(N)$ average) or a **Max-Heap of size $K$** ($\mathcal{O}(N \log K)$ time, $\mathcal{O}(K)$ space).

In technical interviews, this problem is extended to 2D Sorted Matrices (LeetCode #378) and $K$-th smallest sums.

---

## 1. Generalization: K-th Smallest Element in a Sorted Matrix (LeetCode #378)

### 🛑 The Challenge
Given an $N \times N$ matrix where each row and column is sorted in ascending order, find the $k$-th smallest element.

### 💡 Two Optimal Approaches
1. **Min-Heap of Row Pointers ($\mathcal{O}(K \log N)$)**:
   - Push first element of each row `(matrix[r][0], r, 0)` into a Min-Heap of size $N$.
   - Pop minimum $K$ times and insert next element from the popped row.
2. **Binary Search on the Value Range ($\mathcal{O}(N \log(\text{max} - \text{min}))$ Optimal)**:
   - Search space: $[\text{matrix}[0][0], \text{matrix}[N-1][N-1]]$.
   - For a candidate value $M$, count how many elements in the matrix are $\le M$ using Saddleback search from top-right in $\mathcal{O}(N)$ time.
   - **Space Complexity**: strictly $\mathcal{O}(1)$!

---

## Summary Matrix: Trade-offs at a Glance

| Variation | Strategy | Time | Space |
| :--- | :--- | :--- | :--- |
| **1D Array** | QuickSelect / Max-Heap | $\mathcal{O}(N)$ avg / $\mathcal{O}(N \log K)$ | $\mathcal{O}(1)$ / $\mathcal{O}(K)$ |
| **2D Sorted Matrix** | Binary Search on Range + Saddleback | $\mathcal{O}(N \log(\text{Range}))$ | strictly $\mathcal{O}(1)$ |
""",

    "115 Top K Frequent Elements": """# 04 Interview Follow-ups & System Variations: Top K Frequent Elements

The problem returns the $k$ most frequent elements. While a Min-Heap achieves $\mathcal{O}(N \log K)$, the optimal **Bucket Sort (Frequency Buckets)** runs in strictly $\mathcal{O}(N)$ linear time and $\mathcal{O}(N)$ space.

In technical interviews, this problem tests linear bucket sorting and distributed heavy hitters (Count-Min Sketch, Space-Saving algorithm).

---

## 1. Bucket Sort for Guaranteed $\mathcal{O}(N)$ Linear Time

### 💡 Frequency Array of Lists
1. Compute frequency map `unordered_map<int, int> count`.
2. Allocate bucket array of size $N + 1$: `vector<vector<int>> buckets(n + 1)`.
3. Place each unique number into `buckets[count[x]]`.
4. Scan `buckets` from right to left ($N$ down to $1$) and gather the first $K$ numbers.
- **Time Complexity**: $\mathcal{O}(N)$, **Space Complexity**: $\mathcal{O}(N)$.

---

## 2. Distributed Scale: Heavy Hitters in Real-Time Web Traffic

### 🛑 The Problem
Finding the top 100 most trending URLs across 100 million requests/sec on Twitter/Cloudflare without storing every URL in memory.

### 💡 Count-Min Sketch + Space-Saving Algorithm
- Stream URLs into a 2D matrix of hash counters (**Count-Min Sketch**).
- Maintain a bounded Min-Heap / list of $K$ candidate heavy hitters.
- When an item's estimated frequency exceeds the minimum in the heap, promote it.

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Time Complexity | Space Complexity | Best Used When |
| :--- | :--- | :--- | :--- |
| **Bucket Sort** | $\mathcal{O}(N)$ strictly | $\mathcal{O}(N)$ | Max frequency $\le N$ |
| **Min-Heap (size $K$)** | $\mathcal{O}(N \log K)$ | $\mathcal{O}(U)$ unique | $K \ll N$ |
| **Count-Min Sketch** | $\mathcal{O}(1)$ / event | $\mathcal{O}(K + \frac{1}{\epsilon})$ | Unbounded terabyte streams |
""",

    "116 Sort Array by Increasing Frequency": """# 04 Interview Follow-ups & System Variations: Sort Array by Increasing Frequency

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
| **Hash Map + Sort** | $\mathcal{O}(N \log N)$ | $\mathcal{O}(N)$ | Frequency ASC $\to$ Value DESC |
| **Bucket Sort** | $\mathcal{O}(N \log N)$ | $\mathcal{O}(N)$ | Sort within each frequency bucket |
""",

    "117 Find Median from Data Stream": """# 04 Interview Follow-ups & System Variations: Find Median from Data Stream

The problem designs a data structure supporting `addNum(num)` and `findMedian()` in real time. The optimal **Dual-Heap Algorithm** (Max-Heap for lower half, Min-Heap for upper half) achieves $\mathcal{O}(\log N)$ insertion and $\mathcal{O}(1)$ median queries with $\mathcal{O}(N)$ space.

In top-tier technical interviews, this is the absolute classic streaming challenge. Interviewers probe sliding window medians, P99 percentile latency monitors, and T-Digest quantile sketches.

---

## 1. The Dual-Heap Invariant & Balance Rules

### 💡 The Structural Invariants
1. **Order Invariant**: Every element in `max_heap` (lower half) $\le$ every element in `min_heap` (upper half):
   $$\max(\text{lower}) \le \min(\text{upper})$$
2. **Size Invariant**: Either `max_heap.size() == min_heap.size()` OR `max_heap.size() == min_heap.size() + 1`.

### 💡 Insertion Workflow (`addNum`)
```cpp
void addNum(int num) {
    max_heap.push(num);
    min_heap.push(max_heap.top());
    max_heap.pop();
    
    if (max_heap.size() < min_heap.size()) {
        max_heap.push(min_heap.top());
        min_heap.pop();
    }
}

double findMedian() {
    if (max_heap.size() > min_heap.size()) return max_heap.top();
    return (max_heap.top() + min_heap.top()) / 2.0;
}
```

---

## 2. Follow-up: Monitoring P99 Latency (99th Percentile Stream)

### 💡 Asymmetric Dual-Heap
- To support finding the **99th Percentile**:
  - `max_heap` holds $99\%$ of all data points.
  - `min_heap` holds top $1\%$ of all data points.
  - Balance condition: $\text{min\_heap.size()} = \lceil 0.01 \times N \rceil$.

---

## 3. Approximate Streaming Quantiles: T-Digest / GK-Sketch

### 🛑 Memory Bound on 1 Billion Requests
Storing 1 billion floats across heaps requires 8GB RAM.
- **T-Digest**: Compresses stream into dynamic cluster centroids. Computes P50, P90, P99 within 0.1% relative error using only **a few kilobytes of RAM**.

---

## Summary Matrix: Trade-offs at a Glance

| Percentile Metric | Data Structure | `addNum` Time | Query Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **Exact Median (P50)**| 50:50 Dual Heap | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ | $\mathcal{O}(N)$ |
| **Exact P99 Latency** | 99:1 Dual Heap | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ | $\mathcal{O}(N)$ |
| **Approx Percentile** | T-Digest / GK-Quantiles | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ bounded |
""",

    "118 Merge k Sorted Lists": """# 04 Interview Follow-ups & System Variations: Merge k Sorted Lists (Heap)

The problem merges $K$ sorted linked lists of total $N$ nodes. The optimal Min-Heap approach stores the active head node of each of the $K$ lists, running in $\mathcal{O}(N \log K)$ time and $\mathcal{O}(K)$ space.

In technical interviews, this problem is compared with multi-way external streaming and priority queue comparator overhead.

---

## 1. Min-Heap Implementation with Node Pointers

```cpp
struct CompareNode {
    bool operator()(ListNode* a, ListNode* b) {
        return a->val > b->val; // Min-Heap
    }
};

ListNode* mergeKLists(vector<ListNode*>& lists) {
    priority_queue<ListNode*, vector<ListNode*>, CompareNode> pq;
    for (auto list : lists) {
        if (list) pq.push(list);
    }
    
    ListNode dummy(0);
    ListNode* tail = &dummy;
    while (!pq.empty()) {
        ListNode* top = pq.top(); pq.pop();
        tail->next = top;
        tail = tail->next;
        if (top->next) pq.push(top->next);
    }
    return dummy.next;
}
```

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Space Model | Time | Space |
| :--- | :--- | :--- | :--- |
| **Min-Heap (Optimal)** | Heap of $K$ pointers | $\mathcal{O}(N \log K)$ | $\mathcal{O}(K)$ |
| **Divide & Conquer** | Pairwise merge lists | $\mathcal{O}(N \log K)$ | $\mathcal{O}(1)$ auxiliary |
""",

    "119 K Closest Points to Origin": """# 04 Interview Follow-ups & System Variations: K Closest Points to Origin

The problem finds the $k$ closest points to the origin $(0, 0)$ on a 2D plane. Optimal approaches include **Max-Heap of size $K$** ($\mathcal{O}(N \log K)$ time, $\mathcal{O}(K)$ space) and **QuickSelect** ($\mathcal{O}(N)$ average time, $\mathcal{O}(1)$ space).

In technical interviews, this problem tests Euclidean distance optimizations without square roots, and KD-Trees for 2D spatial indexing.

---

## 1. Low-Level Optimization: Avoiding `sqrt()` Calls

### 💡 Monotonic Distance Equivalence
- Distance $D = \sqrt{x^2 + y^2}$.
- Because the square root function is strictly monotonically increasing for non-negative numbers:
  $$D_1 < D_2 \iff x_1^2 + y_1^2 < x_2^2 + y_2^2$$
- Computing raw integer Euclidean norm $x^2 + y^2$ eliminates expensive floating-point `sqrt()` CPU instructions.

---

## 2. Generalization: Spatial Indexing with KD-Tree

### 💡 Dynamic $K$-Nearest Neighbors (KNN)
- If points are fixed and millions of `findKClosest(point)` queries arrive dynamically:
  - Construct a 2D **KD-Tree** (alternating X and Y axis splits) in $\mathcal{O}(N \log N)$ preprocessing.
  - Each KNN query runs in $\mathcal{O}(\log N)$ average time.

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Best Scenario | Time | Space |
| :--- | :--- | :--- | :--- |
| **QuickSelect** | 1-time static query | $\mathcal{O}(N)$ avg | $\mathcal{O}(1)$ |
| **Max-Heap of size $K$** | Streaming points | $\mathcal{O}(N \log K)$ | $\mathcal{O}(K)$ |
| **KD-Tree** | Repeated dynamic queries | $\mathcal{O}(\log N)$ / query | $\mathcal{O}(N)$ tree |
""",

    "120 Reorganize String": """# 04 Interview Follow-ups & System Variations: Reorganize String

The problem reorganizes a string so that no two adjacent characters are identical. Optimal approaches include **Greedy Max-Heap with Blocked Character** ($\mathcal{O}(N \log \Sigma)$) and **Bucket Index Placement** in strictly $\mathcal{O}(N)$ time and $\mathcal{O}(\Sigma)$ space.

In technical interviews, this problem is generalized to $K$-distance separation (Rearrange String $K$ Distance Apart / LeetCode #358).

---

## 1. Impossibility Invariant & $\mathcal{O}(N)$ Linear Placement

### 💡 The Frequency Bound
- If any character has frequency $\text{count} > \lfloor (N + 1) / 2 \rfloor$, it is mathematically impossible to rearrange $\implies$ return `""`.
- **Optimal Placement Algorithm**:
  1. Fill the most frequent character into even indices ($0, 2, 4 \dots$).
  2. Fill remaining characters into subsequent even indices, then switch to odd indices ($1, 3, 5 \dots$).
- **Time Complexity**: $\mathcal{O}(N)$, **Space Complexity**: $\mathcal{O}(\Sigma) = \mathcal{O}(1)$.

---

## 2. Generalization: Rearrange String $K$ Distance Apart (LeetCode #358)

### 💡 Max-Heap + Cooldown Queue of Size $K$
- Maintain a **Max-Heap** of character frequencies and a **Queue** of cooled characters.
- Pop most frequent character, append to result, and push to cooldown queue `(c, count - 1)`.
- When queue size reaches $K$, pop the oldest character from queue and re-insert into Max-Heap.
- **Time Complexity**: $\mathcal{O}(N \log \Sigma)$, **Space Complexity**: $\mathcal{O}(K + \Sigma)$.

---

## Summary Matrix: Trade-offs at a Glance

| Distance Constraint | Optimal Strategy | Time | Space |
| :--- | :--- | :--- | :--- |
| **Distance = 2 (Adjacent)** | Even/Odd Index Filling | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **Distance = $K$ Apart** | Max-Heap + Cooldown Queue (size $K$) | $\mathcal{O}(N \log \Sigma)$ | $\mathcal{O}(K)$ |
""",

    "121 Last Stone Weight": """# 04 Interview Follow-ups & System Variations: Last Stone Weight

The problem simulates smashing the two heaviest stones until at most 1 stone remains. The optimal solution uses a **Max-Heap** in $\mathcal{O}(N \log N)$ time and $\mathcal{O}(N)$ space.

In technical interviews, this problem is contrasted with **Last Stone Weight II** (0-1 Knapsack DP).

---

## 1. Last Stone Weight I vs. Last Stone Weight II (LeetCode #1049)

| Problem | Stone Choice Rule | Problem Reduction | Optimal Strategy | Time |
| :--- | :--- | :--- | :--- | :--- |
| **Stone Weight I (#1046)**| Greedily smash 2 heaviest | Simulation | Max-Heap | $\mathcal{O}(N \log N)$ |
| **Stone Weight II (#1049)**| Choose arbitrary order to minimize final stone | Partition into two sets $S_1, S_2$ with min difference $|S_1 - S_2|$ | 0-1 Knapsack Dynamic Programming | $\mathcal{O}(N \times \sum W)$ |

---

## Summary Matrix: Trade-offs at a Glance

| Variation | Core Technique | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| **Greedy Smashing (I)** | Max-Heap Simulation | $\mathcal{O}(N \log N)$ | $\mathcal{O}(N)$ |
| **Optimal Minimal (II)** | 0-1 Knapsack Subset Sum DP | $\mathcal{O}(N \times \text{Sum})$ | $\mathcal{O}(\text{Sum})$ |
""",

    "122 Smallest Range Covering Elements from K Lists": """# 04 Interview Follow-ups & System Variations: Smallest Range Covering Elements from K Lists

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
"""
}

for folder_name, content in data.items():
    folder_path = os.path.join(BASE_DIR, folder_name)
    if os.path.exists(folder_path):
        target_file = os.path.join(folder_path, "04_Interview_Followups.md")
        with open(target_file, "w", encoding="utf-8") as f:
            f.write(content.strip() + "\n")
        print(f"Written: {target_file}")
    else:
        print(f"Folder NOT found: {folder_path}")
