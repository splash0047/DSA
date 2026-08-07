# Merge k Sorted Lists

## Pattern Used

- **Pattern**: **Min-Heap (Priority Queue) / Divide and Conquer**
- **Concept**: Maintain a Min-Heap of size at most $K$ containing the current head nodes of all non-empty lists. Pop the minimum node, attach it to `tail->next`, and push `node->next` into the heap.

---

## Observation

1. At any step during merging, the smallest available node among all lists MUST be among the current head nodes of the $K$ lists!
2. A Min-Heap of size $K$ allows extracting the minimum element in $\mathcal{O}(\log K)$ time.
3. Total nodes across all lists = $N$. Each node is pushed into and popped from the Min-Heap exactly once $\implies \mathcal{O}(N \log K)$ overall time.

---

## Intuition

Keep track of the "frontier" head of each list using a Min-Heap. Pluck the smallest node, attach it to our merged list, and advance that specific list's head into the Min-Heap.

---

## Algorithm

1. Define custom comparator for Min-Heap: `a->val > b->val`.
2. Initialize Min-Heap `pq`.
3. For each `head` in `lists`:
   - If `head != nullptr`, push `head` into `pq`.
4. `dummy = ListNode(0)`, `tail = &dummy`.
5. While `pq` is not empty:
   a. `min_node = pq.top()`, `pq.pop()`.
   b. `tail->next = min_node`.
   c. `tail = tail->next`.
   d. If `min_node->next != nullptr`:
      - `pq.push(min_node->next)`.
6. Return `dummy.next`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <queue>

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
private:
    struct Compare {
        bool operator()(const ListNode* a, const ListNode* b) const {
            return a->val > b->val; // Min-Heap
        }
    };
public:
    ListNode* mergeKLists(const std::vector<ListNode*>& lists) {
        std::priority_queue<ListNode*, std::vector<ListNode*>, Compare> pq;
        
        // Push initial heads into min-heap
        for (ListNode* head : lists) {
            if (head != nullptr) {
                pq.push(head);
            }
        }
        
        ListNode dummy(0);
        ListNode* tail = &dummy;
        
        while (!pq.empty()) {
            ListNode* min_node = pq.top();
            pq.pop();
            
            tail->next = min_node;
            tail = tail->next;
            
            if (min_node->next != nullptr) {
                pq.push(min_node->next);
            }
        }
        
        return dummy.next;
    }
};
```

---

## Dry Run

### Input
- `lists = [[1 -> 4 -> 5], [1 -> 3 -> 4], [2 -> 6]]`

### Execution Trace

- Push heads `{1 (L1), 1 (L2), 2 (L3)}` into Min-Heap (Size 3).

| Step | `pq.top()` (val) | Attached Node | Pushed Next Node | Heap Size |
| :--- | :--- | :--- | :--- | :--- |
| 1 | `1` (L1) | Node `1` (L1) | `4` (L1) | 3 |
| 2 | `1` (L2) | Node `1` (L2) | `3` (L2) | 3 |
| 3 | `2` (L3) | Node `2` (L3) | `6` (L3) | 3 |
| 4 | `3` (L2) | Node `3` (L2) | `4` (L2) | 3 |
| 5 | `4` (L1) | Node `4` (L1) | `5` (L1) | 3 |
| 6 | `4` (L2) | Node `4` (L2) | `nullptr` | 2 |
| 7 | `5` (L1) | Node `5` (L1) | `nullptr` | 1 |
| 8 | `6` (L3) | Node `6` (L3) | `nullptr` | 0 (Empty) |

### Result
- Merged List: `1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N \log K)$
  - Each of the $N$ nodes is inserted and removed from a priority queue of size at most $K$ in $\mathcal{O}(\log K)$ time.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(K)$
  - Min-Heap stores at most $K$ node pointers.

---

## Why This is Optimal

- Solves $K$-way list merge in optimal $\mathcal{O}(N \log K)$ time.
- Uses minimal $\mathcal{O}(K)$ auxiliary heap memory.

---

## Common Mistakes

1. **Incorrect Priority Queue Comparator**: Writing `a->val < b->val` instead of `a->val > b->val`. Standard `std::priority_queue` is a Max-Heap by default! We need `>` for a Min-Heap.
2. **Pushing `nullptr` Heads**: Pushing empty list heads into priority queue causing null pointer dereference on `pq.top()`.
