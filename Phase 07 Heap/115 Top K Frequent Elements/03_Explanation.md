# Problem Summary

Given an integer array `nums` and an integer `k`, return the $k$ most frequent elements. The optimal approach uses **Bucket Sort**:
- Count element frequencies with `std::unordered_map<int, int>`.
- Create a bucket array `vector<vector<int>> buckets(N + 1)` where index represents frequency count.
- Populate `buckets[count].push_back(num)`.
- Iterate backward from index $N$ down to $1$, collecting numbers into `ans` until `ans.size() == k`.
This achieves true linear $\mathcal{O}(N)$ time complexity and $\mathcal{O}(N)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need the **$K$ most frequent** items.
- Frequency range is bounded by array length $N$.
- Bucket Sort pattern ($\mathcal{O}(N)$) or Min-Heap of size $k$ ($\mathcal{O}(N \log k)$).

---

## Important Clues

1. **"K most frequent elements"**: Frequency counting + top $k$ retrieval.
2. **"Time complexity better than O(N log N)"**: Sorting is too slow; use Bucket Sort or Heap.

---

## Example

### Input
`nums = [1, 1, 1, 2, 2, 3]`, `k = 2`

### Visual Step-by-Step Progression

```text
1. Frequency Map: {1: 3, 2: 2, 3: 1}

2. Frequency Buckets Array:
Index (Freq) -> Elements
[0] -> []
[1] -> [3]
[2] -> [2]
[3] -> [1]
[4] -> []
[5] -> []
[6] -> []

3. Traverse Backwards from Index 6 down to 1:
- Freq 3: Pick 1 -> ans = [1]
- Freq 2: Pick 2 -> ans = [1, 2] (Reached size k=2!)

Result: [1, 2]
```

---

## Alternative Solutions

### 1. Hash Map + Sorting Pairs ($\mathcal{O}(N \log N)$ Time, $\mathcal{O}(N)$ Space)
- Store `{count, num}` pairs and sort in descending order.

### 2. Min-Heap of Size $k$ ($\mathcal{O}(N \log k)$ Time, $\mathcal{O}(N)$ Space)
- Maintain `{count, num}` pairs in min-priority queue of size $k$.

---

## Edge Cases

1. **All elements unique**: `nums = [1, 2, 3, 4]`, `k = 2` -> Handled properly.
2. **$k = N$**: All unique elements returned.
3. **Single element array**: `nums = [1]`, `k = 1` -> Returns `[1]`.

---

## Interview Tips

- **Explain Bucket Sort Advantage**: State *"Since maximum frequency is capped at array length $N$, we can index frequencies in an array of buckets, giving linear $\mathcal{O}(N)$ time which strictly beats $\mathcal{O}(N \log N)$ sorting and $\mathcal{O}(N \log k)$ heap approaches."*

---

## Similar Problems

1. [LeetCode #692: Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/)
2. [LeetCode #451: Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency/)
3. [LeetCode #973: K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/)

---

## Revision Notes

- Problem: Return top $k$ most frequent elements.
- Pattern: Bucket Sort (frequency as bucket index).
- Key Code: `vector<vector<int>> buckets(N + 1); buckets[freq].push_back(num);`
- Traversal: Loop backwards from `i = N` down to `1`.
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(N)$.
