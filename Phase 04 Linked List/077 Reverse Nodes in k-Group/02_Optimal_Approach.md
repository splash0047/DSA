# Reverse Nodes in k-Group

## Pattern Used

- **Pattern**: **Iterative $K$-Group Subsegment Reversal**
- **Concept**: Use a `dummy` node pointing to `head`. Maintain a `groupPrev` pointer (node preceding current $K$-group).
  1. Find the $K^{\text{th}}$ node `kth` from `groupPrev`.
  2. If `kth == nullptr` ($< K$ nodes remaining), break loop.
  3. Record `groupNext = kth->next`.
  4. Reverse subsegment from `groupPrev->next` to `kth`.
  5. Connect `groupPrev->next` to `kth` and former group head to `groupNext`.
  6. Advance `groupPrev` to former group head.

---

## Observation

1. How to reverse a subsegment $A \rightarrow B \rightarrow C$ in-place?
   - Standard 3-pointer reversal algorithm (`prev`, `curr`, `next_node`).
2. Boundary Stitching:
   - Before reversal, the first node of the group will become the LAST node of the group after reversal!
   - Store `tmp = groupPrev->next` (this will be the tail of the reversed group).
   - After reversing $K$ nodes, set `tmp->next = groupNext` and `groupPrev->next = kth`.
   - Update `groupPrev = tmp`.

---

## Intuition

Walk through the list in chunks of size $k$. Check if $k$ full nodes exist in the current chunk. If yes, reverse that subsegment and reconnect the boundary links.

---

## Algorithm

1. `dummy = ListNode(0, head)`, `groupPrev = &dummy`.
2. Loop:
   a. Find $K^{\text{th}}$ node from `groupPrev`: `kth = getKthNode(groupPrev, k)`.
   b. If `kth == nullptr`, break.
   c. `groupNext = kth->next`.
   d. Reverse subsegment between `groupPrev->next` and `kth`:
      - `prev = groupNext`, `curr = groupPrev->next`.
      - While `curr != groupNext`:
        - `next_node = curr->next`.
        - `curr->next = prev`.
        - `prev = curr`.
        - `curr = next_node`.
   e. `tmp = groupPrev->next`.
   f. `groupPrev->next = kth`.
   g. `groupPrev = tmp`.
3. Return `dummy.next`.

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
private:
    ListNode* getKthNode(ListNode* curr, int k) {
        while (curr != nullptr && k > 0) {
            curr = curr->next;
            k--;
        }
        return curr;
    }
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        if (head == nullptr || k == 1) return head;
        
        ListNode dummy(0, head);
        ListNode* groupPrev = &dummy;
        
        while (true) {
            ListNode* kth = getKthNode(groupPrev, k);
            if (kth == nullptr) {
                break; // Fewer than k nodes remaining, keep as is
            }
            
            ListNode* groupNext = kth->next;
            
            // Reverse subsegment [groupPrev->next ... kth]
            ListNode* prev = groupNext;
            ListNode* curr = groupPrev->next;
            
            while (curr != groupNext) {
                ListNode* next_node = curr->next;
                curr->next = prev;
                prev = curr;
                curr = next_node;
            }
            
            // Reconnect boundaries
            ListNode* tmp = groupPrev->next;
            groupPrev->next = kth;
            groupPrev = tmp;
        }
        
        return dummy.next;
    }
};
```

---

## Dry Run

### Input
- `head = [1 -> 2 -> 3 -> 4 -> 5]`, `k = 2`

### Execution Trace

- `dummy = [0 -> 1 -> 2 -> 3 -> 4 -> 5]`
- `groupPrev = 0` (dummy)

1. **Group 1** (`kth = 2`, `groupNext = 3`):
   - Reverse `[1 -> 2]`: becomes `2 -> 1 -> 3`.
   - `0->next = 2`.
   - `groupPrev = 1`.
   - List state: `0 -> 2 -> 1 -> 3 -> 4 -> 5`
2. **Group 2** (`kth = 4`, `groupNext = 5`):
   - Reverse `[3 -> 4]`: becomes `4 -> 3 -> 5`.
   - `1->next = 4`.
   - `groupPrev = 3`.
   - List state: `0 -> 2 -> 1 -> 4 -> 3 -> 5`
3. **Group 3** (`kthNode` from `3` for $k=2$ is `nullptr` because only `5` remains):
   - Break loop!

### Result
- Output List: `2 -> 1 -> 4 -> 3 -> 5`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Each node is visited twice (once to find `kth`, once to reverse).

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Constant auxiliary space.

---

## Why This is Optimal

- Reverses nodes in $K$-groups in $\mathcal{O}(N)$ time.
- Uses zero extra memory ($\mathcal{O}(1)$ space), satisfying the follow-up.

---

## Common Mistakes

1. **Reversing Remainder $< K$ Nodes**: Forgetting to check if `kth == nullptr` before reversing, which accidentally reverses incomplete final groups.
2. **Losing Boundary Links**: Not setting `prev = groupNext` before reversing the subsegment.
