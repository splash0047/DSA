# LRU Cache

- **Problem Number**: 146
- **Platform**: LeetCode #146
- **Difficulty**: Medium
- **Pattern**: Vector/Array Search & Rearrangement

---

## Brute Force Intuition

Maintain a `std::vector<pair<int, int>> cache` storing `{key, value}` pairs.
- For `get(key)`: Search linearly through vector for `key`. If found, move `{key, value}` to the back of the vector (most recently used) and return `value`.
- For `put(key, value)`: Search linearly for `key`. If found, update value and move to back. If not found and vector size == capacity, remove element at index 0 (least recently used), then append `{key, value}` to the back.

---

## Algorithm

1. `get(key)`:
   - Loop `i` from `0` to `cache.size() - 1`:
     - If `cache[i].first == key`:
       - `val = cache[i].second`.
       - Erase `cache[i]`.
       - `cache.push_back({key, val})`.
       - Return `val`.
   - Return `-1`.
2. `put(key, value)`:
   - Loop `i` from `0` to `cache.size() - 1`:
     - If `cache[i].first == key`:
       - Erase `cache[i]`.
       - `cache.push_back({key, value})`.
       - Return.
   - If `cache.size() == capacity`:
     - Erase `cache[0]`.
   - `cache.push_back({key, value})`.

---

## Code

```cpp
#include <vector>
#include <utility>

class LRUCache {
private:
    int cap;
    std::vector<std::pair<int, int>> cache;
public:
    LRUCache(int capacity) {
        cap = capacity;
    }
    
    int get(int key) {
        for (size_t i = 0; i < cache.size(); ++i) {
            if (cache[i].first == key) {
                int val = cache[i].second;
                cache.erase(cache.begin() + i);
                cache.push_back({key, val});
                return val;
            }
        }
        return -1;
    }
    
    void put(int key, int value) {
        for (size_t i = 0; i < cache.size(); ++i) {
            if (cache[i].first == key) {
                cache.erase(cache.begin() + i);
                cache.push_back({key, value});
                return;
            }
        }
        
        if (cache.size() == cap) {
            cache.erase(cache.begin()); // Evict LRU
        }
        cache.push_back({key, value});
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$ per `get` and `put` call.
  - Linear scan and vector `erase` take $\mathcal{O}(N)$ time.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(\text{capacity})$
  - Stores up to `capacity` key-value pairs.

---

## Why This Approach Is Not Optimal

Vector linear searches and node erasures take $\mathcal{O}(N)$ time, violating the mandatory $\mathcal{O}(1)$ average runtime constraint. Using a **Doubly Linked List + Hash Map**, we achieve true $\mathcal{O}(1)$ time complexity for both `get` and `put`.
