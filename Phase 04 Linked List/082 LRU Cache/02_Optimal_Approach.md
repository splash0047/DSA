# LRU Cache

## Pattern Used

- **Pattern**: **Doubly Linked List + Hash Map Design**
- **Concept**:
  1. **Doubly Linked List**: Stores `{key, value}` pairs ordered by usage frequency. Nodes near `head` are **Most Recently Used (MRU)**; nodes near `tail` are **Least Recently Used (LRU)**. Doubly linked nodes allow $\mathcal{O}(1)$ node deletion and insertion.
  2. **Hash Map**: `unordered_map<int, Node*> map` maps `key` directly to its corresponding `Node*` pointer in the doubly linked list, enabling $\mathcal{O}(1)$ lookup.

---

## Observation

1. Why a Doubly Linked List?
   - Deleting an arbitrary node from a Doubly Linked List when given its pointer takes $\mathcal{O}(1)$ time.
   - Inserting a node right after `head` (MRU position) takes $\mathcal{O}(1)$ time.
2. Why store `key` inside the DLL node?
   - When capacity is full, we must evict the LRU node right before `tail`. Having `key` stored inside the node allows us to erase its entry from the Hash Map `map.erase(lru->key)` in $\mathcal{O}(1)$ time!

---

## Intuition

Combine a Hash Map for $\mathcal{O}(1)$ key-to-node lookup with a Doubly Linked List for $\mathcal{O}(1)$ node reordering (moving accessed items to the front and evicting items from the back).

---

## Algorithm

1. Sentinel Nodes: `head` and `tail` dummy nodes connected to each other (`head->next = tail`, `tail->prev = head`).
2. Helper `addNode(Node* node)`: Insert `node` immediately after `head` (MRU position).
3. Helper `removeNode(Node* node)`: Detach `node` from list: `node->prev->next = node->next`, `node->next->prev = node->prev`.
4. `get(key)`:
   - If `key` not in `map`, return `-1`.
   - `node = map[key]`.
   - Move `node` to MRU: `removeNode(node)`, `addNode(node)`.
   - Return `node->val`.
5. `put(key, value)`:
   - If `key` exists in `map`:
     - `node = map[key]`, update `node->val = value`.
     - `removeNode(node)`, `addNode(node)`.
   - Else:
     - If `map.size() == capacity`:
       - `lru = tail->prev`.
       - `removeNode(lru)`, `map.erase(lru->key)`, `delete lru`.
     - `new_node = new Node(key, value)`.
     - `addNode(new_node)`, `map[key] = new_node`.

---

## Clean C++17 Solution

```cpp
#include <unordered_map>

class LRUCache {
private:
    struct Node {
        int key;
        int val;
        Node* prev;
        Node* next;
        Node(int k, int v) : key(k), val(v), prev(nullptr), next(nullptr) {}
    };
    
    int cap;
    std::unordered_map<int, Node*> map;
    Node* head;
    Node* tail;
    
    void addNode(Node* node) {
        node->next = head->next;
        node->prev = head;
        head->next->prev = node;
        head->next = node;
    }
    
    void removeNode(Node* node) {
        Node* prev_node = node->prev;
        Node* next_node = node->next;
        prev_node->next = next_node;
        next_node->prev = prev_node;
    }
    
    void moveToHead(Node* node) {
        removeNode(node);
        addNode(node);
    }
    
    Node* popTail() {
        Node* res = tail->prev;
        removeNode(res);
        return res;
    }

public:
    LRUCache(int capacity) : cap(capacity) {
        head = new Node(0, 0);
        tail = new Node(0, 0);
        head->next = tail;
        tail->prev = head;
    }
    
    int get(int key) {
        auto it = map.find(key);
        if (it == map.end()) {
            return -1;
        }
        Node* node = it->second;
        moveToHead(node);
        return node->val;
    }
    
    void put(int key, int value) {
        auto it = map.find(key);
        if (it != map.end()) {
            Node* node = it->second;
            node->val = value;
            moveToHead(node);
        } else {
            if (map.size() == cap) {
                Node* lru = popTail();
                map.erase(lru->key);
                delete lru;
            }
            Node* new_node = new Node(key, value);
            map[key] = new_node;
            addNode(new_node);
        }
    }
};
```

---

## Dry Run

### Input Operations
`LRUCache(2)`, `put(1,1)`, `put(2,2)`, `get(1)`, `put(3,3)`, `get(2)`

### Execution Trace

1. `LRUCache(2)`: Dummy `head <-> tail`.
2. `put(1,1)`: Add `(1,1)`. List: `head <-> (1,1) <-> tail`.
3. `put(2,2)`: Add `(2,2)`. List: `head <-> (2,2) <-> (1,1) <-> tail`.
4. `get(1)`: Return `1`. Move `(1,1)` to head. List: `head <-> (1,1) <-> (2,2) <-> tail`.
5. `put(3,3)`: Capacity full (2). Evict LRU `tail->prev` = `(2,2)`. Add `(3,3)`. List: `head <-> (3,3) <-> (1,1) <-> tail`.
6. `get(2)`: Key `2` not in map $\rightarrow$ Return `-1`.

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(1)$ for both `get` and `put`.
  - Hash Map lookup is $\mathcal{O}(1)$ average; Doubly Linked List insertion/deletion is strictly $\mathcal{O}(1)$.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(\text{capacity})$
  - Stores up to `capacity` nodes in Hash Map and Doubly Linked List.

---

## Why This is Optimal

- Meets the strict $\mathcal{O}(1)$ average time requirement for all operations.
- Uses optimal $\mathcal{O}(\text{capacity})$ auxiliary memory.

---

## Common Mistakes

1. **Forgetting `key` inside `Node` struct**: Storing only `val` in `Node` struct makes it impossible to delete the evicted LRU key from the Hash Map in $\mathcal{O}(1)$ time.
2. **Double Free / Memory Leaks**: Forgetting `delete lru` after removing from doubly linked list.
