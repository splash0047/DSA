# Problem Summary

Rearrange string `s` so that no two adjacent characters are identical. Return `""` if impossible. The optimal approach uses **Greedy Max-Heap with Previous Character Hold**:
- Check pigeonhole impossibility: `if (maxFreq > (N + 1) / 2) return "";`
- Push `{freq, char}` pairs into a Max-Heap.
- Maintain a `prev` character variable held out of the heap for 1 turn.
- Pop top character `curr`, append to answer, decrement frequency.
- Push `prev` back into heap if `prev.freq > 0`. Update `prev = curr`.
This rearranges `s` in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to **reorganize elements so no adjacent duplicates exist**.
- Greedy Max-Heap + Cooling / Holding Queue pattern.

---

## Important Clues

1. **"No two adjacent characters are the same"**: Alternate placement greedy strategy.
2. **"Return empty string if impossible"**: Impossibility threshold `maxFreq > (N + 1) / 2`.

---

## Example

### Input
`s = "aab"`

### Visual Step-by-Step Progression

```text
Frequencies: 'a': 2, 'b': 1
Max-Heap: [{'a', 2}, {'b', 1}]

Step 1: Pop 'a' -> string="a".  Hold 'a' (rem 1). Heap: [{'b', 1}]
Step 2: Pop 'b' -> string="ab". Release 'a' back -> Heap: [{'a', 1}]
Step 3: Pop 'a' -> string="aba".

Result: "aba"
```

---

## Alternative Solutions

### Even/Odd Index Frequency Interleaving ($\mathcal{O}(N)$ Time, $\mathcal{O}(26)$ Space)
- Count character frequencies. Fill even indices `0, 2, 4...` with the most frequent character first, then fill remaining even indices and odd indices `1, 3, 5...` with other characters.

---

## Edge Cases

1. **Impossible cases**: `s = "aaab"` (`maxFreq = 3 > (4+1)/2 = 2`) $\implies$ returns `""`.
2. **Single character**: `s = "a"` $\implies$ returns `"a"`.
3. **All unique characters**: `s = "abc"` $\implies$ returns `"abc"`.

---

## Interview Tips

- **Pigeonhole Principle Explanation**: State *"If any single character appears more than $\lceil N / 2 \rceil$ times, there are not enough other characters to separate them, making a valid rearrangement impossible."*

---

## Similar Problems

1. [LeetCode #1054: Distant Barcodes](https://leetcode.com/problems/distant-barcodes/)
2. [LeetCode #621: Task Scheduler](https://leetcode.com/problems/task-scheduler/)
3. [LeetCode #358: Rearrange String k Distance Apart](https://leetcode.com/problems/rearrange-string-k-distance-apart/)

---

## Revision Notes

- Problem: Reorganize string so no adjacent characters match.
- Pattern: Max-Heap + `prev` holding variable.
- Impossibility: `if (maxFreq > (N + 1) / 2) return "";`
- Logic: `pop curr -> ans += curr.char -> push prev if prev.freq > 0 -> prev = curr`.
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(1)$.
