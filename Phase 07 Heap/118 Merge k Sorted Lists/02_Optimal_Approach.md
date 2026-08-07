# Merge k Sorted Lists

## Pattern Used

- **Pattern**: **Min-Heap (K-Way Merge)**
- **Concept**:
  - Insert the head node of each of the $k$ lists into a Min-Heap.
  - The custom heap comparator compares `ListNode*` by `node->val`.
  - While heap is not empty:
    - Pop the node with the smallest value `curr`.
    - Attach `curr` to our merged list.
    - If `curr->next != nullptr`, push `curr->next` into the Min-Heap.

---

## Observation

1. Since every input list is already sorted, the global minimum among all remaining unmerged nodes MUST be at the head of one of the $k$ lists!
2. Maintaining a Min-Heap of current list heads allows us to find and extract the smallest remaining node in logarithmic $\mathcal{O}(\log k)$ time.

---

## Intuition

Imagine $k$ sorted lines of people. You want to merge them into 1 line:
- Take the person at the front of each of the $k$ lines and have them stand in a small waiting room (Min-Heap of size $k$).
- Pick the shortest person in the room and move them to the final line.
- Whoever was behind that person in their original line now steps into the waiting room.
- Repeat until the room is empty.

---

## Algorithm

1. Define custom struct comparator `Compare`:
   - `bool operator()(ListNode* a, ListNode* b) { return a->val > b->val; }`
2. Instantiate `std::priority_queue<ListNode*, vector<ListNode*>, Compare> minHeap`.
3. Push non-null head of each list in `lists` into `minHeap`.
4. Create `ListNode dummy(0)` and pointer `tail = &dummy`.
5. While `!minHeap.empty()`:
   a. `ListNode* smallest = minHeap.top(); minHeap.pop();`
   b. `tail->next = smallest;`
   c. `tail = tail->next;`
   d. If `smallest->next != nullptr`:
      - `minHeap.push(smallest->next);`
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

struct Compare {
    bool operator()(ListNode* a, ListNode* b) {
        return a->val > b->val; // Min-heap on node value
    }
};

class Solution {
public:
    ListNode* mergeKLists(std::vector<ListNode*>& lists) {
        std::priority_queue<ListNode*, std::vector<ListNode*>, Compare> minHeap;
        
        // Push heads of all non-empty lists into min-heap
        for (ListNode* head : lists) {
            if (head != nullptr) {
                minHeap.push(head);
            }
        }
        
        ListNode dummy(0);
        ListNode* tail = &dummy;
        
        while (!minHeap.empty()) {
            ListNode* curr = minHeap.top();
            minHeap.pop();
            
            tail->next = curr;
            tail = tail->next;
            
            if (curr->next != nullptr) {
                minHeap.push(curr->next);
            }
        }
        
        return dummy.next;
    }
};
```

---

## Dry Run

### Input
- `lists = [[1->4->5], [1->3->4], [2->6]]`

### Execution Trace

1. Init Min-Heap: Push heads `[1(List1), 1(List2), 2(List3)]`.
2. Pop `1(List1)` $\implies$ `tail->next = 1`. Push `4(List1)`. Heap: `[1(L2), 2(L3), 4(L1)]`.
3. Pop `1(List2)` $\implies$ `tail->next = 1`. Push `3(List2)`. Heap: `[2(L3), 3(L2), 4(L1)]`.
4. Pop `2(List3)` $\implies$ `tail->next = 2`. Push `6(List3)`. Heap: `[3(L2), 4(L1), 6(L3)]`.
5. Pop `3(List2)` $\implies$ `tail->next = 3`. Push `4(List2)`. Heap: `[4(L1), 4(L2), 6(L3)]`.
6. Pop `4(L1)` $\implies$ `tail->next = 4`. Push `5(L1)`.
7. Pop `4(L2)` $\implies$ `tail->next = 4`.
8. Pop `5(L1)` $\implies$ `tail->next = 5`.
9. Pop `6(L3)` $\implies$ `tail->next = 6`.

### Result
- Output Linked List: `1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N \log k)$
  - Where $N$ is total number of nodes across all $k$ lists.
  - Building initial heap takes $\mathcal{O}(k \log k)$.
  - Each of the $N$ node extractions and subsequent pushes takes $\mathcal{O}(\log k)$ time.
  - Total time complexity: $\mathcal{O}(N \log k)$.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(k)$
  - Priority queue stores at most $k$ node pointers at any time.
  - Input list nodes are re-linked in-place.

---

## Why This is Optimal

- Reduces comparison complexity from $\mathcal{O}(N \cdot k)$ (linear scan over $k$ list heads) to $\mathcal{O}(N \log k)$ using a priority queue.
- Re-links nodes in-place without allocating new linked list nodes.

---

## Common Mistakes

1. **Pushing `nullptr` Heads**: Forgetting `if (head != nullptr)` before pushing initial heads into heap.
2. **Incorrect Heap Comparator**: Returning `a->val < b->val` creates a Max-Heap instead of a Min-Heap.
