# 083. LFU Cache

- **Platform**: LeetCode
- **Problem Number**: #460
- **Difficulty**: Hard
- **URL**: [LeetCode #460 - LFU Cache](https://leetcode.com/problems/lfu-cache/)

---

## Problem Statement

Design and implement a data structure for a **Least Frequently Used (LFU)** cache.

Implement the `LFUCache` class:

- `LFUCache(int capacity)` Initializes the object with the `capacity` of the data structure.
- `int get(int key)` Gets the value of the `key` if the `key` exists in the cache. Otherwise, returns `-1`.
- `void put(int key, int value)` Update the value of the `key` if present, or inserts the `key` if not already present. When the cache reaches its `capacity`, it should invalidate and remove the **least frequently used** key before inserting a new item. For this problem, when there is a **tie** (i.e., two or more keys with the same frequency), the **least recently used** key would be invalidated.

To determine the least frequently used key, a **use counter** is maintained for each key in the cache. The key with the smallest `use counter` is the least frequently used key.

When a key is first inserted into the cache, its `use counter` is set to `1` (due to the `put` operation). The `use counter` for a key in the cache is incremented either a `get` or `put` operation is called on it.

The functions `get` and `put` must each run in $\mathcal{O}(1)$ average time complexity.

---

## Examples

### Example 1
```text
Input
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [1], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, 1, null, -1, 3, 4]

Explanation
// cnt(x) = use counter of x; freq(x) = frequency list
LFUCache lfu = new LFUCache(2);
lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1);      // return 1; cache=[1,2], cnt(1)=2, cnt(2)=1
lfu.put(3, 3);   // 2 is the LFU key, evicts 2; cache=[3,1], cnt(3)=1, cnt(1)=2
lfu.get(2);      // return -1 (not found)
lfu.get(1);      // return 1; cache=[1,3], cnt(1)=3, cnt(3)=1
lfu.put(4, 4);   // 3 is the LFU key, evicts 3; cache=[4,1], cnt(4)=1, cnt(1)=3
lfu.get(1);      // return 1; cache=[1,4], cnt(1)=4, cnt(4)=1
lfu.get(3);      // return -1 (not found)
lfu.get(4);      // return 4; cache=[4,1], cnt(4)=2, cnt(1)=4
```

---

## Constraints

- $1 \le \text{capacity} \le 10^4$
- $0 \le \text{key} \le 10^5$
- $0 \le \text{value} \le 10^9$
- At most $2 \times 10^5$ calls will be made to `get` and `put`.
