# Reorder List

## Pattern Used

- **Pattern**: **Find Mid + Reverse Second Half + Interleave Merge**
- **Concept**:
  1. **Find Middle**: Use Fast & Slow pointers (`slow`, `fast`) to find the midpoint of the linked list.
  2. **Reverse Second Half**: Reverse the linked list starting from `slow->next` to get the tail portion in reverse order. Disconnect `slow->next = nullptr`.
  3. **Interleave Merge**: Zip-merge the first half (`first = head`) and the reversed second half (`second = reversed_head`).

---

## Observation

1. Interleaving pattern $L_0 \rightarrow L_n \rightarrow L_1 \rightarrow L_{n-1} \dots$ is equivalent to merging two lists:
   - First Half: $L_0 \rightarrow L_1 \rightarrow L_2 \dots$
   - Reversed Second Half: $L_n \rightarrow L_{n-1} \rightarrow L_{n-2} \dots$
2. Splitting at the midpoint and reversing the second half transforms the problem into a simple 2-pointer zip merge!

---

## Intuition

1. Cut the linked list in half at the middle node.
2. Reverse the second half so its nodes are accessed backward ($L_n, L_{n-1}, \dots$).
3. Alternately stitch nodes from the first half and the reversed second half.

---

## Algorithm

1. If `head == nullptr || head->next == nullptr`, return.
2. **Find Middle**:
   - `slow = head`, `fast = head`.
   - While `fast->next != nullptr` and `fast->next->next != nullptr`:
     - `slow = slow->next`.
     - `fast = fast->next->next`.
3. **Reverse Second Half**:
   - `prev = nullptr`, `curr = slow->next`.
   - `slow->next = nullptr` (Disconnect first half).
   - While `curr != nullptr`:
     - `next_node = curr->next`.
     - `curr->next = prev`.
     - `prev = curr`.
     - `curr = next_node`.
   - `second = prev`.
4. **Interleave Merge**:
   - `first = head`.
   - While `second != nullptr`:
     - `tmp1 = first->next`.
     - `tmp2 = second->next`.
     - `first->next = second`.
     - `second->next = tmp1`.
     - `first = tmp1`.
     - `second = tmp2`.

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
    void reorderList(ListNode* head) {
        if (head == nullptr || head->next == nullptr || head->next->next == nullptr) return;
        
        // Step 1: Find middle node
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast->next != nullptr && fast->next->next != nullptr) {
            slow = slow->next;
            fast = fast->next->next;
        }
        
        // Step 2: Reverse second half
        ListNode* prev = nullptr;
        ListNode* curr = slow->next;
        slow->next = nullptr; // Split into two lists
        
        while (curr != nullptr) {
            ListNode* next_node = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next_node;
        }
        
        // Step 3: Interleave two halves
        ListNode* first = head;
        ListNode* second = prev;
        
        while (second != nullptr) {
            ListNode* tmp1 = first->next;
            ListNode* tmp2 = second->next;
            
            first->next = second;
            second->next = tmp1;
            
            first = tmp1;
            second = tmp2;
        }
    }
};
```

---

## Dry Run

### Input
- `head = [1 -> 2 -> 3 -> 4 -> 5]`

### Execution Trace

1. **Find Mid**: `slow` stops at node `3`.
2. **Reverse Second Half**:
   - First Half: `1 -> 2 -> 3 -> nullptr`
   - Reversed Second Half: `5 -> 4 -> nullptr`
3. **Interleave Merge**:
   - Iteration 1: `1 -> 5 -> 2`, `first` at `2`, `second` at `4`.
   - Iteration 2: `2 -> 4 -> 3`, `first` at `3`, `second` at `nullptr`.

### Result
- Output List: `1 -> 5 -> 2 -> 4 -> 3`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Mid search: $N/2$ steps. Reversal: $N/2$ steps. Interleave merge: $N/2$ steps. Total $\mathcal{O}(N)$.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - In-place pointer modifications with zero auxiliary memory allocation.

---

## Why This is Optimal

- Reorders list in linear $\mathcal{O}(N)$ time.
- Uses zero extra memory ($\mathcal{O}(1)$ space).

---

## Common Mistakes

1. **Cycle Creation during Zip Merge**: Forgetting to set `slow->next = nullptr` when splitting the list, creating an infinite cycle during traversal.
2. **Lost Pointers during Interleaving**: Overwriting `first->next` or `second->next` without storing temporary next variables `tmp1` and `tmp2`.
