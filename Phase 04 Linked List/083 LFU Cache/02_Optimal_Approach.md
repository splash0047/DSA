# LFU Cache

## Pattern Used

- **Pattern**: **Double Hash Map + Frequency Doubly Linked Lists**
- **Concept**:
  1. **Key Map**: `unordered_map<int, Node*> key_map` maps `key` to its DLL Node pointer in $\mathcal{O}(1)$ time.
  2. **Frequency Map**: `unordered_map<int, List*> freq_map` maps each frequency count $F$ to a dedicated Doubly Linked List storing all nodes with frequency $F$. Each list orders nodes by recency (LRU order).
  3. **`min_freq` Variable**: Maintains the current minimum frequency across all elements in the cache.

---

## Observation

1. When a key's frequency increments from $F \to F + 1$:
   - Remove node from `freq_map[F]` list.
   - If `freq_map[F]` becomes empty AND `min_freq == F`, increment `min_freq++`.
   - Add node to `freq_map[F + 1]` list.
2. When cache is full (`key_map.size() == capacity`):
   - Evict the LRU node from `freq_map[min_freq]` (the node right before `tail` of that frequency list).
   - Erase evicted node from `key_map` and delete pointer.
3. New key insertion:
   - Set `node->freq = 1`.
   - Set `min_freq = 1`.
   - Add node to `freq_map[1]`.

---

## Intuition

Group cached nodes into buckets based on their access frequency. Inside each frequency bucket, order nodes as an LRU Doubly Linked List. Maintain `min_freq` to immediately pinpoint the target bucket for eviction in $\mathcal{O}(1)$ time.

---

## Algorithm

### Node Structure
- `struct Node { int key, val, freq; Node *prev, *next; };`

### Doubly Linked List Helper Structure (`List`)
- Sentinel `head` and `tail` nodes.
- `addFront(Node*)`: Insert node right after `head` (MRU position).
- `removeNode(Node*)`: Remove node in $\mathcal{O}(1)$ time.
- `removeTail()`: Remove and return `tail->prev` (LRU node).

### `get(key)`
1. If `key` not in `key_map`, return `-1`.
2. `node = key_map[key]`.
3. Update frequency of `node` ($F \to F + 1$).
4. Return `node->val`.

### `put(key, value)`
1. If `capacity == 0`, return.
2. If `key` in `key_map`:
   - `node = key_map[key]`, `node->val = value`.
   - Update frequency of `node` ($F \to F + 1$).
3. Else:
   - If `key_map.size() == capacity`:
     - `lru_node = freq_map[min_freq]->removeTail()`.
     - `key_map.erase(lru_node->key)`, `delete lru_node`.
   - `new_node = new Node(key, value, 1)`.
   - `key_map[key] = new_node`.
   - `min_freq = 1`.
   - `freq_map[1]->addFront(new_node)`.

---

## Clean C++17 Solution

```cpp
#include <unordered_map>

class LFUCache {
private:
    struct Node {
        int key;
        int val;
        int freq;
        Node* prev;
        Node* next;
        Node(int k, int v) : key(k), val(v), freq(1), prev(nullptr), next(nullptr) {}
    };
    
    struct DoublyLinkedList {
        Node* head;
        Node* tail;
        int size;
        
        DoublyLinkedList() {
            head = new Node(0, 0);
            tail = new Node(0, 0);
            head->next = tail;
            tail->prev = head;
            size = 0;
        }
        
        void addFront(Node* node) {
            node->next = head->next;
            node->prev = head;
            head->next->prev = node;
            head->next = node;
            size++;
        }
        
        void removeNode(Node* node) {
            Node* prev_node = node->prev;
            Node* next_node = node->next;
            prev_node->next = next_node;
            next_node->prev = prev_node;
            size--;
        }
        
        Node* removeTail() {
            if (size == 0) return nullptr;
            Node* lru = tail->prev;
            removeNode(lru);
            return lru;
        }
    };
    
    int cap;
    int min_freq;
    std::unordered_map<int, Node*> key_map;
    std::unordered_map<int, DoublyLinkedList*> freq_map;
    
    void updateFreq(Node* node) {
        int old_freq = node->freq;
        DoublyLinkedList* old_list = freq_map[old_freq];
        old_list->removeNode(node);
        
        if (old_freq == min_freq && old_list->size == 0) {
            min_freq++;
        }
        
        node->freq++;
        int new_freq = node->freq;
        
        if (freq_map.find(new_freq) == freq_map.end()) {
            freq_map[new_freq] = new DoublyLinkedList();
        }
        
        freq_map[new_freq]->addFront(node);
    }

public:
    LFUCache(int capacity) : cap(capacity), min_freq(0) {}
    
    int get(int key) {
        auto it = key_map.find(key);
        if (it == key_map.end()) {
            return -1;
        }
        Node* node = it->second;
        updateFreq(node);
        return node->val;
    }
    
    void put(int key, int value) {
        if (cap == 0) return;
        
        auto it = key_map.find(key);
        if (it != key_map.end()) {
            Node* node = it->second;
            node->val = value;
            updateFreq(node);
        } else {
            if (key_map.size() == cap) {
                DoublyLinkedList* min_list = freq_map[min_freq];
                Node* lru_node = min_list->removeTail();
                key_map.erase(lru_node->key);
                delete lru_node;
            }
            
            Node* new_node = new Node(key, value);
            key_map[key] = new_node;
            min_freq = 1;
            
            if (freq_map.find(1) == freq_map.end()) {
                freq_map[1] = new DoublyLinkedList();
            }
            
            freq_map[1]->addFront(new_node);
        }
    }
};
```

---

## Dry Run

### Input Operations
`LFUCache(2)`, `put(1,1)`, `put(2,2)`, `get(1)`, `put(3,3)`, `get(2)`

### Execution Trace

1. `put(1,1)`: `min_freq = 1`. `freq_map[1]` = `[1:1]`.
2. `put(2,2)`: `min_freq = 1`. `freq_map[1]` = `[2:2] <-> [1:1]`.
3. `get(1)`: `(1:1)` freq becomes 2. `freq_map[1]` = `[2:2]`, `freq_map[2]` = `[1:1]`. `min_freq` remains `1`.
4. `put(3,3)`: Full capacity (2). Evict LRU from `freq_map[min_freq=1]` $\implies$ Evicts `(2:2)`. Insert `(3,3)` into `freq_map[1]`. `min_freq = 1`.
5. `get(2)`: Key `2` missing $\rightarrow$ Returns `-1`.

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(1)$ for both `get` and `put`.
  - All Hash Map lookups and DLL insertions/removals take strict $\mathcal{O}(1)$ time.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(\text{capacity})$
  - Stores up to `capacity` nodes.

---

## Why This is Optimal

- Solves LFU Cache design in optimal $\mathcal{O}(1)$ average time per operation.
- Uses optimal $\mathcal{O}(\text{capacity})$ memory.

---

## Common Mistakes

1. **Forgetting to Update `min_freq` on Frequency Increment**: If the list for `min_freq` becomes empty after moving a node $F \to F + 1$, `min_freq` MUST increment by 1 (`min_freq++`).
2. **Resetting `min_freq` on Existing Key Update**: `min_freq = 1` should ONLY be set when inserting a BRAND NEW key, never on updating an existing key!
