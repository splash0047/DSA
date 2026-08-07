# Problem Summary

Simulate smashing the two heaviest stones in an array `stones` until at most 1 stone remains. If remaining weights $x \le y$ smash, weight $y - x$ is left. The optimal approach uses a **Max-Heap (Priority Queue)**:
- Push all stone weights into `std::priority_queue<int> maxHeap`.
- While `maxHeap.size() > 1`:
  - Pop `y = maxHeap.top()` and `x = maxHeap.top()`.
  - If `y > x`, push `y - x` back into `maxHeap`.
- Return `maxHeap.empty() ? 0 : maxHeap.top()`.
This simulates the stone smashing process in $\mathcal{O}(N \log N)$ time and $\mathcal{O}(N)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You repeatedly need the **two largest / smallest elements** from a dynamic collection.
- Game simulation with max element extraction pattern.

---

## Important Clues

1. **"Choose the heaviest two stones"**: Max-Heap priority queue.
2. **"Repeat until at most one stone remains"**: While loop `maxHeap.size() > 1`.

---

## Example

### Input
`stones = [2, 7, 4, 1, 8, 1]`

### Visual Step-by-Step Progression

```text
Initial Heap: [8, 7, 4, 2, 1, 1]

Smash 8 and 7 -> diff = 1 -> Heap: [4, 2, 1, 1, 1]
Smash 4 and 2 -> diff = 2 -> Heap: [2, 1, 1, 1]
Smash 2 and 1 -> diff = 1 -> Heap: [1, 1, 1]
Smash 1 and 1 -> diff = 0 -> Heap: [1]

Result: 1
```

---

## Alternative Solutions

### Repeated Array Sorting ($\mathcal{O}(N^2 \log N)$ Time, $\mathcal{O}(\log N)$ Space)
- Sort vector on every iteration to access two largest elements.

---

## Edge Cases

1. **Single Stone**: `stones = [1]` $\implies$ returns `1`.
2. **All Stones Destroyed**: `stones = [2, 2]` $\implies$ returns `0`.
3. **Identical Weights**: `stones = [3, 3, 3]` $\implies$ returns `3`.

---

## Interview Tips

- **Heapify Construction Optimization**: Mention that initializing `priority_queue<int> maxHeap(stones.begin(), stones.end())` uses linear time `std::make_heap` ($\mathcal{O}(N)$) rather than pushing elements one-by-one ($\mathcal{O}(N \log N)$).

---

## Similar Problems

1. [LeetCode #1167: Minimum Cost to Connect Sticks](https://leetcode.com/problems/minimum-cost-to-connect-sticks/)
2. [LeetCode #215: Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)

---

## Revision Notes

- Problem: Repeatedly smash 2 heaviest stones, return last stone weight.
- Pattern: Max-Heap.
- Loop condition: `while (maxHeap.size() > 1)`.
- Core step: `y = maxHeap.top(); pop(); x = maxHeap.top(); pop(); if (y > x) maxHeap.push(y - x);`
- Optimal Complexity: Time $\mathcal{O}(N \log N)$, Space $\mathcal{O}(N)$.
