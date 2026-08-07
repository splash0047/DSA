# Partition List

## Pattern Used

- **Pattern**: **Two Dummy Sentinel Lists (In-Place Pointer Partitioning)**
- **Concept**: Maintain two dummy head nodes: `less_dummy` (for nodes $< x$) and `greater_dummy` (for nodes $\ge x$). Traverse the original list, splicing each node onto the tail of `less_dummy` or `greater_dummy`. Finally, stitch `less_tail->next = greater_dummy.next` and nullify `greater_tail->next = nullptr`.

---

## Observation

1. Maintaining two separate tail pointers `less_tail` and `greater_tail` automatically preserves the original relative order of nodes in both partitions.
2. Dummy sentinel nodes eliminate special-case code for empty partitions.
3. Crucial Final Step: Disconnect `greater_tail->next = nullptr` to prevent unintended pointer cycles!

---

## Intuition

Filter the original list into two sub-lists (nodes $< x$ and nodes $\ge x$), then append the second sub-list to the end of the first sub-list.

---

## Algorithm

1. `less_dummy = ListNode(0)`, `less_tail = &less_dummy`.
2. `greater_dummy = ListNode(0)`, `greater_tail = &greater_dummy`.
3. `curr = head`.
4. While `curr != nullptr`:
   a. If `curr->val < x`:
      - `less_tail->next = curr`.
      - `less_tail = less_tail->next`.
   b. Else:
      - `greater_tail->next = curr`.
      - `greater_tail = greater_tail->next`.
   c. `curr = curr->next`.
5. `greater_tail->next = nullptr` (Prevent cycle).
6. `less_tail->next = greater_dummy.next` (Stitch sub-lists together).
7. Return `less_dummy.next`.

---

## Clean C++17 Solution

```cpp
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        ListNode less_dummy(0);
        ListNode greater_dummy(0);
        
        ListNode* less_tail = &less_dummy;
        ListNode* greater_tail = &greater_dummy;
        
        ListNode* curr = head;
        while (curr != nullptr) {
            if (curr->val < x) {
                less_tail->next = curr;
                less_tail = less_tail->next;
            } else {
                greater_tail->next = curr;
                greater_tail = greater_tail->next;
            }
            curr = curr->next;
        }
        
        // Prevent cycle at the end of the greater partition
        greater_tail->next = nullptr;
        
        // Connect less list to greater list
        less_tail->next = greater_dummy.next;
        
        return less_dummy.next;
    }
};
```

---

## Dry Run

### Input
- `head = [1 -> 4 -> 3 -> 2 -> 5 -> 2]`, `x = 3`

### Execution Trace

- `less_list`: `1 -> 2 -> 2`
- `greater_list`: `4 -> 3 -> 5`

1. Set `greater_tail->next = nullptr` (`5->next = nullptr`).
2. Connect `less_tail->next = greater_dummy.next` (`2->next = 4`).

### Result
- Output List: `1 -> 2 -> 2 -> 4 -> 3 -> 5`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Single pass over $N$ nodes.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Constant auxiliary space (rewires existing node pointers in-place).

---

## Why This is Optimal

- Partitioning preserves original relative order in linear $\mathcal{O}(N)$ time.
- Uses zero extra memory ($\mathcal{O}(1)$ space).

---

## Common Mistakes

1. **Cycle Creation**: Forgetting to execute `greater_tail->next = nullptr`. If the last node in the original list went to the `less` partition, the last node in `greater` still points to a node now in `less`, creating a cycle!
2. **Losing Relative Order**: Attempting to swap values in-place using quicksort partitioning, which destroys relative element ordering.
