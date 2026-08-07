# Problem Summary

Given an array of points `[x, y]`, return the $k$ closest points to the origin `(0, 0)`. The optimal approach uses a **Max-Heap of size $k$**:
- Use squared distance $x^2 + y^2$ to avoid floating-point math.
- Push `{squared_dist, point}` into a Max-Heap.
- If heap size exceeds $k$, pop the top (farthest) point.
- The $k$ points remaining in the heap are the $k$ closest points.
This achieves $\mathcal{O}(N \log k)$ time and $\mathcal{O}(k)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need the **$K$ closest / smallest** geometric items.
- Fixed-size Max-Heap pattern for Top $K$ closest points.

---

## Important Clues

1. **"K closest points to origin"**: Max-Heap of size $k$ algorithm.
2. **"Euclidean distance"**: Compare squared distances $x^2 + y^2$.

---

## Example

### Input
`points = [[1,3], [-2,2]]`, `k = 1`

### Visual Step-by-Step Progression

```text
Point [1, 3]  -> dist^2 = 1 + 9  = 10
Point [-2, 2] -> dist^2 = 4 + 4  = 8

Max-Heap of size 1:
1. Insert [1, 3]  (dist=10) -> Heap: [{10, [1,3]}]
2. Insert [-2, 2] (dist=8)  -> Heap: [{10, [1,3]}, {8, [-2,2]}]
   Heap size exceeds 1 -> Pop top {10, [1,3]}
   Heap becomes: [{8, [-2,2]}]

Result: [[-2, 2]]
```

---

## Alternative Solutions

### 1. Full Sorting ($\mathcal{O}(N \log N)$ Time, $\mathcal{O}(1)$ Space)
- Sort points by distance and take first $k$.

### 2. QuickSelect ($\mathcal{O}(N)$ Avg Time, $\mathcal{O}(1)$ Space)
- Partition array around pivot until pivot index is $k - 1$.

---

## Edge Cases

1. **$k = N$**: Returns all input points.
2. **Tie distances**: Points with identical distances to origin are handled naturally by C++ pair comparison.
3. **Negative coordinates**: $(-x)^2 = x^2$, handled automatically.

---

## Interview Tips

- **Explain Squared Distance Trick**: State *"We compare squared Euclidean distances ($x^2 + y^2$) directly rather than using `sqrt()` to eliminate floating-point precision loss and expensive square root operations."*

---

## Similar Problems

1. [LeetCode #215: Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)
2. [LeetCode #347: Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)
3. [LeetCode #692: Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/)

---

## Revision Notes

- Problem: Return $k$ closest points to $(0,0)$.
- Pattern: Max-Heap of size $k$ with squared distance $x^2 + y^2$.
- Code: `maxHeap.push({x*x + y*y, p}); if (maxHeap.size() > k) maxHeap.pop();`
- Return: Extract remaining $k$ points from heap.
- Optimal Complexity: Time $\mathcal{O}(N \log k)$, Space $\mathcal{O}(k)$.
