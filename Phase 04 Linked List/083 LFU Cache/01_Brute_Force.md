# LFU Cache

- **Problem Number**: 460
- **Platform**: LeetCode #460
- **Difficulty**: Hard
- **Pattern**: Min-Heap / Priority Queue with Timestamp

---

## Brute Force Intuition

Store cached elements in a Hash Map `unordered_map<int, CacheNode>` where each node tracks `{key, value, freq, timestamp}`. Maintain a global `time` counter incremented on every `get` or `put` operation. When capacity is full, perform a linear scan over all cached keys to find the key with the **minimum frequency** (breaking ties by **minimum timestamp** for LRU eviction).

---

## Algorithm

1. `get(key)`:
   - If `key` not in `map`, return `-1`.
   - Increment `map[key].freq++`.
   - Update `map[key].timestamp = ++timer`.
   - Return `map[key].value`.
2. `put(key, value)`:
   - If `key` exists in `map`:
     - Update `map[key].value = value`.
     - `map[key].freq++`.
     - `map[key].timestamp = ++timer`.
     - Return.
   - If `map.size() == capacity`:
     - Linear scan over `map` to find key with `min_freq` (and `min_timestamp` on ties).
     - Erase that key from `map`.
   - Insert new key into `map` with `freq = 1` and `timestamp = ++timer`.

---

## Code

```cpp
#include <unordered_map>
#include <climits>

class LFUCache {
private:
    struct CacheNode {
        int key;
        int value;
        int freq;
        int timestamp;
    };
    
    int cap;
    int timer;
    std::unordered_map<int, CacheNode> map;
    
public:
    LFUCache(int capacity) : cap(capacity), timer(0) {}
    
    int get(int key) {
        auto it = map.find(key);
        if (it == map.end()) {
            return -1;
        }
        it->second.freq++;
        it->second.timestamp = ++timer;
        return it->second.value;
    }
    
    void put(int key, int value) {
        if (cap == 0) return;
        
        auto it = map.find(key);
        if (it != map.end()) {
            it->second.value = value;
            it->second.freq++;
            it->second.timestamp = ++timer;
            return;
        }
        
        if (map.size() == cap) {
            // Linear scan to find key with minimum freq and oldest timestamp
            int lfu_key = -1;
            int min_freq = INT_MAX;
            int min_time = INT_MAX;
            
            for (const auto& pair : map) {
                const CacheNode& node = pair.second;
                if (node.freq < min_freq || (node.freq == min_freq && node.timestamp < min_time)) {
                    min_freq = node.freq;
                    min_time = node.timestamp;
                    lfu_key = pair.first;
                }
            }
            
            map.erase(lfu_key); // Evict LFU
        }
        
        map[key] = {key, value, 1, ++timer};
    }
};
```

---

## Time Complexity

- **Time Complexity**:
  - `get`: $\mathcal{O}(1)$ average.
  - `put`: $\mathcal{O}(N)$ when eviction triggers (linear scan over `capacity` elements).

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(\text{capacity})$
  - Stores up to `capacity` nodes.

---

## Why This Approach Is Not Optimal

Eviction requires an $\mathcal{O}(N)$ linear scan over all cached keys, violating the strict $\mathcal{O}(1)$ average time requirement for `put`. Using **Double Hash Map + Frequency Doubly Linked Lists**, we achieve true $\mathcal{O}(1)$ time complexity for both `get` and `put`.
