# Problem Summary

Find the smallest numerical range `[a, b]` that includes at least one number from each of `k` sorted lists. The optimal approach uses a **Min-Heap of size $k$**:
- Insert the $0^{th}$ element of each list into a Min-Heap and track `maxVal`.
- The current range is `[minHeap.top().val, maxVal]`.
- Pop `curr = minHeap.top()`, update best range.
- If `curr` has a next element in its list, push it to `minHeap` and update `maxVal`.
- If any list gets exhausted, break and return `ans`.
This evaluates the smallest range in $\mathcal{O}(N \log k)$ time and $\mathcal{O}(k)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to find a **covering range across $K$ sorted sequences**.
- Min-Heap K-Pointer Range Tracking pattern.

---

## Important Clues

1. **"Range including at least one number from each of k lists"**: K-Way covering range.
2. **"Lists are sorted in non-decreasing order"**: Heap pointer progression.

---

## Example

### Input
`nums = [[4, 10, 15], [0, 9, 12], [5, 18, 22]]`

### Visual Step-by-Step Progression

```text
Heap of size 3 (holding 1 item per list):
Init: [0(L1), 4(L0), 5(L2)] -> maxVal=5. Range = [0, 5] (len 5)
Pop 0 -> Add 9(L1) -> Heap: [4(L0), 5(L2), 9(L1)] -> maxVal=9. Range = [4, 9] (len 5)
Pop 4 -> Add 10(L0) -> Heap: [5(L2), 9(L1), 10(L0)] -> maxVal=10. Range = [5, 10] (len 5)
...

Smallest range found = [20, 24] (len 4)
```

---

## Alternative Solutions

### Flatten + Sliding Window ($\mathcal{O}(N \log N)$ Time, $\mathcal{O}(N)$ Space)
- Merge all elements into a single array of pairs `{val, list_idx}`, sort, and run a 2-pointer sliding window.

---

## Edge Cases

1. **$k = 1$**: Single list $\implies$ range is `[nums[0][0], nums[0][0]]` (len 0).
2. **Lists of single elements**: Handled correctly on initial step.
3. **Equal element values**: Handled seamlessly by heap.

---

## Interview Tips

- **Explain Pointer Progression Logic**: State *"To shrink the range `[min_val, max_val]`, we MUST advance the pointer of `min_val` because advancing any other pointer can only increase `max_val` and widen the range."*

---

## Similar Problems

1. [LeetCode #23: Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)
2. [LeetCode #76: Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)
3. [LeetCode #378: Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/)

---

## Revision Notes

- Problem: Smallest range covering $\ge 1$ element from each of $k$ sorted lists.
- Pattern: Min-Heap of size $k$ tracking `minVal` and `maxVal`.
- Loop: `curr = minHeap.top(); pop(); minVal = curr.val; updateBestRange(); push(nextVal); update maxVal;`
- Stop: Break when any list is exhausted.
- Optimal Complexity: Time $\mathcal{O}(N \log k)$, Space $\mathcal{O}(k)$.
