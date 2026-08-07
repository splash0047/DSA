# Problem Summary

Given an integer array `nums`, sort it in **increasing** order of frequency. If two values have equal frequency, sort them in **decreasing** order of value. The optimal approach uses a **Min-Heap with Custom Comparator**:
- Build frequency map `freqMap`.
- Push `{freq, val}` into a priority queue configured to pop lowest frequency first, and highest value first on ties.
- Pop from priority queue and append values into `ans` array according to their frequencies.
This achieves $\mathcal{O}(N + U \log U)$ time and $\mathcal{O}(U)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to **sort an array by frequency** with custom tie-breaker rules.
- Multi-criteria custom heap / priority queue pattern.

---

## Important Clues

1. **"Increasing order based on frequency"**: Min-heap on frequency.
2. **"Multiple values same frequency -> decreasing value order"**: Secondary max-heap tie-breaker.

---

## Example

### Input
`nums = [2, 3, 1, 3, 2]`

### Visual Step-by-Step Progression

```text
1. Frequencies:
   1 -> 1
   2 -> 2
   3 -> 2

2. Priority Queue Priority Order:
   Top 1: {freq: 1, val: 1}
   Top 2: {freq: 2, val: 3} (3 comes before 2 because value is larger)
   Top 3: {freq: 2, val: 2}

3. Output Construction:
   - Pop {1, 1} -> [1]
   - Pop {2, 3} -> [1, 3, 3]
   - Pop {2, 2} -> [1, 3, 3, 2, 2]

Result: [1, 3, 3, 2, 2]
```

---

## Alternative Solutions

### Custom Lambda Sorting ($\mathcal{O}(N \log N)$ Time, $\mathcal{O}(N)$ Space)
- Use `std::sort` on `nums` with lambda comparator `[&](int a, int b) { return freq[a] != freq[b] ? freq[a] < freq[b] : a > b; }`.

---

## Edge Cases

1. **All elements have same frequency**: Sorted in strictly descending order.
2. **All elements unique**: Sorted in strictly descending order.
3. **Negative numbers**: Handled naturally by comparator `a > b`.

---

## Interview Tips

- **Explain C++ Priority Queue Comparator Sign**: State *"In C++ `priority_queue`, the custom functor returns `true` when the first argument should be placed AFTER the second argument. Hence `a.freq > b.freq` makes smaller frequencies pop first."*

---

## Similar Problems

1. [LeetCode #451: Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency/)
2. [LeetCode #347: Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)
3. [LeetCode #692: Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/)

---

## Revision Notes

- Problem: Sort by increasing frequency, decreasing value tie-breaker.
- Pattern: Priority Queue with custom struct comparator.
- Comparator: `a.freq != b.freq ? a.freq > b.freq : a.val < b.val`.
- Construction: Pop `{freq, val}`, append `val` `freq` times to result.
- Optimal Complexity: Time $\mathcal{O}(N + U \log U)$, Space $\mathcal{O}(U)$.
