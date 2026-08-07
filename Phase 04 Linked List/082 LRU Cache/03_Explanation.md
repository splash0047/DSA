# Problem Summary

Design a Least Recently Used (LRU) Cache class supporting `get(key)` and `put(key, value)` in $\mathcal{O}(1)$ average time. The optimal approach uses a **Doubly Linked List + Hash Map**:
- **Doubly Linked List** (with dummy `head` & `tail` sentinels) maintains nodes ordered by recency. Nodes right after `head` are MRU; nodes right before `tail` are LRU.
- **Hash Map** (`unordered_map<int, Node*>`) maps keys directly to DLL node pointers for $\mathcal{O}(1)$ lookup.
This achieves $\mathcal{O}(1)$ time for both operations and $\mathcal{O}(\text{capacity})$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to design a **cache / eviction policy data structure** with $\mathcal{O}(1)$ lookup and $\mathcal{O}(1)$ order updates.
- Doubly Linked List + Hash Map Data Structure Design pattern.

---

## Important Clues

1. **"Least Recently Used (LRU) eviction"**: Recency ordering.
2. **"get and put must each run in O(1) time"**: Hash Map + Doubly Linked List requirement.

---

## Example

### Input Operations
`capacity = 2`, `put(1,1)`, `put(2,2)`, `get(1)`, `put(3,3)`, `get(2)`

### Visual Step-by-Step Progression

```text
DLL State Evolution:
1. put(1,1) -> Head <-> [1:1] <-> Tail
2. put(2,2) -> Head <-> [2:2] <-> [1:1] <-> Tail
3. get(1)   -> Head <-> [1:1] <-> [2:2] <-> Tail (Move [1:1] to MRU)
4. put(3,3) -> Evict LRU [2:2] -> Head <-> [3:3] <-> [1:1] <-> Tail
5. get(2)   -> Key 2 missing -> Return -1
```

---

## Alternative Solutions

### C++ `std::list` + Hash Map
- Use standard library `std::list<pair<int, int>>` and store list iterators `std::list::iterator` inside `unordered_map`.
- **Time Complexity**: $\mathcal{O}(1)$.
- **Space Complexity**: $\mathcal{O}(\text{capacity})$.

---

## Edge Cases

1. **Capacity = 1**: Evicts single element immediately on second `put`.
2. **Updating Existing Key**: `put(key, new_value)` updates value and moves node to MRU without increasing map size.
3. **Key Not Found**: `get(key)` returns `-1` without modifying DLL order.

---

## Interview Tips

- **Explain Why `key` Must Be Stored in DLL Node**: State *"Each DLL node stores BOTH key and value (`struct Node { int key; int val; }`). When capacity is exceeded, we delete the LRU node `tail->prev`. Having `key` inside the node enables us to erase `map.erase(lru->key)` in $\mathcal{O}(1)$ time."*

---

## Similar Problems

1. [LeetCode #460: LFU Cache](https://leetcode.com/problems/lfu-cache/)
2. [LeetCode #432: All O`one Data Structure](https://leetcode.com/problems/all-oone-data-structure/)
3. [LeetCode #380: Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/)

---

## Revision Notes

- Problem: Implement LRU Cache with $\mathcal{O}(1)$ `get` and `put`.
- Pattern: Hash Map (`unordered_map<int, Node*>`) + Doubly Linked List (`head`, `tail` sentinels).
- DLL Order: `head` $\leftrightarrow$ MRU $\leftrightarrow \dots \leftrightarrow$ LRU $\leftrightarrow$ `tail`.
- `get(key)`: Lookup in map. If found, `moveToHead(node)`, return `node->val`. Else `-1`.
- `put(key, val)`: If found, update val & `moveToHead`. Else if full, `popTail()` & `map.erase(lru->key)`. Create `new Node` & `addNode`.
- Optimal Complexity: Time $\mathcal{O}(1)$, Space $\mathcal{O}(\text{capacity})$.
