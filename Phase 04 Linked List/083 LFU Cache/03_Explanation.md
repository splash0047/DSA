# Problem Summary

Design a Least Frequently Used (LFU) Cache class supporting `get(key)` and `put(key, value)` in $\mathcal{O}(1)$ average time. On ties in frequency, the least recently used key is evicted. The optimal approach uses **Double Hash Map + Frequency Doubly Linked Lists**:
- `key_map`: `unordered_map<int, Node*>` maps `key` to its DLL `Node*` pointer.
- `freq_map`: `unordered_map<int, DoublyLinkedList*>` maps frequency count $F$ to a Doubly Linked List of all nodes with frequency $F$ (in LRU order).
- `min_freq`: integer tracking the current minimum frequency bucket for $\mathcal{O}(1)$ eviction.
This achieves $\mathcal{O}(1)$ time complexity for all operations and $\mathcal{O}(\text{capacity})$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to design an **LFU eviction policy data structure** with $\mathcal{O}(1)$ lookup, frequency tracking, and LRU tie-breaking.
- Double Hash Map + Frequency Buckets pattern.

---

## Important Clues

1. **"Least Frequently Used (LFU) eviction"**: Frequency-based cache eviction.
2. **"Tie-breaker: least recently used key"**: LRU order within same frequency bucket.
3. **"get and put must run in O(1) time"**: Double Hash Map + DLL requirement.

---

## Example

### Input Operations
`capacity = 2`, `put(1,1)`, `put(2,2)`, `get(1)`, `put(3,3)`, `get(2)`

### Visual Step-by-Step Progression

```text
Frequency Buckets:
freq = 1: [2:2] <-> [1:1] (min_freq = 1)

get(1) -> [1:1] moves to freq = 2:
freq = 1: [2:2] (min_freq = 1)
freq = 2: [1:1]

put(3,3) -> Evict LRU from freq_map[min_freq=1] -> Evicts [2:2]!
freq = 1: [3:3]
freq = 2: [1:1]

get(2) -> Missing -> Return -1
```

---

## Alternative Solutions

### Min-Heap Priority Queue (O(1) Get, O(log N) Put / Eviction)
- Use a Priority Queue ordering nodes by `(freq, timestamp)`.
- **Time Complexity**: `get` $\mathcal{O}(1)$, `put` $\mathcal{O}(\log N)$.
- **Space Complexity**: $\mathcal{O}(\text{capacity})$.

---

## Edge Cases

1. **Capacity = 0**: Handled immediately by returning on `put`.
2. **Multiple Nodes Same Frequency**: Disambiguated by DLL tail order (LRU eviction).
3. **`min_freq` Tracking**: Incremented when `freq_map[min_freq]` becomes empty; reset to `1` on brand new key insertion.

---

## Interview Tips

- **Compare LRU vs LFU Data Structure Architectures**: State *"While LRU Cache requires a single Doubly Linked List with a Hash Map, LFU Cache requires MULTIPLE Doubly Linked Lists (one list per frequency bucket) mapped by a secondary Hash Map `freq_map[freq]`, combined with a `min_freq` variable to achieve $\mathcal{O}(1)$ operations."*

---

## Similar Problems

1. [LeetCode #146: LRU Cache](https://leetcode.com/problems/lru-cache/)
2. [LeetCode #432: All O`one Data Structure](https://leetcode.com/problems/all-oone-data-structure/)

---

## Revision Notes

- Problem: Implement LFU Cache with $\mathcal{O}(1)$ `get` and `put`.
- Pattern: `key_map` (`map<key, Node*>`) + `freq_map` (`map<freq, DLL*>`) + `min_freq`.
- `updateFreq(node)`:
  - Remove from `freq_map[old_freq]`.
  - `if (old_freq == min_freq && list->empty) min_freq++`.
  - `node->freq++`, add to `freq_map[new_freq]`.
- `get(key)`: If in map, `updateFreq(node)`, return `node->val`. Else `-1`.
- `put(key, val)`: If found, update val & `updateFreq`. Else if full, `lru = freq_map[min_freq]->removeTail(); key_map.erase(lru->key);`. Set `min_freq = 1`, insert into `freq_map[1]`.
- Optimal Complexity: Time $\mathcal{O}(1)$, Space $\mathcal{O}(\text{capacity})$.
